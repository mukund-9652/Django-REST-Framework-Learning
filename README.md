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
vagrant init ubuntu/bionic64
```

```bash
vagrant up
```

[If vagrant shows ssh error then go to virtual box and shut down the new environment.]

```bash
vagrant ssh
```

**Now the prompt will go to the vagrant terminal. It will be displayed like this:**

```bash
vagrant@ubuntu-bionic:/vagrant$ 

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

## Initialization




