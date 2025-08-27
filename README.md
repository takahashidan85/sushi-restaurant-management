# Sushi Restaurant Management (Student Project)

Clean-architecture flavored Flask app for managing a sushi restaurant.
- No Docker included in this version.
- SQLite by default for local development and tests (in-memory for tests).
- App factory, domain, infrastructure, application (services), and presentation (routes).

Run locally:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=wsgi.py
export FLASK_ENV=development
flask run --port 8000
```

Run tests:
```bash
pip install -r requirements.txt
pytest -q
```
