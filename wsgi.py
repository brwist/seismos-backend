#!/user/bin/env python
from werkzeug.security import generate_password_hash
from app import create_app, db, models
from app.models import Well
from worker_db_backup import make_db_restor

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


@app.cli.command("db_restore")
def db_restore():
    make_db_restor.delay(0)
    print("async code started")


@app.shell_context_processor
def get_context():
    TABLES = [
        "Project", "Client", "CustomerFieldRep",
        "Pad", "Equipment", "Well",
        "FieldNotes", "JobInfo", "JobType",
        "Crew", "ProjectCrew", "NFProcessingResult",
        "Stage", "StageAVG", "FFProcessingResult",
        "DefaultVal", "DefaultAdvanceVal", "DefaultParamVal",
        "LocationInfo", "CountyName", "BasinName",
        "State", "ChemFluids",
        "Perforation", "Proppant",
    ]

    def clear_table(modelname):
        try:
            model = getattr(models, modelname)
        except AttributeError:
            print(f"No model: {modelname}")
            return None

        for item in model.query.all():
            item.delete()

        print(f"Model: {modelname} cleared")
        return True

    def model_list(modelname):
        try:
            model = getattr(models, modelname)
        except AttributeError:
            print(f"No model: {modelname}")
            return None

        return model.query.all()

    def insert_test_data(well_id):
        well = Well.query.filter(Well.id == well_id).first()
        if not well:
            print(f"No well with id {well_id}")
            return

        print("Inserting test data")

    def log():
        for model in TABLES:
            print(model_list(model))

    def clear_all_data():
        for model in TABLES:
            clear_table(model)

    def create_user():
        username, password, email = "bobo", "1234", "bobo@gmail.com"
        user = models.User(username=username, password=generate_password_hash(password), email=email)
        user.save()
        print(f"User created: {username} {password} {email}")

    return dict(
        app=app,
        db=db,
        m=models,
        clear_table=clear_table,
        model_list=model_list,
        log=log,
        clear_all_data=clear_all_data,
        create_user=create_user,
        insert_test_data=insert_test_data
    )


if __name__ == "__main__":
    app.run()
