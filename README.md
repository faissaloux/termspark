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