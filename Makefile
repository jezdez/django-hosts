VENV = /tmp/django-hosts-env
export PATH := $(VENV)/bin:$(PATH)

test:
	pytest

clean:
	make -C docs clean
	rm -rf $(VENV)

docs:
	virtualenv $(VENV)
	pip install -r docs/requirements.txt
	pip install -e .
	make -C docs html

.PHONY: test docs clean
