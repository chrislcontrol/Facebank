.DEFAULT_GOAL := default_target

PROJECT_NAME := user-storage
PYTHON_VERSION := 3.9.0
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)
DATABASE_PASS := postgres


run-postgres:
	docker start $(PROJECT_NAME)-postgres 2>/dev/null || docker run --name $(PROJECT_NAME)-postgres -p 5432:5432 -e POSTGRES_PASSWORD='$(DATABASE_PASS)' -d postgres:10-alpine

.pip:
	pip install pip --upgrade

setup-dev: .pip
	pip uninstall -y typing
	pip install -U setuptools==59.6.0
	pip install -r requirements-dev.txt

.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .create-venv setup-dev


containers-up: run-postgres

run-app:
	python run.py

containers-down:
	docker stop $$(docker ps -aq)

containers-reset: containers-down containers-up

init-migrations:
	-cd src/application && env FLASK_APP=app.py flask db init && cd ..

create-migrations:
	cd src/application && env FLASK_APP=app.py flask db migrate && cd ..

run-migrations:
	cd src/application && env FLASK_APP=app.py flask db upgrade && cd ..

migrate: init-migrations create-migrations run-migrations
