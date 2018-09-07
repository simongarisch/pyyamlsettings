[![Build Status](https://travis-ci.org/simongarisch/yamlsettings.svg?branch=master)](https://travis-ci.org/simongarisch/yamlsettings)
[![Coverage Status](https://coveralls.io/repos/github/simongarisch/yamlsettings/badge.svg?branch=master)](https://coveralls.io/github/simongarisch/yamlsettings?branch=master)
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
result = settings.get_data("att1")
print(result) # 42

result = settings.get_data("level1", "level2", "b")
print(result) # 4
```
