web: gunicorn --pythonpath ./app app.wsgi --log-file -
worker: python manage.py runworker channels --settings=.settings -v2