web: gunicorn --pythonpath ./app app.wsgi --log-file -
web2: daphne --root-path=/app chat.routing:application --port $PORT --bind 0.0.0.0 -v2


web3: daphne app.chat.routing:application --port $PORT --bind 0.0.0.0 -v2
web4: daphne app.app.asgi:application --port $PORT --bind 0.0.0.0 -v2
web5: daphne app.asgi:application --port $PORT --bind 0.0.0.0 -v2

web6: daphne --root-path=/app app.asgi:application --port $PORT --bind 0.0.0.0 -v2
web7: daphne --pythonpath ./app app.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker3: cd app && python manage.py runworker channels --settings=app.settings -v2

worker: cd app && python manage.py runworker channel_layer -v2
worker2: cd app && python manage.py runworker channels --settings=settings -v2
worker4: cd app && python manage.py runworker channels --settings=app.app.settings -v2