# REST API Learning
Profiles for rest api project

# Installation and setup

## Step 1: Install:
1. Git
2. VirtualBox
3. VSCode
4. Vagrant

`restart the computer`

## Step 2: Vagrant Virtual Environment

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

- **Create your django app and models**

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

