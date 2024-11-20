venv:
	python3 -m venv venv
activate:
	source venv/bin/activate
install:
	pip install -r requirements.txt
lint:
	pylint --disable=R,C hello
test:
	pytest test_hello.py