[![Test Python package](https://github.com/faissaloux/termspark/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/faissaloux/termspark/actions/workflows/tests.yml) ![PyPI](https://img.shields.io/pypi/v/termspark) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/termspark) ![PyPI - Status](https://img.shields.io/pypi/status/termspark)

# Installation
```bash
    pip install termspark
```

# Usage
```python
    from termspark import TermSpark

    TermSpark().print_right('RIGHT')
    TermSpark().print_left('LEFT')
    TermSpark().print_center('CENTER')
    TermSpark().line('.')

    TermSpark().print_left('LEFT').print_right('RIGHT').set_separator('.')
    TermSpark().print_left('LEFT').print_center('CENTER').print_right('RIGHT').set_separator('.')
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

```python
    from termspark.termspark import TermSpark

    TermSpark().print_right('RIGHT', 'blue')
    TermSpark().print_left('LEFT', 'red')
    TermSpark().print_center('CENTER', 'green')
```