web: gunicorn codeblog.wsgi --log-file -
python manage.py collectstatic --noinput
manage.py migrate