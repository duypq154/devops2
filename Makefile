setup:
	python3 -m venv ~/.devops2
	#source ~/.devops2/bin/activate

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	#pip install pytest
	#pip3 install pytest
	#pip install click
	#pip3 install click
	#pip install pylint
	#pip3 install pylint
	
test:
	python3 -m pytest -vv test_hello.py
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb

lint:
	pylint --disable=R,C hello.py
	#pylint --disable=R,C,W1203 app.py
	#test github action

all: install lint test