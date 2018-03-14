from main_app.celery import app

@app.task
def test_task(arg):
    """
    Prints input arg
    """
    print(arg)

