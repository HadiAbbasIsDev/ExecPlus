"""Use case: Supplies retrieval before a vector provider is selected.

What it does: Fails explicitly instead of returning incomplete knowledge results.
"""

from uuid import UUID

from execplus.application.contracts import KnowledgeChunk, RetrievalHit
from execplus.domain.errors import ProviderUnavailableError
from execplus.domain.models import WorkspaceScope


class DisabledEmbeddingStore:
    async def upsert(self, chunks: tuple[KnowledgeChunk, ...]) -> None:
        raise ProviderUnavailableError("Vector retrieval is disabled")

    async def search(
        self,
        query: str,
        scope: WorkspaceScope,
        dataset_ids: frozenset[UUID],
        limit: int,
    ) -> tuple[RetrievalHit, ...]:
        raise ProviderUnavailableError("Vector retrieval is disabled")

    async def delete_dataset(self, workspace_id: UUID, dataset_id: UUID) -> None:
        raise ProviderUnavailableError("Vector retrieval is disabled")
