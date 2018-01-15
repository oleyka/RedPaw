venv:
	virtualenv -p python3 venv
	. venv/bin/activate && venv/bin/pip install -Ir requirements.txt
	. venv/bin/activate && venv/bin/pip install -Ir test-requirements.txt

freeze: venv requirements.in test-requirements.txt
	. venv/bin/activate && venv/bin/pip install pip-tools
	. venv/bin/activate && LANG=en_US.UTF-8 venv/bin/pip-compile requirements.in --output-file requirements.txt
	. venv/bin/activate && LANG=en_US.UTF-8 venv/bin/pip-compile test-requirements.in --output-file test-requirements.txt

run: venv
	python prepaw/manage.py runserver 192.168.42.42:8000

clean:
	rm -rf .tox
	rm -f coverage.xml .coverage
	rm -rf venv

.PHONY:
