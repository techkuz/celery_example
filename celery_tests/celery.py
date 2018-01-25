from celery import Celery
from celery.schedules import crontab

app = Celery('celery', broker='redis://localhost', backend='redis://localhost', include=['celery_tests.tasks'])



if __name__ == '__main__':
    app.start()


