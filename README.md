###Install dependencies
```
mkdir virtualenv
virtualenv raspberrypi_gpio-flask
pip install -r requirements.txt
```
### Setup virtual env
```
source ./virtualenv/raspberrypi_gpio-flask/bin/activate
```
### Setup virtual env
```
export FLASK_APP=serve.py ; flask run
```
