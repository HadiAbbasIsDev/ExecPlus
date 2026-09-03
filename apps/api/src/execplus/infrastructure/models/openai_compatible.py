"""Use case: Connects ExecPlus to OpenAI-compatible language-model endpoints.

What it does: Translates provider-neutral requests without exposing infrastructure details.
"""

import httpx

from execplus.application.contracts import ModelRequest, ModelResponse
from execplus.domain.models import ModelTier


class OpenAICompatibleLanguageModel:
    def __init__(
        self,
        base_url: str,
        api_key: str,
        small_model: str,
        large_model: str,
        provider_name: str,
        timeout_seconds: float = 60.0,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._models = {ModelTier.SMALL: small_model, ModelTier.LARGE: large_model}
        self._provider_name = provider_name
        self._timeout_seconds = timeout_seconds

    async def complete(self, request: ModelRequest) -> ModelResponse:
        model = self._models[request.tier]
        headers = {"Authorization": f"Bearer {self._api_key}"} if self._api_key else {}
        payload = {
            "model": model,
            "messages": [
                {"role": message.role, "content": message.content}
                for message in request.messages
            ],
            "temperature": request.temperature,
        }
        async with httpx.AsyncClient(timeout=self._timeout_seconds) as client:
            response = await client.post(
                f"{self._base_url}/chat/completions",
                headers=headers,
                json=payload,
            )
            response.raise_for_status()
        body = response.json()
        return ModelResponse(
            content=str(body["choices"][0]["message"]["content"]),
            model=str(body.get("model", model)),
            provider=self._provider_name,
        )
