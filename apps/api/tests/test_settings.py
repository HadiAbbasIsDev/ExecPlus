"""Use case: Verifies fail-fast runtime configuration.

What it does: Prevents incomplete model routes from reaching startup.
"""

import pytest
from pydantic import ValidationError

from execplus.config import Settings


def test_models_can_remain_disabled() -> None:
    settings = Settings(_env_file=None, llm_mode="disabled")

    assert settings.llm_mode == "disabled"


def test_local_route_requires_both_model_names() -> None:
    with pytest.raises(ValidationError, match="EXECPLUS_LLM_LARGE_MODEL"):
        Settings(
            _env_file=None,
            llm_mode="local",
            llm_small_model="small-local",
            llm_large_model="",
        )


def test_hosted_route_requires_an_api_key() -> None:
    with pytest.raises(ValidationError, match="EXECPLUS_LLM_API_KEY"):
        Settings(
            _env_file=None,
            llm_mode="hosted",
            llm_small_model="small-hosted",
            llm_large_model="large-hosted",
            llm_api_key="",
        )
