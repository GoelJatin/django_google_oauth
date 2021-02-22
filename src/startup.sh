cd oauth/

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input --clear

gunicorn oauth.wsgi:application --bind 0.0.0.0:8000 -w 4 --log-file -
