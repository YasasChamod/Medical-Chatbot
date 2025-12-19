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

# Medical Chatbot (Medibot)

A small Flask-based medical chatbot web app using a retrieval-augmented generation (RAG) pattern. This repository contains a working `app.py` Flask server plus a simple web UI in `templates/index.html` and `static/style.css`.

## Status
- Core app: `app.py` is implemented and starts a Flask server.
- Frontend: `templates/index.html` + `static/style.css` provide a dark-themed UI with message bubbles, a professional "Dr. Medibot" header and Enter-to-submit behavior.

## Quick links
- Server entry: `app.py`
- Frontend template: `templates/index.html`
- Styles: `static/style.css`
- Python package code: `src/`

## Prerequisites
- Python 3.10+
- Git
- (Optional) Conda
- Required API keys and services used by the embedding / vector store (for example Pinecone, GROQ/OpenAI). Place secret keys in a `.env` file.

## Setup (PowerShell)
1. Clone the repository:

```powershell
git clone https://github.com/YasasChamod/Medical-Chatbot.git
cd "Medical-Chatbot"
```

2. Create and activate a virtual environment (venv) or use conda:

Using venv:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Using conda (optional):

```powershell
conda create -n medibot python=3.10 -y
conda activate medibot
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Create a `.env` file in the project root containing any required keys, e.g.:

```env
OPENAI_API_KEY="your-openai-key"
PINECONE_API_KEY="your-pinecone-key"
PINECONE_ENVIRONMENT="your-pinecone-environment"
```

## Running the app locally
1. Ensure your environment is active and required keys are present.
2. Start the app:

```powershell
python app.py
```

3. Open http://127.0.0.1:5000 in your browser.

### Notes about embeddings and vector store
- The Flask app expects the embedding and vector store pieces (see `src/helper.py` and `store_index.py`) to be configured for your chosen provider (Pinecone, FAISS, etc.). If you don't yet have embeddings or a Pinecone index, implement `store_index.py` or modify `src/helper.py` to use a local index.

## Frontend features (what changed)
- Dark theme with improved readability: `static/style.css`.
- Professional header: the UI now shows a `Dr. Medibot` header with an avatar (`templates/index.html`).
- Message bubbles with avatars and sender labels instead of plain text messages.
- Enter-to-submit: pressing Enter sends the message (clicking Ask still works). To change this behavior to support Shift+Enter for newlines, see the note below.

## Customization tips
- Change accent/button color: edit the `background` value for the `button` selector and `.message-row.bot .message` in `static/style.css`.
- Use an image avatar: replace the `.header .avatar` content in `templates/index.html` with an `<img src="/static/doctor.png" alt="doctor"/>` and add the image to `static/`.
- Make Enter create newlines (Shift+Enter to submit): modify the keydown handler in `templates/index.html` (I can do this for you).

## Development notes
- `app.py` runs Flask in debug mode when executed directly. For production, use a WSGI server (Gunicorn/Uvicorn) and set debug=False.
- Keep secrets out of source control and prefer environment variables or a secure secrets store in deployment.

## Next steps I can help with
- Implement `store_index.py` to build embeddings and populate a Pinecone or FAISS index.
- Add Shift+Enter multiline input behavior.
- Swap emoji avatars for images and tune styling (colors, spacing).

## License
See `LICENSE` in the repository root.

If you want, I can update the README further with screenshots or add a short GIF demonstrating Enter-to-submit and message bubbles.
