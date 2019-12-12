test:
	pytest tests

fmt:
	isort -sl -y
	black -l 80 jsonbourne.py
	black -l 80 tests

