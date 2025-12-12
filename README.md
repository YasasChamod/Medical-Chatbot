# Medical Chatbot

A small Python project scaffold for a medical chatbot. This repository currently contains the project layout and placeholders for core modules. The README below explains how to set up the development environment, where to add code, and suggested next steps to make the project runnable.

## Overview

- **Purpose:** Provide a starting point for a medical chatbot using LangChain, vector stores (e.g., Pinecone), and an API/webapp interface.
- **Status:** Starter scaffold — some files (e.g., `app.py`, `src/`) are present but not yet implemented. This README documents how to get started and where to add the missing pieces.

## Quick Links

- Code entry: `app.py`
- Python package code: `src/`
- Requirements: `requirements.txt`

## Prerequisites

- Python 3.10+ (3.10 recommended)
- Git
- (Optional) Conda
- API keys for services you plan to use (e.g., OpenAI, Pinecone)

## Installation (PowerShell)

1. Clone the repository:

```powershell
git clone https://github.com/YasasChamod/Medical-Chatbot.git
cd "Medical-Chatbot"
```

2. Create and activate a virtual environment (venv) or use conda:

Using venv (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Using conda (optional):

```powershell
conda create -n medibot python=3.10 -y; conda activate medibot
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add any required keys (example):

```
OPENAI_API_KEY="your-openai-key"
PINECONE_API_KEY="your-pinecone-key"
PINECONE_ENVIRONMENT="us-east1-gcp"
```

Note: This repo currently does not include the code that calls these services. Add or enable the relevant modules before attempting to use them.

## Usage (what to do next)

- The repository currently lacks an implemented `app.py` and the core scripts to build/store embeddings. To run a web app or CLI you should implement the main entry in `app.py` (Flask/FastAPI) and the vector store utilities (e.g., `store_index.py`) in the codebase.
- Suggested minimal flow you can implement:
	1. Create `scripts/store_index.py` that builds embeddings and uploads them to Pinecone (or a local FAISS index).
	2. Implement `app.py` to load the index and expose a chat API (Flask or FastAPI).
	3. Add a simple HTML/JS frontend or use curl to test the API.

Example (placeholder) command that will work once those scripts exist:

```powershell
python scripts/store_index.py
python app.py
# then open http://localhost:5000
```

## Project Structure

- `app.py` — application entrypoint (currently empty)
- `requirements.txt` — Python dependencies
- `src/` — package folder (place your modules here)
	- `src/helper.py` — helper utilities (placeholder)
	- `src/prompt.py` — prompt templates and prompt-building logic (placeholder)
- `research/` — notebooks and experiments

## Development notes

- Use `src/` for library code and keep `app.py` minimal (web server startup + wiring).
- Keep secrets out of source control. Use `.env` + `python-dotenv` or environment variables in CI.
- Add tests when you implement behavior; consider a `tests/` folder and `pytest`.

## Deployment notes (optional)

This section contains suggestions only — there is no deployment automation in the repo yet.

- Containerize with a `Dockerfile` and push to ECR for AWS deployment.
- Use GitHub Actions for CI/CD and store secrets in repository Actions secrets.

## Contributing

If you'd like me to implement the missing scripts and make the app runnable, tell me which runtime you prefer (Flask or FastAPI) and whether you want Pinecone or a local FAISS index — I can then:

- implement `scripts/store_index.py`
- implement `app.py` and a simple web UI
- add step-by-step usage examples and tests

## License

See `LICENSE` in the repository root.

## Contact

If you want changes to the README or want me to implement the runnable parts, reply with the preferred web framework and vector store.
