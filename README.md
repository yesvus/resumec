# About

**resumec** is a production-grade, deterministic CV compiler built in Python. It is not a chatbot. 

The goal of this project is to build a predictable, repeatable pipeline that converts `(raw_cv.md + job_post_url + github repos)` into a tailored, perfectly-formatted markdown CV based on strict schemas and validation rules.

## Architecture Principles
* Every stage is a pure function.
* No LLM generates markdown directly; LLMs output structured JSON only.
* Templates render markdown deterministically via Jinja2.
* Matching and selection logic is standard code (using TF-IDF / fuzzy matching), not AI.
* Designed to be easily wrapped by a CLI today and a FastAPI web UI tomorrow.

## Project Structure

```text
resumec/
├─ pyproject.toml
├─ README.md
├─ .env
├─ resumec/
│  ├─ __init__.py
│  ├─ cli.py
│  ├─ config.py
│  │
│  ├─ pipeline/
│  │   ├─ orchestrator.py
│  │   │
│  │   ├─ ingest/
│  │   │   ├─ job_fetcher.py
│  │   │   ├─ repo_crawler.py
│  │   │   └─ rawcv_loader.py
│  │   │
│  │   ├─ normalize/
│  │   │   ├─ person_parser.py
│  │   │   ├─ job_parser.py
│  │   │   └─ repo_parser.py
│  │   │
│  │   ├─ enrich/
│  │   │   ├─ extract_keywords.py
│  │   │   └─ classify_project.py
│  │   │
│  │   ├─ match/
│  │   │   ├─ scorer.py
│  │   │   └─ selector.py
│  │   │
│  │   ├─ generate/
│  │   │   ├─ llm_client.py
│  │   │   ├─ prompts.py
│  │   │   └─ rewrite_cv.py
│  │   │
│  │   ├─ validate/
│  │   │   ├─ rules.py
│  │   │   └─ repair.py
│  │   │
│  │   ├─ render/
│  │   │   └─ markdown_renderer.py
│  │   │
│  │   └─ persist/
│  │       └─ save_cv.py
│  │
│  ├─ schemas/
│  │   ├─ person.py
│  │   ├─ job.py
│  │   ├─ repo.py
│  │   └─ cv.py
│  │
│  ├─ templates/
│  │   └─ swe.md.jinja
│  │
│  └─ utils/
│      ├─ logging.py
│      └─ retry.py
│
├─ data/
│  └─ raw_cv.md
│
├─ cvs/
│
└─ tests/
```

## Usage

You can run the determinist CV compiler using the `uv` package manager. 

```bash
uv run python -m resumec.cli compile <job_url>
```

**Example:**
```bash
uv run python -m resumec.cli compile "https://example.com/job/senior-python"
```

The script will:
1. Load `data/raw_cv.md`
2. Fetch the target job posting
3. Compile, score, and evaluate your experience against the job keywords
4. Rewrite your CV deterministically


## License

This project is licensed under the [MIT License](LICENSE).