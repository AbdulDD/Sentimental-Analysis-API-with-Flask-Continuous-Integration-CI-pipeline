# Install dependencies
install:
	pip install -r requirements.txt

# Run tests
test:
	pytest


# Run linter
lint:
	flake8 . --exclude=.venv


# Format code
format:
	black .

# Run everything
all: install lint format test
