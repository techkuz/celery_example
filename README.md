# celery_example
Example of structure for celery-app with periodic tasks

Launch commands:  
`$ pip install -r requirements.txt`  
`$ celery -A main_app.periodic_tasks beat`  
`$ celery -A main_app worker`

Python 3.6