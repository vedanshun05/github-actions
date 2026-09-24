# GitHub Actions

A simple calculator app used to learn GitHub Actions.

## Structure

```
github-actions/
├── app/
│   ├── __init__.py
│   └── calculator.py      # Calculator logic + CLI
├── tests/
│   └── test_calculator.py # Pytest tests
├── requirements.txt       # Dependencies
├── .gitignore
└── README.md
```

## Usage

```bash
python -m app.calculator
```

Enter `q` at any prompt to quit.

## Run tests

```bash
pip install -r requirements.txt
pytest tests/ -v
```
