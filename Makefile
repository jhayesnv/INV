.PHONY: run
run:
	python manage.py runserver

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: superuser
superuser:
	python manage.py createsuperuser

.PHONY: update
update: migrations migrate ;
