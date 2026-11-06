from pathlib import Path

folders = [
    "src/atlas_enterprise_ai/templates",
    "src/atlas_enterprise_ai/static/css",
    "src/atlas_enterprise_ai/static/js",
    "worker",
    "infra",
    "scripts",
    "docs",
]

# Project files
files = [
    # Root files
    ".env",
    ".env.example",

    # Backend
    "src/atlas_enterprise_ai/config.py",
    "src/atlas_enterprise_ai/db.py",
    "src/atlas_enterprise_ai/aws.py",
    "src/atlas_enterprise_ai/vector.py",
    "src/atlas_enterprise_ai/rag.py",
    "src/atlas_enterprise_ai/memory.py",
    "src/atlas_enterprise_ai/guardrails.py",
    "src/atlas_enterprise_ai/graph.py",
    "src/atlas_enterprise_ai/observability.py",

    # Frontend
    "src/atlas_enterprise_ai/templates/index.html",
    "src/atlas_enterprise_ai/static/css/styles.css",
    "src/atlas_enterprise_ai/static/js/app.js",

    # Document ingestion
    "worker/__init__.py",
    "worker/ingest.py",

    # Database
    "infra/schema.sql",
    "scripts/init_db.py",

    # Documentation
    "docs/SETUP.md",
]

def create_structure():

    for folder in folders:
        Path(folder).mkdir(parents=True, exist_ok=True)

    for file in files:
        path = Path(file)

        path.parent.mkdir(parents=True, exist_ok=True)

        path.touch(exist_ok=True)


if __name__ == "__main__":
    create_structure()