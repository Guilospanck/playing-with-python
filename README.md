# playing-with-python

## Installing Python 3.11

You can use [asdf](https://asdf-vm.com/guide/getting-started.html) to do that. Once you have it installed, run at the root of this package:

```sh
asdf install
```

This will install python with the versions defined in the [.tool-versions](.tool-versions) file, namely `python 3.11.1 2.7.18`. By doing that, `asdf` will substitute the function of something like `virtualenv` as the versions of these tools are only used in this directory and any subdirectories.

## Create [requirements.txt](requirements.txt)

Run:

```sh
pip freeze > requirements.txt
```

And to install the requirements:

```sh
pip install -r requirements.txt
```
