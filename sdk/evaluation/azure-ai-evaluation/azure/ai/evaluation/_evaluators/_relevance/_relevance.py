# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import os
import re

import numpy as np
from promptflow._utils.async_utils import async_run_allowing_running_loop
from promptflow.core import AsyncPrompty

from azure.ai.evaluation._exceptions import ErrorBlame, ErrorCategory, ErrorTarget, EvaluationException

from ..._common.utils import construct_prompty_model_config

try:
    from ..._user_agent import USER_AGENT
except ImportError:
    USER_AGENT = None


class _AsyncRelevanceEvaluator:
    # Constants must be defined within eval's directory to be save/loadable
    PROMPTY_FILE = "relevance.prompty"
    LLM_CALL_TIMEOUT = 600
    DEFAULT_OPEN_API_VERSION = "2024-02-15-preview"

    def __init__(self, model_config: dict):
        prompty_model_config = construct_prompty_model_config(
            model_config,
            self.DEFAULT_OPEN_API_VERSION,
            USER_AGENT,
        )

        current_dir = os.path.dirname(__file__)
        prompty_path = os.path.join(current_dir, self.PROMPTY_FILE)
        self._flow = AsyncPrompty.load(source=prompty_path, model=prompty_model_config)

    async def __call__(self, *, query: str, response: str, context: str, **kwargs):
        # Validate input parameters
        query = str(query or "")
        response = str(response or "")
        context = str(context or "")

        if not (query.strip() and response.strip() and context.strip()):
            msg = "'query', 'response' and 'context' must be non-empty strings."
            raise EvaluationException(
                message=msg,
                internal_message=msg,
                error_category=ErrorCategory.MISSING_FIELD,
                error_blame=ErrorBlame.USER_ERROR,
                error_target=ErrorTarget.RELEVANCE_EVALUATOR,
            )

        # Run the evaluation flow
        llm_output = await self._flow(
            query=query, response=response, context=context, timeout=self.LLM_CALL_TIMEOUT, **kwargs
        )

        score = np.nan
        if llm_output:
            match = re.search(r"\d", llm_output)
            if match:
                score = float(match.group())

        return {"gpt_relevance": float(score)}


class RelevanceEvaluator:
    """
    Initialize a relevance evaluator configured for a specific Azure OpenAI model.

    :param model_config: Configuration for the Azure OpenAI model.
    :type model_config: Union[~azure.ai.evaluation.AzureOpenAIModelConfiguration,
        ~azure.ai.evaluation.OpenAIModelConfiguration]

    **Usage**

    .. code-block:: python

        eval_fn = RelevanceEvaluator(model_config)
        result = eval_fn(
            query="What is the capital of Japan?",
            response="The capital of Japan is Tokyo.",
            context="Tokyo is Japan's capital, known for its blend of traditional culture \
                and technological advancements.")

    **Output format**

    .. code-block:: python

        {
            "gpt_relevance": 3.0
        }
    """

    def __init__(self, model_config: dict):
        self._async_evaluator = _AsyncRelevanceEvaluator(model_config)

    def __call__(self, *, query: str, response: str, context: str, **kwargs):
        """
        Evaluate relevance.

        :keyword query: The query to be evaluated.
        :paramtype query: str
        :keyword response: The response to be evaluated.
        :paramtype response: str
        :keyword context: The context to be evaluated.
        :paramtype context: str
        :return: The relevance score.
        :rtype: dict
        """
        return async_run_allowing_running_loop(
            self._async_evaluator, query=query, response=response, context=context, **kwargs
        )

    def _to_async(self):
        return self._async_evaluator
