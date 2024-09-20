# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import os
from typing import Optional, Any

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
from azure.core.credentials import AccessTokenInfo
from ... import CredentialUnavailableError
from ..._constants import EnvironmentVariables
from .._internal import AsyncContextManager
from .._internal.get_token_mixin import GetTokenMixin
from .._internal.managed_identity_client import AsyncManagedIdentityClient
from ..._internal import within_credential_chain
from ..._credentials.imds import _get_request, _check_forbidden_response, PIPELINE_SETTINGS


class ImdsCredential(AsyncContextManager, GetTokenMixin):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__()

        self._client = AsyncManagedIdentityClient(_get_request, **dict(PIPELINE_SETTINGS, **kwargs))
        if EnvironmentVariables.AZURE_POD_IDENTITY_AUTHORITY_HOST in os.environ:
            self._endpoint_available: Optional[bool] = True
        else:
            self._endpoint_available = None
        self._user_assigned_identity = "client_id" in kwargs or "identity_config" in kwargs

    async def __aenter__(self) -> "ImdsCredential":
        await self._client.__aenter__()
        return self

    async def close(self) -> None:
        await self._client.close()

    async def _acquire_token_silently(self, *scopes: str, **kwargs: Any) -> Optional[AccessTokenInfo]:
        return self._client.get_cached_token(*scopes)

    async def _request_token(self, *scopes: str, **kwargs: Any) -> AccessTokenInfo:  # pylint:disable=unused-argument

        if within_credential_chain.get() and not self._endpoint_available:
            # If within a chain (e.g. DefaultAzureCredential), we do a quick check to see if the IMDS endpoint
            # is available to avoid hanging for a long time if the endpoint isn't available.
            try:
                await self._client.request_token(*scopes, connection_timeout=1, retry_total=0)
                self._endpoint_available = True
            except HttpResponseError as ex:
                # IMDS responded
                _check_forbidden_response(ex)
                self._endpoint_available = True
            except Exception as ex:  # pylint:disable=broad-except
                error_message = (
                    "ManagedIdentityCredential authentication unavailable, no response from the IMDS endpoint."
                )
                raise CredentialUnavailableError(message=error_message) from ex

        try:
            token_info = await self._client.request_token(*scopes, headers={"Metadata": "true"})
        except CredentialUnavailableError:
            # Response is not json, skip the IMDS credential
            raise
        except HttpResponseError as ex:
            # 400 in response to a token request indicates managed identity is disabled,
            # or the identity with the specified client_id is not available
            if ex.status_code == 400:
                error_message = "ManagedIdentityCredential authentication unavailable. "
                if self._user_assigned_identity:
                    error_message += "The requested identity has not been assigned to this resource."
                else:
                    error_message += "No identity has been assigned to this resource."

                if ex.message:
                    error_message += f" Error: {ex.message}"

                raise CredentialUnavailableError(message=error_message) from ex

            _check_forbidden_response(ex)
            # any other error is unexpected
            raise ClientAuthenticationError(message=ex.message, response=ex.response) from ex
        except Exception as ex:  # pylint:disable=broad-except
            # if anything else was raised, assume the endpoint is unavailable
            error_message = "ManagedIdentityCredential authentication unavailable, no response from the IMDS endpoint."
            raise CredentialUnavailableError(error_message) from ex
        return token_info
