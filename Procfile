web: gunicorn --pythonpath ./app app.wsgi --log-file -
web2: daphne -root-path=/app chat.routing:application --port $PORT --bind 0.0.0.0 -v2
worker: cd app && python manage.py runworker channel_layer -v2
worker2: cd app && python manage.py runworker channels --settings=app.settings -v2