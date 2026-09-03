"""Use case: Verifies runtime language-model selection.

What it does: Protects configuration-driven switching between disabled, local, and hosted routes.
"""

from execplus.bootstrap import build_language_model
from execplus.config import Settings
from execplus.infrastructure.models.disabled import DisabledLanguageModel
from execplus.infrastructure.models.openai_compatible import OpenAICompatibleLanguageModel


def test_disabled_model_route_has_no_external_dependency() -> None:
    model = build_language_model(Settings(_env_file=None, llm_mode="disabled"))

    assert isinstance(model, DisabledLanguageModel)


def test_local_model_route_uses_compatible_adapter() -> None:
    settings = Settings(
        _env_file=None,
        llm_mode="local",
        llm_small_model="local-small",
        llm_large_model="local-large",
    )

    model = build_language_model(settings)

    assert isinstance(model, OpenAICompatibleLanguageModel)


def test_hosted_model_route_uses_compatible_adapter() -> None:
    settings = Settings(
        _env_file=None,
        llm_mode="hosted",
        llm_api_key="test-key",
        llm_small_model="hosted-small",
        llm_large_model="hosted-large",
    )

    model = build_language_model(settings)

    assert isinstance(model, OpenAICompatibleLanguageModel)
