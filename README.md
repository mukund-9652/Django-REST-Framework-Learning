# REST API Learning with Django

## Documentation:

* [About Django](#about-django)
* [Installation](#installation)
## About DJANGO:

Django is a high-level Python web framework that encourages rapid development
and clean, pragmatic design. Thanks for checking it out.

All documentation is in the "``docs``" directory and online at
https://docs.djangoproject.com/en/stable/. If you're just getting started,
here's how we recommend you read the docs:

* First, read ``docs/intro/install.txt`` for instructions on installing Django.

* Next, work through the tutorials in order (``docs/intro/tutorial01.txt``,
  ``docs/intro/tutorial02.txt``, etc.).

* If you want to set up an actual deployment server, read
  ``docs/howto/deployment/index.txt`` for instructions.

* You'll probably want to read through the topical guides (in ``docs/topics``)
  next; from there you can jump to the HOWTOs (in ``docs/howto``) for specific
  problems, and check out the reference (``docs/ref``) for gory details.

* See ``docs/README`` for instructions on building an HTML version of the docs.

Docs are updated rigorously. If you find any problems in the docs, or think
they should be clarified in any way, please take 30 seconds to fill out a
ticket here: https://code.djangoproject.com/newticket

To get more help:

* Join the ``#django`` channel on ``irc.libera.chat``. Lots of helpful people
  hang out there. See https://web.libera.chat if you're new to IRC.

* Join the django-users mailing list, or read the archives, at
  https://groups.google.com/group/django-users.

To contribute to Django:

* Check out https://docs.djangoproject.com/en/dev/internals/contributing/ for
  information about getting involved.

To run Django's test suite:

* Follow the instructions in the "Unit tests" section of
  ``docs/internals/contributing/writing-code/unit-tests.txt``, published online at
  https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/#running-the-unit-tests

Supporting the Development of Django
====================================

Django's development depends on your contributions. 

If you depend on Django, remember to support the Django Software Foundation: https://www.djangoproject.com/fundraising/

# Installation

1. Git : https://git-scm.com/downloads
2. VirtualBox : https://www.virtualbox.org/wiki/Downloads
3. VSCode : https://code.visualstudio.com/download
4. Vagrant : https://developer.hashicorp.com/vagrant/downloads

*restart the computer*

# Vagrant Virtual Environment Setup

1. Create a project folder (NewProject)

Run the following commands

```bash
> vagrant init ubuntu/bionic64
```

```bash
> vagrant up
```

[If vagrant shows ssh error then go to virtual box and shut down the new environment and again run the above command.]

```bash
> vagrant ssh
```

**Now the prompt will go to the vagrant terminal. It will be displayed like this:**

```bash
vagrant@ubuntu-bionic:~$ 

```

**Go the the vagrant workspace with cd command:**

```bash
$ cd /vagrant/
```

**Now run the following commands to update and install python virtual environment package**

```bash
$ sudo apt-get update
$ sudo apt install python-pip
$ sudo apt-get install python3-venv
'The command is used to create the virtual environment (env)'
$ python3 -m venv ~/env
```

**After installing and creating the virtual environment, activate the environment.**

```bash

$ source ~/env/bin/activate

```

This activates the virtual environment so that we can build, run, migrate and test the django and models.


**Our Installation and setup is complete!!**
**Now we go for Django Projects!!!**

# Django Projects

## 1. Initialization and Things to remember

- Always up the vagrant server first

```bash
> vagrant up
```

- Then access the vagrant terminal

```bash
> vagrant ssh
```

- Go the the vagrant workspace with cd command:

```bash
$ cd /vagrant/
```

- Then start the python virtual environment

```bash

$ source ~/env/bin/activate

```

## 2. Django Files

- Install the Django and DjangoRestFramework into the virtual environment

```bash
$ pip install django djangorestframework
```

- Create django project:
```bash
$ django-admin startproject newproject .
```

- Create django app:
```bash
$ python3 manage.py startapp pages 
```

- Create the migration for migrating the model to a database
```bash
$ python3 manage.py makemigrations
```

- Deploy the migrations to the database
```bash
$ python3 manage.py migrate
```

- Run the django app
```bash
$ python3 manage.py runserver 0.0.0.0:8000
```

