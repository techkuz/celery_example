from celery.schedules import crontab

from tasks.celery import app
from tasks.tasks import test
from config import config

HELLO_TIMINGS = config["celery"]["periodic_tasks"]["hello"]
WORLD_TIMINGS = config["celery"]["periodic_tasks"]["world"]

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(**HELLO_TIMINGS),
        test.s('hello'), name=f'hello every {HELLO_TIMINGS}',)

    sender.add_periodic_task(
        WORLD_TIMINGS, test.s('world'), name=f'world every {WORLD_TIMINGS}',)

    sender.add_periodic_task(
        crontab(**config["celery"]["periodic_tasks"]["happy_mondays"]),
        test.s('Happy Mondays!'),)
