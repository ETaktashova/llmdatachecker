include .env
export

run:
	python3 -m src.main

lint:
	python3 -m mypy /.

deps:
	pip install -r requirements.txt

build:
	docker build -t llmchecker .