[![flake8](https://github.com/LoGosX/wslpath-python/actions/workflows/flake8.yml/badge.svg)](https://github.com/LoGosX/wslpath-python/actions/workflows/flake8.yml) [![mypy](https://github.com/LoGosX/wslpath-python/actions/workflows/mypy.yml/badge.svg)](https://github.com/LoGosX/wslpath-python/actions/workflows/mypy.yml)
# wslpath-python

This is a simple Python wrapper around `wslpath` command found in *Windows Subsystem for Linux* (WSL) environment.

This package contains a single function `wslpath` that calls the `wslpath` command with appropriate arguments.

## Requirements
Tha package has no additional requirements. Developed and tested in Python 3.9, but it should work in Python 3.5 and above.



## Installation
This package can be installed using pip
```bash
pip install wslpath-python
```


## Example usage
```python
>>> from wslpath import wslpath
>>>
>>> wslpath(r'C:\Users\macie\PycharmProjects\wslpath-python')
'/mnt/c/Users/macie/PycharmProjects/wslpath-python'
>>>
>>> from pathlib import Path
>>> wslpath(Path(r'C:\Users\macie\PycharmProjects\wslpath-python'))
PosixPath('/mnt/c/Users/macie/PycharmProjects/wslpath-python')
>>>
>>> wslpath('.')
'.'
>>> wslpath('.', force_absolute_path=True)
'/mnt/c/Users/macie/PycharmProjects/wslpath-python/'
```
