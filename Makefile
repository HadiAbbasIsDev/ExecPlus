# Use case: Provides a stable command surface for common developer and CI workflows.
# What it does: Wraps environment setup, local services, applications, tests, and static analysis.

.PHONY: install dev-infra down api web format lint typecheck test check

COMPOSE ?= docker-compose

install:
	python3 -m pip install -e '.[dev]'
	npm install

dev-infra:
	$(COMPOSE) up -d postgres minio

down:
	$(COMPOSE) down

api:
	python3 -m uvicorn execplus.main:app --app-dir apps/api/src --reload --host 0.0.0.0 --port 8000

web:
	npm run dev:web

format:
	python3 -m ruff format apps/api/src apps/api/tests tests
	python3 -m ruff check --fix apps/api/src apps/api/tests tests

lint:
	python3 -m ruff check apps/api/src apps/api/tests tests
	npm run lint:web

typecheck:
	python3 -m mypy
	npm run typecheck:web

test:
	python3 -m pytest
	npm run test:web

check: lint typecheck test
	npm run build:web
