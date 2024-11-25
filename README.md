# How to create a BEEP project in your computer.

## STEP 1 - Setting up Python and project folder

#### 1. Create a folder with a relevant file name (ie. BEEP_Project) and download/install all files of this repository.

#### 2. Install [Python 3.8](https://www.python.org/downloads/release/python-3810/ "Python 3.8") in project folder (./py308 or ../py308 etc.) or any folder you want.

## STEP 2 - Setting up local pip environment

#### 1. To install pipenv, in your terminal, type: `pip install pipenv`

#### 2. If you want the environment files in your local project folder: (optional)

##### I) In Powershell terminal:

Type: `$env:PIPENV_VENV_IN_PROJECT="true"`

##### II) Or, In CMD terminal:

Type: `set PIPENV_VENV_IN_PROJECT=true`

#### 3. In terminal type: `pipenv --python <../path/to/python/3.8/>`

###### Use the installed path of Python 3.8 while running this command. This will create a new pip environment folder in you computer using the python 3.8 as your main interpretter.

#### 4. Enter in the environment by typing: `pipenv shell`

## STEP 3 - Installing recomended libraries:

### 1. While you are inside your pipenv, type: `pip install -r ./requirements.txt`

This will install all the libraries needed for the project.

###### Note: you must have requirements.txt file in order to install exact versions otherwise the project will not run.

### 2. To install individually by focusing on one core librabrary, type: `pipenv install <pybamm/beep>`

This works better on separate virtual enviroment with separate python versions for each core library.

### 3. To check for any problems, type: `pipenv check`

# ALL DONE? HAVE FUN.
