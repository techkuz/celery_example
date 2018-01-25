from celery import Celery

app = Celery('celery', broker='redis://localhost', backend='redis://localhost', include=['celery_tests.tasks'])


if __name__ == '__main__':
    app.start()
