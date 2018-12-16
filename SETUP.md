# Project Setup
Helpful commands and setup suggestions

## Download the repository
````
$ git clone git@github.com:LuminousLeopards/ChristmasLister.git
$ cd ChristmasLister
````


&nbsp;
## Python venv

### Check that Python3 is installed
Ensure that you have Python3. 
```
$ python --version
```
Should return something like:
```
Python 3.6.6
```
If using a standard linux distribution, you may have to use ```python3``` in place of ```python```. If this is the case, make the substitution in the below commands until the venv is built.


&nbsp;
### Build a local virtual environment
[Python Virtual Enviornment basics](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv)

The virtual environment (venv) allows clean tracking of Python dependencies within the project. venv builds virtual python, pip and library files for use by the project. Every time a new shell is created, you will need to activate the venv so that the system libraries and python are overridden by the venv libs and binaries.
````
$ cd ChristmasLister
$ python -m pip venv . 
````
This sets up the virtual environment within the ChristmasLister repository, but keeps the christmaslister source directory clean.

Now you should see the following added:
```
Include/
Lib/
pyenv.cfg
Scripts/
```

&nbsp;
### How to activate the virtual environment

When developing or testing, we should activate the virtual environment. This creates a clean, trackable shell around our project.

Open Git Bash (Windows)
```
$ cd ChristmasLister/
$ . Scripts/activate
```

If you're on Linux, your virtual environment directories will be a little bit different.
```
$ cd ChristmasLister/
$ . bin/activate
```

To check that you're using 


## Docker Build commands

## Visual Studio Code Plugins
```
Git History
Docker
MagicPython
Markdown All in One
```


