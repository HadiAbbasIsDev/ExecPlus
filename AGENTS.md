> **File use case:** Persistent handoff and operating guide for humans and coding agents working on ExecPlus.
> **What it does:** Records current state, non-negotiable rules, commands, boundaries, and the next approved slice of work.

# ExecPlus Engineering Handoff

Read this file, `ROADMAP.md`, and `docs/architecture.md` before changing the project.

## Current state

- Phase 0: Engineering Foundation is complete as of 2026-09-02.
- The repository is a Python and TypeScript modular monorepo.
- The API has liveness and readiness endpoints.
- Language models and vector databases are represented by provider-neutral protocols.
- No vector database vendor has been selected.
- The local-model path expects an OpenAI-compatible endpoint so Ollama, vLLM, or another server can be evaluated later.
- Runtime model selection is composed in `execplus/bootstrap.py`; routes and use cases must not branch on vendors.
- DuckDB is the planned Phase 1 compute engine for uploaded files.
- PostgreSQL is reserved for control-plane metadata, permissions, conversations, lineage, and audit records.
- MinIO provides an S3-compatible local object-store target.
- Authentication provider selection remains an explicit Phase 1 decision.
- No product feature should be represented as implemented unless tests prove it.

## Non-negotiable engineering rules

1. Never ask an LLM to calculate or supply a business number.
2. Execute validated, read-only queries and build answers from returned results.
3. Scope every resource lookup and mutation by `workspace_id`.
4. Apply permissions before query execution and before hybrid retrieval.
5. Return clarification for ambiguous requests and a supported-scope explanation for impossible requests.
6. Record model route, generated query, execution outcome, lineage, and returned answer in the audit trail.
7. Keep domain and application modules independent from web frameworks and infrastructure SDKs.
8. Add or update tests with each behavior change.
9. Update `ROADMAP.md` and this current-state section only when evidence supports the status change.
10. Do not commit datasets, secrets, model weights, generated exports, or local database volumes.
11. Put a file-level use-case and responsibility header at the top of every new file.
12. Do not add inline explanatory comments; prefer clear names, small functions, tests, and architecture documents.
13. Next.js can regenerate `next-env.d.ts`; restore its required file-purpose header before committing.

## Dependency direction

```text
presentation -> application -> domain
infrastructure -> application ports and domain
domain -> standard library only
```

Framework imports are forbidden in `execplus/domain`. Application services depend on protocols in `execplus/application/ports.py`, not concrete providers.

## Commands

```bash
make install
make check
make test
make api
make web
make dev-infra
make down
```


## Definition of done

- Acceptance criteria have automated coverage.
- Unit tests and architecture tests pass.
- Static analysis passes.
- Tenant isolation and numerical lineage are considered explicitly.
- Public contracts and configuration are documented.
- Logs contain identifiers and outcomes, not uploaded row values or secrets.
- Roadmap and handoff state reflect the tested implementation.

## Next approved slice

Begin Phase 1 with workspace-aware upload validation and profiling:

1. Select and integrate the authentication provider behind an identity port.
2. Add PostgreSQL migrations for workspaces, memberships, datasets, uploads, and audit events.
3. Implement streamed CSV and XLSX validation with a 20 MB enforced limit.
4. Reject multi-sheet or merged-cell workbooks before persistence.
5. Persist uploads under workspace-scoped object keys.
6. Profile rows, columns, types, date ranges, dimensions, metrics, and semantic tags.
7. Add contract, unit, integration, and tenant-isolation tests.

Do not begin conversational query generation until ingestion isolation and profiling acceptance criteria pass.
