# CodeInsight AI

An AI-assisted Python code review dashboard built with **Python** and **Streamlit**.

## Features

- Paste Python code into a web interface
- Run automated code-quality checks
- Identify basic security, reliability, readability, and maintainability issues
- Display review findings in a clean dashboard
- Easy to extend with an LLM such as Ollama or an API-based model

## Tech Stack

- Python
- Streamlit
- Regular Expressions
- Git & GitHub

## Run Locally

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
streamlit run app.py
```

The app will open in your browser.

## Future Improvements

- Connect an LLM for natural-language code explanations
- Add support for JavaScript, SQL, and Java
- Add downloadable review reports
- Add code-quality scoring
- Add RAG-based coding guidelines

## Author

Ankitha Reddy
