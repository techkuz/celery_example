from celery.schedules import crontab

from main_app.celery import app
from example_app.tasks import test_task
from config import config

HELLO_TIMINGS = config["celery"]["periodic_tasks"]["hello"]
WORLD_TIMINGS = config["celery"]["periodic_tasks"]["world"]

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    #  prints hello periodically
    sender.add_periodic_task(crontab(**HELLO_TIMINGS),
                             test_task.s('hello'),
                             name=f'prints hello every {HELLO_TIMINGS}',)
    #  prints world periodically
    sender.add_periodic_task(WORLD_TIMINGS["seconds"],
                             test_task.s('world'),
                             name=f'prints world every {WORLD_TIMINGS}')

    #  prints Happy mondays periodically
    sender.add_periodic_task(crontab(**config["celery"]["periodic_tasks"]["happy_mondays"]),
                             test_task.s('Happy Mondays!'),)
