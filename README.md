[![Test Python package](https://github.com/faissaloux/termspark/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/faissaloux/termspark/actions/workflows/tests.yml) ![PyPI](https://img.shields.io/pypi/v/termspark) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/termspark) ![PyPI - Status](https://img.shields.io/pypi/status/termspark)

# Installation
```bash
    pip install termspark
```

# Usage
```python
    from termspark import TermSpark

    TermSpark().print_right('RIGHT')
    TermSpark().spark_right('RIGHT')
    TermSpark().print_left('LEFT')
    TermSpark().spark_left('LEFT')
    TermSpark().print_center('CENTER')
    TermSpark().spark_center('CENTER')
    TermSpark().line('.')

    TermSpark().print_left('LEFT').print_right('RIGHT').set_separator('.')
    TermSpark().print_left('LEFT').print_center('CENTER').print_right('RIGHT').set_separator('.')
    TermSpark().spark_left('LEFT').spark_center('CENTER').spark_right('RIGHT').set_separator('.')
```

> **Note**
> Separator can contain only one character max.

##### You can also paint your content

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

    TermSpark().print_right('RIGHT', 'blue')
    TermSpark().print_left('LEFT', 'light red')
    TermSpark().print_center('CENTER', 'light_green')
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

    TermSpark().print_right('RIGHT', None, 'light_magenta')
    TermSpark().print_left('LEFT', 'red', 'white')
    TermSpark().print_center('CENTER', 'white', 'light blue')
```

##### You can use different styles on same position
```python
    from termspark.termspark import TermSpark

    TermSpark().spark_left([' * ', 'gray', 'white'], [' Info ', 'white', 'blue'])
    TermSpark().spark_center([' * ', 'gray', 'white'], [' Warning ', 'white', 'yellow'])
    TermSpark().spark_right([' * ', 'gray', 'white'], [' Error ', 'white', 'red'])
```
`You know you can use them all together 😉`