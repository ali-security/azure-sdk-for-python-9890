# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from promptflow._utils.async_utils import async_run_allowing_running_loop
from azure.ai.evaluation._common.constants import EvaluationMetrics

try:
    from ._content_safety_base import ContentSafetyEvaluatorBase
except ImportError:
    from _content_safety_base import ContentSafetyEvaluatorBase


class _AsyncSelfHarmEvaluator(ContentSafetyEvaluatorBase):
    def __init__(self, azure_ai_project: dict, credential=None):
        super().__init__(
            metric=EvaluationMetrics.SELF_HARM,
            azure_ai_project=azure_ai_project,
            credential=credential,
        )

    async def __call__(self, *, query: str, response: str, **kwargs):
        return await super().__call__(query=query, response=response, **kwargs)


class SelfHarmEvaluator:
    """
    Initialize a self harm evaluator for self harm score.

    :param azure_ai_project: The scope of the Azure AI project.
        It contains subscription id, resource group, and project name.
    :type azure_ai_project: dict
    :param credential: The credential for connecting to Azure AI project.
    :type credential: ~azure.core.credentials.TokenCredential

    **Usage**

    .. code-block:: python

        azure_ai_project = {
            "subscription_id": "<subscription_id>",
            "resource_group_name": "<resource_group_name>",
            "project_name": "<project_name>",
        }
        eval_fn = SelfHarmEvaluator(azure_ai_project)
        result = eval_fn(query="What is the capital of France?", response="Paris.")

    **Output format**

    .. code-block:: python

        {
            "self_harm": "High",
            "self_harm_score": 6.5,
            "self_harm_reason": "Some reason"
        }
    """

    def __init__(self, azure_ai_project: dict, credential=None):
        self._async_evaluator = _AsyncSelfHarmEvaluator(azure_ai_project, credential)

    def __call__(self, *, query: str, response: str, **kwargs):
        """
        Evaluates self harm content.

        :keyword query: The query to be evaluated.
        :paramtype query: str
        :keyword response: The response to be evaluated.
        :paramtype response: str
        :return: The self harm score.
        :rtype: dict
        """
        return async_run_allowing_running_loop(self._async_evaluator, query=query, response=response, **kwargs)

    def _to_async(self):
        return self._async_evaluator
