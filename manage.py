from flask.cli import FlaskGroup
from app.app_factory import create_app
from app.core.extensions import db, migrate

app = create_app()
cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()

@app.cli.command("seed")
def seed():
    """Seed demo data into the database."""
    from seed import run_seed
    run_seed()
    print("Data inserted")