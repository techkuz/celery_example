from celery import Celery
from config import config


app = Celery('celery', **config["celery"]["settings"], include=['celery_tests.tasks'])


if __name__ == '__main__':
    app.start()
