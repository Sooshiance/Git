# Define the virtual environment directory
VENV_DIR = .venv

# Define the Python interpreter from the virtual environment
PYTHON = $(VENV_DIR)/bin/python

# Define the Django management command
DJANGO_MANAGE = $(PYTHON) backend/manage.py

# Default target
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make runserver      - Run the Django development server"
	@echo "  make makemigrations - Create new migrations based on changes to models"
	@echo "  make migrate        - Apply migrations to the database"
	@echo "  make test           - Run tests"
	@echo "  make createsuperuser - Create a superuser for the admin site"

.PHONY: run
run:
	$(DJANGO_MANAGE) runserver

.PHONY: makemigrations
migrations:
	$(DJANGO_MANAGE) makemigrations

.PHONY: migrate
migrate:
	$(DJANGO_MANAGE) migrate

.PHONY: test
test:
	$(DJANGO_MANAGE) test

.PHONY: createsuperuser
superuser:
	$(DJANGO_MANAGE) createsuperuser
