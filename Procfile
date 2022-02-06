release: python manage.py migrate
web2: daphne app.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channel_layer
