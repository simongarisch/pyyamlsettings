[![Build Status](https://dev.azure.com/gatman946/simongarisch/_apis/build/status/simongarisch.pyyamlsettings?branchName=master)](https://dev.azure.com/gatman946/simongarisch/_build/latest?definitionId=1&branchName=master)
[![Build Status](https://travis-ci.org/simongarisch/pyyamlsettings.svg?branch=master)](https://travis-ci.org/simongarisch/pyyamlsettings)
<a href="https://github.com/python/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
[![Coverage Status](https://coveralls.io/repos/github/simongarisch/pyyamlsettings/badge.svg?branch=master)](https://coveralls.io/github/simongarisch/pyyamlsettings?branch=master)
[![PyPI version](https://badge.fury.io/py/pyyamlsettings.svg)](https://badge.fury.io/py/pyyamlsettings)

# pyyamlsettings

A Flyweight pattern for loading yaml files in Python.

## Installation
pyyamlsettings is python 2 and 3 compatible.
```bash
pip install pyyamlsettings
```

## Overview
There is a YamlSettings class exposed by the package that allows you to load and query yaml files.
Suppose we have a yaml file with the structure:
```
att1: 42
att2: "This is a string"

level1:
    a: 1
    b: 2
    level2:
        a: 3
        b: 4
```

We can load this file:
```python
import os
import pyyamlsettings

yaml_file_path = os.path.join("tests", "test_yaml_file.yaml")
settings = pyyamlsettings.YamlSettings(yaml_file_path)
```

And read particular items with:
```python
result = settings.get("att1")
print(result) # 42

result = settings.get("level1", "level2", "b")
print(result) # 4
```

## Notes
Due to a [deprecation message](https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation) yaml.load was modified slightly.
```python
yaml.load(input, Loader=yaml.FullLoader)
```

Users may have [issues installing PyYAML](https://stackoverflow.com/questions/49911550/how-to-upgrade-disutils-package-pyyaml) as a dependency with the error message:
```bash
Cannot uninstall 'PyYAML'. It is a distutils installed project and ...
```

One way around this is to run:
```bash
pip install --ignore-installed PyYAML
```
