import os
from celery import Celery
from dotenv import load_dotenv
from app.controllers import backup_base_controller

load_dotenv()

app = Celery("Worker", broker=os.environ.get("REDIS_URL", ""))


BACKUP_SECONDS_DELAY = 5


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(BACKUP_SECONDS_DELAY, make_backup.s())


@app.task
def make_backup():
    backup_base_controller.backup()


@app.task
def make_db_restor(last_backup=0):
    backup_base_controller.restore(last_backup)
