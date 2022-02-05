web: daphne --pythonpath ./app app.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
chatworker: --pythonpath ./app python manage.py runworker --settings=app.settings -v2