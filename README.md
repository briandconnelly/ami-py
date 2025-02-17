# ami

![Decvelopment Status](https://img.shields.io/badge/dev%20status-beta-orange)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ami)
![PyPI - License](https://img.shields.io/pypi/l/ami)
![PyPI - Version](https://img.shields.io/pypi/v/ami)
[![Codecov test
coverage](https://codecov.io/gh/briandconnelly/ami-py/branch/main/graph/badge.svg)](https://app.codecov.io/gh/briandconnelly/ami-py?branch=main)

`ami` (Am I...?) is a Python package that provides simple functions to detect various runtime environments and configurations.


## Examples

```py
import ami

# Am I using Linux?
ami.using_linux()


# On an ARM CPU?
ami.using_arm_cpu()


# Am I running a virtual environment?
ami.using_virtualenv()


# Am I running in a container?
ami.using_container()


# Am I connected to the internet?
ami.online()


# Am I on battery power?
ami.using_battery_power()
```


## Installation

Install the latest stable version of ami from PyPI:

```sh
pip install ami
```

If you'd like to add ami to a project managed with uv:

```sh
uv add ami
```


## Requirements

- Python 3.11 or higher


## License

This project is licensed under the MIT License - see the LICENSE file for details.
