> **File use case:** Architecture decision record for numerical-answer integrity.
> **What it does:** Makes executable queries and lineage mandatory for every numerical answer.

# ADR 0002: Numerical answers require exact computation

- Status: Accepted
- Date: 2026-09-02

## Context

Business users require trustworthy figures. Language models are probabilistic and can generate plausible but incorrect values.

## Decision

Language models may interpret requests and propose read-only query plans. DuckDB or PostgreSQL executes validated plans. Answer assembly accepts numerical claims only from typed execution results and attaches dataset, record count, metric, aggregation, grouping, filters, query, and execution identifiers.

## Consequences

Unexecutable, ambiguous, or unsupported requests return clarification or refusal. Accuracy testing can use fixed datasets and golden query results. Narrative freedom is intentionally constrained by traceable evidence.

