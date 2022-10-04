release: python manage.py migrate --no-input
web: gunicorn eemis.wsgi 
worker: celery -A eemis worker -l INFO