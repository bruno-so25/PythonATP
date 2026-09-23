# pyATP

`pyATP` is a Python library for reading and manipulating ATP/EMTP input cards.

## Overview

ATP files are text-based and heavily rely on fixed-column formatting. This library exposes a small Python API to load ATP cards, inspect lines and components, and eventually build or modify sections such as `/BRANCH`.

## Installation

```bash
pip install -e .
```

## Quick start

```python
from pyATP import read_atp

card = read_atp("case.atp")
print(card.lines[0])
print(card.branches)
```

## Project structure

- `pyATP/` – package root
- `pyATP/objects/` – classes that model ATP lines, cards, branches and components
- `tests/` – automated tests

## Current status

This project is in an early stage. The current focus is on reading ATP input files and modeling fixed-column fields in a reusable way.
