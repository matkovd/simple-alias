## Simple alias

Oversimplified tool to create bash / zsh / *sh aliases straight from command line. 

#### Usage:
**Installation:**
```shell script
git clone https://github.com/matkovd/simple-alias.git
cd simple-alias
pip3 install -e .
```
**Example:**
```shell script
create_alias dev 'export SOME_DEV_VARS=some_value;export http_proxy='
bash #or zsh, just to reload your session aliases
dev # now you can use new alias
```
**CLI**
```
Usage: create_alias [OPTIONS] ALIAS COMMAND

Options:
  --help  Show this message and exit.
```

