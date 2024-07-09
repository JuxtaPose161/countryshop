FROM python:3.7

WORKDIR /app
COPY . /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFERED 1

RUN pip install -r requirements.txt
CMD python manage.py migrate \
    && python -Xutf8 manage.py loaddata db.json \
    && python manage.py collectstatic --no-input \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@mail.com', 'admin')" \
    && gunicorn countryshop.wsgi:application --bind 0.0.0.0:8000