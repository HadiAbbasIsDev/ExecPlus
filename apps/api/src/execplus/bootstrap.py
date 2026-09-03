"""Use case: Composes provider implementations from validated settings.

What it does: Selects disabled, local, or hosted model adapters at the application edge.
"""

from execplus.application.ports import LanguageModel
from execplus.config import Settings
from execplus.infrastructure.models.disabled import DisabledLanguageModel
from execplus.infrastructure.models.openai_compatible import OpenAICompatibleLanguageModel


def build_language_model(settings: Settings) -> LanguageModel:
    if settings.llm_mode == "disabled":
        return DisabledLanguageModel()
    return OpenAICompatibleLanguageModel(
        base_url=settings.llm_base_url,
        api_key=settings.llm_api_key,
        small_model=settings.llm_small_model,
        large_model=settings.llm_large_model,
        provider_name=settings.llm_mode,
    )

