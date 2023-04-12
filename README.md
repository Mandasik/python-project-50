### Hexlet tests and linter status:
[![Actions Status](https://github.com/Mandasik/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Mandasik/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/ac55f2cd7dc255ea7a6d/maintainability)](https://codeclimate.com/github/Mandasik/python-project-50/maintainability)
[![linnt-and-tests](https://github.com/Mandasik/python-project-50/actions/workflows/my-checks.yml/badge.svg)](https://github.com/Mandasik/python-project-50/actions/workflows/my-checks.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ac55f2cd7dc255ea7a6d/test_coverage)](https://codeclimate.com/github/Mandasik/python-project-50/test_coverage)
## Description
gendiff is a library that provides a tool for describing the differences between two files in json or yml format. It can be used as a command-line utility with flags --help and --format. As a library, it can be imported into your code. The interface function generate_diff takes two paths to the files being compared and an argument format_out that determines the format in which the difference will be presented. There are three available output formats: "stylish", "plain", and "json".
### Demonstration of the gendiff utility in the terminal.
[![asciicast](https://asciinema.org/a/576965.svg)](https://asciinema.org/a/576965)

To install the package, it is necessary to copy the repository to your computer using the following commands:

```bash
>> git clone git@github.com:Mandasik/python-project-50.git
```

After that, you can navigate to the directory with the repository and install the package:

```bash
>> cd python-project-50
>> poetry build
>> python3 -m pip install --user dist/*.whl
```
