# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from devtools_testutils.aio import recorded_by_proxy_async
from preparer import TextTranslationPreparer
from testcase import TextTranslationTest


class TestDictionaryLookupAsync(TextTranslationTest):
    @TextTranslationPreparer()
    @recorded_by_proxy_async
    async def test_single_input_element(self, **kwargs):
        endpoint = kwargs.get("translation_text_endpoint")
        apikey = kwargs.get("translation_text_apikey")
        region = kwargs.get("translation_text_region")
        client = self.create_async_client(endpoint, apikey, region)

        from_parameter = "en"
        to = "es"
        input_text_elements = ["fly"]

        async with client:
            response = await client.lookup_dictionary_entries(
                body=input_text_elements, from_parameter=from_parameter, to=to
            )
        assert response is not None
        assert response[0].normalized_source == "fly"
        assert response[0].display_source == "fly"

    @TextTranslationPreparer()
    @recorded_by_proxy_async
    async def test_multiple_input_elements(self, **kwargs):
        endpoint = kwargs.get("translation_text_endpoint")
        apikey = kwargs.get("translation_text_apikey")
        region = kwargs.get("translation_text_region")
        client = self.create_async_client(endpoint, apikey, region)

        from_parameter = "en"
        to = "es"
        input_text_elements = ["fly", "fox"]

        async with client:
            response = await client.lookup_dictionary_entries(
                body=input_text_elements, from_parameter=from_parameter, to=to
            )
        assert response is not None
        assert len(response) == 2
        assert response[0].normalized_source == "fly"
        assert response[0].display_source == "fly"
        assert response[1].normalized_source == "fox"
        assert response[1].display_source == "fox"
