VENV_NAME?=venv
PYTHON=${VENV_NAME}/bin/python
PIP=${VENV_NAME}/bin/pip

# Default target executed when no arguments are given to make.
default: setup

setup: ${VENV_NAME}/bin/activate

${VENV_NAME}/bin/activate: requirements.txt
	test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)
	${PIP} install -r requirements.txt
	touch ${VENV_NAME}/bin/activate

run: setup
	${PYTHON} -m app

clean:
	rm -rf $(VENV_NAME)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

.PHONY: default setup run clean
