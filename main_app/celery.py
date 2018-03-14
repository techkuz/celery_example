from celery import Celery
from config import config

app = Celery('celery',
             broker=config["celery"]["settings"]["broker_url"],
             backend=config["celery"]["settings"]["result_backend"],
             include=['example_app.tasks'])

if __name__ == '__main__':
    app.start()
