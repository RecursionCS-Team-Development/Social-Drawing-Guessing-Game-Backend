web: gunicorn app.wsgi --log-file -
web2: daphne chat.routing:application --port $PORT --bind 0.0.0.0 -v2
web3: daphne app.asgi:application --port $PORT --bind 0.0.0.0 -v2

worker: python manage.py runworker channel_layer -v2
worker2: python manage.py runworker channels --settings=settings -v2
worker3: python manage.py runworker channels --settings=app.settings -v2