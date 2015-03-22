BASEDIR=$(CURDIR)
VENV=$(BASEDIR)/venv

PY=$(VENV)/bin/python
PELICAN=$(VENV)/bin/pelican

INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py
PORT = 8000


html: $(PELICAN)
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE)

publish: $(PELICAN)
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF)

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                      (re)generate the web site            '
	@echo '   make publish                   generate using production settings   '
	@echo '   make run [PORT=8000]           serve site at http://localhost:8000  '
	@echo '   make clean                     remove the generated files           '
	@echo '                                                                       '

run: $(PELICAN)
	@echo 'Serving at http://localhost:$(PORT)/'
	scripts/serve.py --python=$(PY) --pelican=$(PELICAN) --input=$(INPUTDIR) --output=$(OUTPUTDIR) --settings=$(CONFFILE) --port=$(PORT)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

.PHONY: html help run clean

$(PY):
	virtualenv --python=python3 venv

$(VENV)/bin/pip: $(PY)

$(PELICAN): $(VENV)/bin/pip requirements.txt
	$(VENV)/bin/pip install -r requirements.txt
