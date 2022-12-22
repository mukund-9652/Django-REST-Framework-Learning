# REST API Learning
Profiles for rest api project

## Step 1: Install:
1. Git
2. VirtualBox
3. VSCode
4. Vagrant

`restart the computer`

## Step 2: Vagrant Virtual Environment

1. Create a project folder (NewProject)

Run the following commands

`
vagrant init ubuntu/bionic64
`

`
vagrant up
`

[If vagrant shows ssh error then go to virtual box and shut down the new environment.]

`vagrant ssh`

**Now the prompt will go to the vagrant terminal. It will be displayed like this:**

` vagrant@ubuntu-bionic:/vagrant$ `

**Now run the following commands to update and install python virtual environment package**

```
$ sudo apt-get update
$ sudo apt install python-pip
$ sudo apt-get install python3-venv
'The command is used to create the virtual environment (env)'
$ python3 -m venv ~/env
```

**After installing and creating the virtual environment, activate the environment.**
`$ source ~/env/bin/activate`

This activates the virtual environment so that we can build, run, migrate and test the django and models.




