venv:
	virtualenv -p python3 venv
	. venv/bin/activate && pip install -Ir requirements.txt

freeze: venv requirements.in
	. venv/bin/activate && pip install pip-tools
	. venv/bin/activate && pip-compile requirements.in

clean:
	rm -rf .tox
	rm -f coverage.xml .coverage
	rm -rf venv

.PHONY:
