"""Use case: Declares replaceable infrastructure capabilities.

What it does: Defines contracts for queries, models, retrieval, and readiness.
"""

from typing import Protocol
from uuid import UUID

from execplus.application.contracts import (
    ComponentStatus,
    KnowledgeChunk,
    ModelRequest,
    ModelResponse,
    RetrievalHit,
)
from execplus.domain.models import QueryPlan, QueryResult, WorkspaceScope


class QueryExecutor(Protocol):
    async def execute(self, plan: QueryPlan, scope: WorkspaceScope) -> QueryResult: ...


class LanguageModel(Protocol):
    async def complete(self, request: ModelRequest) -> ModelResponse: ...


class EmbeddingStore(Protocol):
    async def upsert(self, chunks: tuple[KnowledgeChunk, ...]) -> None: ...

    async def search(
        self,
        query: str,
        scope: WorkspaceScope,
        dataset_ids: frozenset[UUID],
        limit: int,
    ) -> tuple[RetrievalHit, ...]: ...

    async def delete_dataset(self, workspace_id: UUID, dataset_id: UUID) -> None: ...


class ReadinessProbe(Protocol):
    @property
    def name(self) -> str: ...

    async def check(self) -> ComponentStatus: ...
