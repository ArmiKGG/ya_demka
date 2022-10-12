run:
	python3 ./main.py
.PHONY: run

lint:
	python3 -m flake8 .
.PHONY: lint

install:
	pip3 install -r requirements.txt
.PHONY: install