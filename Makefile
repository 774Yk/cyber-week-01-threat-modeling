.PHONY: test lint security run

test:
	python -m unittest discover -s tests -v

lint:
	python -m compileall -q app tools tests
	python -m py_compile app/*.py tools/*.py tests/*.py

security:
	python tools/security_checks.py

run:
	python app/lab_server.py
