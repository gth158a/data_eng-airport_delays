### Commands for flask

Code was adapted from:
https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80

```
$ virtualenv flask-aws
$ source flask-aws/bin/activate
```
To install the required modules:
```
$ pip install -r requirements.txt
```
Edit ```config.py``` by commenting out the AWS URL and uncomment this line:
```
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
```
Next run:
```
$ python db_create.py
```
And the tables are created.  Now you can launch the app:
```
$ python application.py
```
And point your browser to http://0.0.0.0:5000
