# celery_example
Example of structure for celery-app with periodic tasks

Launch commands:  
`$ pip install -r requirements.txt`  
`$ celery -A celery_tests.periodic_tasks beat`  
`$ celery -A celery_tests worker`
