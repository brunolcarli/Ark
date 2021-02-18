run:
	python main.py

install:
	pip install -r ark/requirements/development.txt

replit:
	make install -r ark/requirements/replit.txt
	make run
