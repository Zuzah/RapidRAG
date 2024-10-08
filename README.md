# RapidRAG
An optimized RAG system to allow users to provide data via upload of documents, and then chat about the content. Built using FastAPI  + LLM APIs

## Tech Stack

- **Backend**: FastAPI for building a RESTful API with async support:
  - `fastapi[all]`: Includes all dependencies for full FastAPI functionality (e.g., `pydantic`, `uvicorn`, `starlette`).

- **Frontend**:
  - `TBD`:
- **AI/NLP**:
  - `TBD`:
- **Database**: PostgreSQL (Planned)
- **CI/CD**: GitHub Actions (To be added)
- **Environment & Deployment**: Docker, Docker Compose (Planned)
- **Others**: Redis (For caching, planned)

## Running the Backend

To run the FastAPI backend, use the `uvicorn` ASGI server. Execute via poetry:

```bash
poetry run uvicorn app.main:app --reload
```

### Prerequisites
Make sure you have **Poetry** installed and the necessary dependencies set up:

1. **Install Poetry:** (if not already installed): Follow the instructions to install Poetry from the official documentation, or use this command:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. **Install Project Dependencies:** Once Poetry is installed, run the following command in the project root (where pyproject.toml is located) to install all dependencies:
```bash
poetry install
```

3. **Activate Poetry Environment:**: You can either enter a Poetry-managed shell.:
```bash
poetry shell
```

Or run commands directly with:
```bash
poetry run <command>
```

4. **Running Uvicorn (for development)**: Once the dependencies are installed, you can start the FastAPI server:

```bash
poetry run uvicorn app.main:app --reload
```

## Setting Up Environment Variables

The app relies on .env to load various values. An`.env.example` is provided to list the names, but not the values. Follow the steps below to setup your .env file:

1. Copy the `example.env` file to a `.env` file:
    ```bash
    cp .env.example .env
    ```

2. Edit the `.env` file and set the correct values (chosen by your team, or referred in a shared private document)

## Common Commands

Here are the essential commands for working with this project:

### Poetry Commands

- **Install dependencies:**
  ```bash
  poetry install
  ```

- **Activate Poetry shell:**
  ```bash
  poetry shell
  ```

- **Run FastAPI server (development):**
  ```bash
  poetry run uvicorn app.main:app --reload
  ```
### Linting with `ruff`

- **Run `ruff` to check code style:**
  ```bash
  poetry run ruff check .
  ```

- **Automatically fix linting issues with `ruff`:**
  ```bash
  poetry run ruff check . --fix
  ```
### Pre-Commit Hooks

Pre-commit hooks are scripts that run automatically before you make a commit and aim .improve code quality. They can also be executed locally for testing:

- **Run the pre-commit hooks manually:**
  ```bash
  poetry run pre-commit run --all-files
  ```
