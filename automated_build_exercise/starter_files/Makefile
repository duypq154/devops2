install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
	pip install pytest
	pip3 install pytest

test:
	python3 -m pytest -vv test_hello.py
	
lint:
	pylint --disable=R,C hello.py

all: install lint test