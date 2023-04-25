web: gunicorn myshop.wsgi --log-file -
worker: env QUEUE=* bundle exec rake resque:work