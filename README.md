# RedPaw

[![Build Status](https://travis-ci.org/oleyka/RedPaw.svg?branch=detour%2Fdjango-practice)](https://travis-ci.org/oleyka/RedPaw)
[![License](https://img.shields.io/badge/license-BSD-blue.svg)](https://github.com/oleyka/RedPaw)

Deploy locally
--------------
```
source ./redpaw.env && python prepaw/manage.py runserver
```

Deploy to Heroku
----------------
To deploy a new instance:
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?env[DJANGO_SETTINGS_MODULE]=prepaw.heroku-settings)

Heroku-specific settings are retrieved using the ```DJANGO_SETTINGS_MODULE``` variable in Heroku UI.

TODO:

1. Playbook for automated Heroku deployments.
2. Playbooks for in-house deployments.
3. For linting, add to cm/: pip install pylint, pylint-django and pep8
4. Test dataset and tests.
