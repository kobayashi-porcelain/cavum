# Makefile for Cavum Project

.PHONY: help init init-dev install install-dev test lint clean

PYTHON = python3
PIP = pip
VENV_DIR = venv

help:
	@echo "Available commands:"
	@echo "  make init         - Create virtual environment"
	@echo "  make install      - Install end-user dependencies"
	@echo "  make install-dev  - Install development dependencies"
	@echo "  make test         - Run test suite"
	@echo "  make lint         - Run code linting"
	@echo "  make clean        - Remove virtual environment and __pycache__"

init:
	$(PYTHON) -m venv $(VENV_DIR)

install:
	. $(VENV_DIR)/bin/activate && $(PIP) install -r requirements-use.txt

install-dev:
	. $(VENV_DIR)/bin/activate && $(PIP) install -r requirements-dev.txt

test:
	. $(VENV_DIR)/bin/activate && pytest tests/

lint:
	. $(VENV_DIR)/bin/activate && pylint cavum

clean:
	rm -rf $(VENV_DIR) __pycache__ **/__pycache__ .pytest_cache

