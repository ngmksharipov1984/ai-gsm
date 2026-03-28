# FastAPI + PostgreSQL Cards Viewer

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

Open: <http://127.0.0.1:8000/>

The application uses SQLAlchemy ORM and reads data from:

`postgresql://postgres:password@192.168.88.59:5443/AzsOnline_RELEASE`
