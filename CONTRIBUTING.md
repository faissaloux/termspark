# CONTRIBUTING

Contributions are welcome, and are accepted via pull requests.
Please review these guidelines before submitting any pull requests.

## Process

1. Fork the project
3. Create a new branch
3. Code, **test**, commit and push
4. Open a pull request detailing your changes.

## Guidelines

* Send a coherent commit history, making sure each individual commit in your pull request is meaningful.
* You may need to [rebase](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) to avoid merge conflicts.

## Setup
- Clone your fork

- Setup your virtual environment using `venv`
```bash
    python -m venv venv
```
- Activate your virtual environment

| Platform | Shell           | Command to activate venv          |
|----------|-----------------|-----------------------------------|
| POSIX    | bash/zsh        | $ source venv/bin/activate        |
|          | fish            | $ source venv/bin/activate.fish   |
|          | csh/tcsh        | $ source venv/bin/activate.csh    |
|          | PowerShell Core | C:\> venv\Scripts\activate.bat    |
| Windows  | cmd.exe         | $ source venv/bin/activate        |
|          | PowerShell      | PS C:\> venv\Scripts\Activate.ps1 |

- Install the dev dependencies:
```bash
pip install -e .[dev]
```
## Tests
Run all tests:
```bash
pytest
```
or
```bash
python -m pytest
```

> **Note**
> Make sure tests cover 100%
```bash
pytest --cov
```