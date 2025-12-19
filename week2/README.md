# Action Item Extractor

A robust backend service designed to extract actionable tasks and todos from unstructured text notes. The project leverages both rule-based heuristics and LLM-powered extraction (via Ollama) to provide precise task identification.

## Project Overview

The Action Item Extractor is a FastAPI-based application that allows users to:
- Save and store meeting notes.
- Extract action items using a classic rule-based approach.
- Extract action items using a sophisticated LLM approach with Mistral-Nemo.
- Manage extracted tasks by marking them as completed.
- Persist data in a local SQLite database.

## Features

- LLM Integration: Uses Ollama and Mistral-Nemo:12b for structured data extraction.
- Dual Extraction Modes: Classic (rule-based) and LLM-based for high accuracy.
- Schema Validation: Pydantic-based API contracts for reliable data handling.
- Lightweight Frontend: A responsive HTML/JS interface for interacting with the service.

## Setup and Installation

### Prerequisites

- Python 3.12 or higher.
- Conda (recommended for environment management).
- Ollama (installed and running locally).
- Mistral-Nemo model pulled in Ollama: `ollama pull mistral-nemo:12b`.

### Environment Setup

1. Create and activate the conda environment:
   ```bash
   conda activate cs146s
   ```

2. Install dependencies:
   ```bash
   pip install fastapi uvicorn pydantic ollama python-dotenv pytest
   ```

3. Ensure Ollama is running in the background.

### Running the Application

Start the FastAPI server using uvicorn from the project root:

```bash
uvicorn week2.app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Notes
- `POST /notes`: Create a new note.
- `GET /notes`: List all saved notes.
- `GET /notes/{note_id}`: Retrieve a specific note.

### Action Items
- `POST /action-items/extract`: Extract action items using classic rule-based logic.
- `POST /action-items/extract-llm`: Extract action items using Mistral-Nemo LLM.
- `GET /action-items`: List all action items (optional filtering by note_id).
- `POST /action-items/{action_item_id}/done`: Mark an action item as completed or incomplete.

## Test Suite

The project uses pytest for automated testing, including mocked LLM responses to ensure deterministic results.

### Running Tests

Execute the following command to run all unit tests:

```bash
python -m pytest week2/tests/test_extract.py
```

## Architecture

- `app/main.py`: Entry point and application lifecycle management.
- `app/db.py`: Database connection and resource management using context managers.
- `app/schemas.py`: Pydantic models defining API contracts.
- `app/routers/`: Modular route definitions for notes and action items.
- `app/services/`: Business logic for item extraction routines.
- `frontend/`: Minimalist HTML and JavaScript client.
