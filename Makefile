install:
	@docker-compose build
	@make up

up:
	@docker-compose up

stop:
	@docker-compose stop

down:
	@docker-compose down -v

db:
	@docker exec jangominishop_python_1 python manage.py makemigrations
	@docker exec jangominishop_python_1 python manage.py migrate

superuser:
	@docker exec -it jangominishop_python_1 python manage.py createsuperuser

python:
	@docker exec -it jangominishop_python_1 /bin/bash

bot:
	@docker exec -it jangominishop_python_1 python manage.py bot

