
# RestApiMongoDBFlask

This is the first project to integrate Mongo DB with Flask
 
### Login system :busts_in_silhouette:

In this project is being implemented a basic login system.

| Models | Methods|Attributes|
|--|--|-|
| User | ``start_session`` ||
| | ``signup`` ||
| | ``signout`` ||
| | ``login`` ||


 - start_session 

> Start session variables logged_in and user and return code 200 if success
 - signup

> Adds a new user if succes
 - signout

> Implements signout by claring session and redirect to the form
 - login

> Implements login into the system and redirect to dashboard

**Encryption** :key:
For encrypt the password is being use pbkdf2_sha256 from passlib.hash
| Encrypt | Decrypt   |
|--|--|
|pbkdf2_sha256.hash("password")| pbkdf2_sha256.verify("password", hash) |

## Creating the virtual env

### How to connect create a Python Virtual Environment

> _It is often useful to have one or more Python environments where you can experiment with different combinations of packages without affecting your main installation. Python supports this through virtual environments. The virtual environment is a copy of an existing version of Python with the option to inherit existing packages. A virtual environment is also useful when you need to work on a shared system and do not have permission to install packages as you will be able to install them in the virtual environment._
[Reference here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)
## Outline

-   Open a terminal
-   Setup the pip package manager
-   Install the virtualenv package
-   Create the virtual environment
-   Activate the virtual environment
-   Deactivate the virtual environment

#### Open a terminal

The method you use to open a terminal depends on your operating system.

#### Setup the pip package manager

Check to see if your Python installation has pip. Enter the following in your terminal:

```bash
pip -h
```

If you see the help text for pip then you have pip installed, otherwise  [download and install pip](https://pip.pypa.io/en/latest/installing.html)

#### Install the virtualenv package

The virtualenv package is required to create virtual environments. You can install it with pip:

```bash
pip install virtualenv

## Create the virtual environment

To create a virtual environment, you must specify a path. For example to create one in the local directory called ‘mypython’, type the following:

```bash
virtualenv mypython
```

#### Activate the virtual environment

You can activate the python environment by running the following command:

### Mac OS / Linux

```bash
source mypython/bin/activate
```

### Windows

```bash
mypthon\Scripts\activate
```

You should see the name of your virtual environment in brackets on your terminal line e.g. (mypython).

Any python commands you use will now work with your virtual environment

#### Deactivate the virtual environment

To decativate the virtual environment and use your original Python environment, simply type ‘deactivate’.

```bash
deactivate
``````

## To run the script

It is necessary to run the virtualenv to use the specific modules of the project
```shell
Package       Version
------------- -------
autopep8      1.6.0
bcrypt        3.2.0
cffi          1.15.0
click         8.0.3
cryptography  35.0.0
Flask         2.0.2
Flask-PyMongo 2.3.0
itsdangerous  2.0.1
Jinja2        3.0.3
MarkupSafe    2.0.1
passlib       1.7.4
pip           21.3.1
pycodestyle   2.8.0
pycparser     2.21
pymongo       3.12.1
setuptools    58.2.0
six           1.16.0
toml          0.10.2
Werkzeug      2.0.2
wheel         0.37.0
```

```sh
fox@eva:~/RestApiMongoDBFlask$ source ./venv/bin/activate
(venv) fox@eva:~/RestApiMongoDBFlask$ 
```

### Mandatory to have running MongoDB

```bash
(venv) fox@eva:~/RestApiMongoDBFlask$ mongosh
Current Mongosh Log ID: 6191913c8dac019665b67627
Connecting to:          mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000
Using MongoDB:          5.0.3
Using Mongosh:          1.1.2

For mongosh info see: https://docs.mongodb.com/mongodb-shell/

------
   The server generated these startup warnings when booting:
   2021-11-14T19:06:11.467+00:00: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem
   2021-11-14T19:06:12.252+00:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
   2021-11-14T19:06:12.252+00:00: Soft rlimits for open file descriptors too low
------

Warning: Found ~/.mongorc.js, but not ~/.mongoshrc.js. ~/.mongorc.js will not be loaded.
  You may want to copy or rename ~/.mongorc.js to ~/.mongoshrc.js.
test> show databases;
admin               41 kB
config            73.7 kB
local               41 kB
user_login_sytem  73.7 kB
test> 
```

### Executing the bashscript to run or directly running the app

```bash
(venv) fox@eva:~/RestApiMongoDBFlask$ ./run 
 * Serving Flask app 'app.py' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 674-160-922
```
```bash
(venv) fox@eva:~/RestApiMongoDBFlask$ ./app.py
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5001/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 134-687-007
```
