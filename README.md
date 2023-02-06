![Logo](https://raw.githubusercontent.com/faissaloux/termspark/main/.github/art/logo.png)

[![Test Python package](https://github.com/faissaloux/termspark/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/faissaloux/termspark/actions/workflows/tests.yml) [![codecov](https://codecov.io/gh/faissaloux/termspark/branch/main/graph/badge.svg)](https://codecov.io/gh/faissaloux/termspark) [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/faissaloux/termspark/main.svg)](https://results.pre-commit.ci/latest/github/faissaloux/termspark/main) ![PyPI](https://img.shields.io/pypi/v/termspark) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/termspark) ![PyPI - Status](https://img.shields.io/pypi/status/termspark)

# Installation
```bash
    pip install termspark
```

# Usage
```python
    from termspark import TermSpark

    TermSpark().print_right('RIGHT').spark()
    TermSpark().spark_right('RIGHT').spark()
    TermSpark().print_left('LEFT').spark()
    TermSpark().spark_left('LEFT').spark()
    TermSpark().print_center('CENTER').spark()
    TermSpark().spark_center('CENTER').spark()
    TermSpark().line('.').spark()

    TermSpark().print_left('LEFT').print_right('RIGHT').set_separator('.').spark()
    TermSpark().print_left('LEFT').print_center('CENTER').print_right('RIGHT').set_separator('.').spark()
    TermSpark().spark_left('LEFT').spark_center('CENTER').spark_right('RIGHT').set_separator('.').spark()
```

> **Note**
> Separator can contain only one character max.

## You can also paint your content

**Supported colors:**
- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white
- gray / grey
- light red
- light green
- light yellow
- light blue
- light magenta
- light cyan

```python
    from termspark.termspark import TermSpark

    TermSpark().print_right('RIGHT', 'blue').spark()
    TermSpark().print_left('LEFT', 'light red').spark()
    TermSpark().print_center('CENTER', 'light_green').spark()
```

**Supported highlights:**
- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white
- gray / grey
- light red
- light green
- light yellow
- light blue
- light magenta
- light cyan

```python
    from termspark.termspark import TermSpark

    TermSpark().print_right('RIGHT', None, 'light_magenta').spark()
    TermSpark().print_left('LEFT', 'red', 'white').spark()
    TermSpark().print_center('CENTER', 'white', 'light blue').spark()
```

## You can use different styles on same position
```python
    from termspark.termspark import TermSpark

    TermSpark().spark_left([' * ', 'gray', 'white'], [' Info ', 'white', 'blue']).spark()
    TermSpark().spark_center([' * ', 'gray', 'white'], [' Warning ', 'white', 'yellow']).spark()
    TermSpark().spark_right([' * ', 'gray', 'white'], [' Error ', 'white', 'red']).spark()
```
`You know you can use them all together 😉`

## Lines are too long to write a termspark line! 😑
```python
    from termspark.termspark import TermSpark

    TermSpark().spark_left([' * ', 'gray', 'white'], [' Info ', 'white', 'blue']).spark_center([' * ', 'gray', 'white'], [' Warning ', 'white', 'yellow']).spark_right([' * ', 'gray', 'white'], [' Error ', 'white', 'red']).spark()
```
### You can separate them by calling each function in a line 🤤
```python
    from termspark.termspark import TermSpark

    termspark = TermSpark()
    termspark.spark_left([' * ', 'gray', 'white'], [' Info ', 'white', 'blue'])
    termspark.spark_center([' * ', 'gray', 'white'], [' Warning ', 'white', 'yellow'])
    termspark.spark_right([' * ', 'gray', 'white'], [' Error ', 'white', 'red'])
    termspark.spark()
```
### Still too long 🙄 Got you 🤩
```python
    from termspark.termspark import TermSpark

    termspark = TermSpark()
    termspark.spark_left([' * ', 'gray', 'white'])
    termspark.spark_left(' Info ', 'white', 'blue')
    termspark.spark_center([' * ', 'gray', 'white'])
    termspark.spark_center([' Warning ', 'white', 'yellow'])
    termspark.spark_right(' * ', 'gray', 'white')
    termspark.spark_right([' Error ', 'white', 'red'])
    termspark.spark()
```