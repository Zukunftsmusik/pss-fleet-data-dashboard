# setup
.PHONY: init-dev
init-dev:
	uv self update
	uv sync --project backend
	rm -rf frontend/node_modules frontend/package-lock.json
	cd frontend && npx --package=node -c "npm install --legacy-peer-deps"

.PHONY: update
update:
	uv sync --project backend --upgrade


# dev tools
.PHONY: lock
lock:
	uv export --project backend --no-hashes --no-header --no-annotate --no-dev --format requirements.txt > backend/requirements.txt
	uv export --project backend --no-hashes --no-header --no-annotate --format requirements.txt > backend/requirements-dev.txt


# formatting and linting
.PHONY: check
check:
	uv run --project backend ruff check ./backend/app
	uv run --project backend vulture ./backend/app

.PHONY: format
format:
	uv run --project backend ruff check --fix ./backend/app ./backend/tests
	uv run --project backend ruff format ./backend/app ./backend/tests


# testing
.PHONY: coverage
coverage:
	uv run --project backend pytest --cov=./backend/app --cov-report=xml:backend/cov.xml --cov-report=term --cov-report=lcov

.PHONY: test
test:
	uv run --project backend pytest tests


# run

.PHONY: run-backend
run-backend:
	# Starts the FastAPI server on port 8000 with auto-reload enabled
	uv run --directory backend uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

.PHONY: run-frontend
run-frontend:
	# Navigates to frontend and boots the Vite dev server on port 5173
	cd frontend && npx --package=node -c "npm run dev"