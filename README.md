# RapidRAG
An optimized RAG system to allow users to provide data via upload of documents, and then chat about the content. Built using FastAPI  + LLM APIs

## Tech Stack

- **Backend**: FastAPI for building a RESTful API with async support:
  - `fastapi[all]`: Includes all dependencies for full FastAPI functionality (e.g., `pydantic`, `uvicorn`, `starlette`).

- **Frontend**: TBD
- **AI/NLP**:
  - `fastapi[all]`: Includes all dependencies for full FastAPI functionality (e.g., `pydantic`, `uvicorn`, `starlette`).
- **Database**: PostgreSQL (Planned)
- **CI/CD**: GitHub Actions (To be added)
- **Environment & Deployment**: Docker, Docker Compose (Planned)
- **Others**: Redis (For caching, planned)

## Running the Backend

To run the FastAPI backend, use the `uvicorn` ASGI server:

```bash
uvicorn app.main:app --reload
```

### Prerequisites
Make sure you have all the dependencies installed. You can do this by running:
```bash
pip install -r requirements.txt
```

## Setting Up Environment Variables

The app relies on .env to load various values. An`.env.example` is provided to list the names, but not the values. Follow the steps below to setup your .env file:

1. Copy the `example.env` file to a `.env` file:
    ```bash
    cp .env.example .env
    ```

2. Edit the `.env` file and set the correct values (chosen by your team, or referred in a shared private document)



