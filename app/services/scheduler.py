from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

from flask import current_app
from app import db
from app.models.models import URL   


def start_scheduler(app):
    scheduler = BackgroundScheduler()

    def job():
        with app.app_context():
            now = datetime.utcnow()
            URL.query.filter(URL.expired_at < now).delete()
            print(f"Deleted expired URLs at {now}")
            db.session.commit()
            print("Scheduler job executed successfully")
    scheduler.add_job(job, trigger="interval", seconds=60)
    scheduler.start()