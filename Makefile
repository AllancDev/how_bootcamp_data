clean:
	rm -rf .venv day-summary *.checkpoint .pytest_cache .coverage

init: clean
	pip3 install poetry
	poetry install --no-root
test:
	poetry run python -m pytest

## CI/CD
ci-setup:
	pip3 install poetry
	poetry install --no-root

ci-test:
	poetry run python -m pytest

ci-deploy: 
	poetry run zappa update $(stage) || poetry run zappa deploy $(stage) 