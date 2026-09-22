# Ollama Local Chatbot

A lightweight, private chat application for interacting with locally hosted AI models through [Ollama](https://ollama.com/) and [Streamlit](https://streamlit.io/). The app provides a simple browser-based conversation interface while keeping model execution on your own machine.

## Overview

This project connects a Streamlit user interface to the Ollama Python client. When the application starts, it asks Ollama for the models installed locally and lets you choose one from the sidebar. Messages are sent to the selected model with streaming enabled, so the assistant response appears progressively as it is generated.

The application is intentionally small and easy to extend. It is suitable for experimenting with local language models, building a private personal assistant, or using as a starting point for a more capable AI application.

##  Screenshots

![](.screenShot1.png)

## Features

- Chat with locally hosted Ollama models from a web browser.
- Automatically discover models available in the local Ollama installation.
- Select the active model from the sidebar.
- Enter a model name manually if Ollama is unavailable when the page loads.
- Stream assistant responses token by token for a responsive experience.
- Preserve the conversation in Streamlit session state while interacting with the app.
- Render user and assistant messages in separate chat containers.
- Clear the current conversation with one button.
- Run without a cloud API key or a remote AI provider.
- Use a centered, minimal interface with a dedicated settings sidebar.

## Technology Stack

| Technology | Purpose |
| --- | --- |
| Python | Application language |
| Streamlit | Web interface, chat components, session state, and page configuration |
| Ollama | Local model runtime and chat API |
| `ollama` Python package | Python client used to list models and stream chat responses |
| `uv` build backend | Packaging and project build configuration |

The project declares Python `3.13` or newer in `pyproject.toml`.

## How It Works

1. Streamlit loads `app.py` and configures the page title, icon, and layout.
2. The sidebar calls `ollama.list()` to retrieve locally available models.
3. The selected model is used when a user submits a prompt.
4. The prompt is added to the session conversation history.
5. The app calls `ollama.chat()` with the full message history and `stream=True`.
6. Each streamed response chunk is appended and rendered immediately.
7. The completed assistant response is added to the conversation history.

Conversation history is stored in `st.session_state`, so it remains available across Streamlit reruns for the active browser session. It is not persisted to a database or written to disk.

## Prerequisites

Before running the application, install:

- Python 3.13 or newer
- Ollama
- At least one Ollama model

Install Ollama from [ollama.com](https://ollama.com/download). After installation, make sure the Ollama service is running and download a model. For example:

```bash
ollama pull llama3
```

You can use any model supported by your Ollama installation. The model name entered in the app must match the name reported by Ollama.

## Installation

Clone or download this project, then create and activate a virtual environment:

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

The project also includes `pyproject.toml` for modern Python packaging workflows. With `uv`, dependencies can be installed with:

```powershell
uv sync
```

## Run the Application

Start Ollama first, then launch Streamlit from the project root:

```powershell
streamlit run app.py
```

Streamlit will print a local URL, typically:

```text
http://localhost:8501
```

Open that URL in a browser, select an available model, and start chatting.

## Using the Interface

1. Open the application in your browser.
2. Choose an installed model from **Settings** in the sidebar.
3. Type a prompt into the chat input at the bottom of the page.
4. Submit the prompt and watch the response stream into the conversation.
5. Select **Clear Chat History** to start a new conversation.

If the app cannot connect to Ollama, it displays the connection error and provides a text field where you can enter a model name manually. Ollama still needs to be running successfully for a response to be generated.

## Project Structure

```text
chatbot/
├── app.py                 # Streamlit application and Ollama chat flow
├── pyproject.toml         # Project metadata, dependencies, and build settings
├── requirements.txt       # Runtime dependencies for pip installation
└── src/
    └── chatbot/
        └── __init__.py    # Package entry point
```

The primary application logic currently lives in `app.py`. The `src/chatbot` package is included for packaging and future modularization.

## Privacy

Prompts and responses are sent to the local Ollama service for inference. This application does not include a cloud AI integration, telemetry, authentication, or persistence layer. Network behavior can still depend on Ollama itself and on any models or tooling you install separately.
