venv:
	virtualenv -p python3 venv
	. venv/bin/activate && venv/bin/pip install -Ir requirements.txt

freeze: venv requirements.in
	. venv/bin/activate && venv/bin/pip install pip-tools
	. venv/bin/activate && venv/bin/pip-compile requirements.in

run: venv
	python prepaw/manage.py runserver 192.168.42.42:8000

clean:
	rm -rf .tox
	rm -f coverage.xml .coverage
	rm -rf venv

.PHONY:
