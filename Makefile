ENV_DIR := $(shell pwd)/_env
PYTHON_BIN := $(shell which python)

.DEFAULT_GOAL = all

.PHONY: all
all: help

.PHONY: test
test: bin/python setup.py
	bin/python setup.py test

.PHONY: env
env: bin/python 

bin/python: bin/buildout buildout.cfg
	ARCHFLAGS="-arch i386 -arch x86_64" ./bin/buildout -N

bin/buildout: $(ENV_DIR)/bin/python bootstrap.py
	mkdir -p .downloads
	$(ENV_DIR)/bin/python bootstrap.py

bootstrap.py:
	curl -S -s -O http://python-distribute.org/bootstrap.py

$(ENV_DIR)/bin/python:
	virtualenv --no-site-packages --python=$(PYTHON_BIN) $(ENV_DIR)

.PHONY: clean
clean: envclean pyclean

.PHONY: pyclean
pyclean:
	find src -name \*.pyc -exec rm -f {} \;
	rm -rf src/*.egg-info dist

.PHONY: envclean
envclean:
	rm -rf bin eggs develop-eggs parts .installed.cfg bootstrap.py src/*.egg-info
	rm -rf distribute-*.tar.gz
	rm -rf $(ENV_DIR)
	
