web: daphne --pythonpath ./app app.asgi:application  --port $PORT --bind 0.0.0.0 -v2
worker: cd app && python manage.py runworker channel_layer -v2