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

## Architecture layers

The project is organized in four layers so the API can evolve without mixing concerns:

```text
ATP file
  |
  v
ATPCard (raw text + section buffering)
  |
  v
ATPComponent / BranchComponent (fixed-column field abstractions)
  |
  v
ATPSection (logical grouping of records)
  |
  v
ATPCase (public high-level case model)
  |
  v
read_atp() (library entry point)
```

This keeps parsing and field handling close to the ATP format while leaving the public API focused on meaningful case/section operations.

## Example usage

```python
from pyATP import read_atp

case = read_atp("tests/data/sample.atp")

print(type(case).__name__)
print(list(case.sections.keys()))

for branch in case.branches:
    print({
        "type": branch.type,
        "n1": branch.n1,
        "n2": branch.n2,
        "resistance": branch.resistance,
    })
```

The example above loads an ATP file, exposes the available sections in the case, and iterates over branch components from the `/BRANCH` section with access to their fixed-column values.

## Current status

This project is in an early stage. The current focus is on reading ATP input files and modeling fixed-column fields in a reusable way.
