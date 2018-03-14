from .celery import app

@app.task
def test(arg):
    """
    Prints input arg
    """
    print(arg)

