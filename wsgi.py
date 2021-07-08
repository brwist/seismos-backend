#!/user/bin/env python

from app import create_app, db, models

app = create_app()


@app.cli.command("db_create")
def db_create():
    import os
    from sqlalchemy_utils import database_exists, create_database
    from sqlalchemy import create_engine

    url = os.environ.get('DEVEL_DATABASE_URL')
    db_engine = create_engine(url, echo=True)
    if not database_exists(db_engine.url):
        create_database(db_engine.url, encoding="utf8mb4")

    db.create_all()


@app.shell_context_processor
def get_context():
    return dict(app=app, db=db, m=models)


if __name__ == "__main__":
    app.run()
