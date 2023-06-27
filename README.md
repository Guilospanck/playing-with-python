# playing-with-python

## Installing Python 3.11

You can use [asdf](https://asdf-vm.com/guide/getting-started.html) to do that. Once you have it installed, run at the root of this package:

```sh
asdf install
```

This will install python with the versions defined in the [.tool-versions](.tool-versions) file, namely `python 3.11.1 2.7.18`.

## Creating virtual environment with `venv`

It is necessary if you wanna separate your local project packages from your global python projects.

Run:

```sh
python -m venv .venv
```

This will create a `.venv` folder that will hold all the packages that you install from now on. But first, you have to activate it:

```sh
source .venv/bin/activate
```

Now you're good to go and your global packages will not be polluted.

## Create [requirements.txt](requirements.txt)

Run:

```sh
pip freeze > requirements.txt
```

And to install the requirements:

```sh
pip install -r requirements.txt
```

## Installing packages

It's good to update `pip` - the python package installer - before installing any packages:

```sh
pip install --upgrade pip
```

Now you can install packages:

```sh
python -m pip install <package-name>
```

## Run application

```sh
python hello_world/app.py
```