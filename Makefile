start:
	python manage.py runserver 8001

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createuser:
	python manage.py createsuperuser
	