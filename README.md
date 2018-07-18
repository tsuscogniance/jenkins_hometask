# Python UI automation hometask
## To run meest logistics tests you need:

* Have on your machine installed Python 3+.

* Install pip3:

```sudo apt-get install python3-pip```

* Clone the project to your machine

```git clone ssh://git@base.cogniance.com:2222/tsus/test_meest_logistics.git```

* Move to project folder

```cd test_meest_logistics/```

* Install virtualenv

```pip3 install virtualenv```

* Setup virtual environment

```virtualenv -p python3 hometask_selenium_env```
    
* Activate the virtualenv

```source hometask_selenium_env/bin/activate```
    
* Install requirements:

```pip install -r requirements.txt```

* Run tests:

```pytest -sv```