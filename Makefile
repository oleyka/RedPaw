ACTIVATE = . venv/bin/activate &&

venv:
	virtualenv -p python3 venv
	$(ACTIVATE) venv/bin/pip install -IUr requirements.txt
	$(ACTIVATE) venv/bin/pip install -IUr test-requirements.txt

freeze: venv requirements.in test-requirements.txt
	$(ACTIVATE) venv/bin/pip install pip-tools
	$(ACTIVATE) LANG=en_US.UTF-8 venv/bin/pip-compile requirements.in --output-file requirements.txt
	$(ACTIVATE) LANG=en_US.UTF-8 venv/bin/pip-compile test-requirements.in --output-file test-requirements.txt

run: venv
	$(ACTIVATE) python prepaw/manage.py runserver 192.168.42.42:8000

test: venv
	$(ACTIVATE) tox

clean:
	rm -rf .tox
	rm -f coverage.xml .coverage
	rm -rf venv

.PHONY:
