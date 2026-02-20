# Fraction — Custom Rational Number Class in Python

A custom implementation of a rational number (fraction) class built from scratch in Python,
without using the standard library's `fractions` module.

Built to deeply understand **Python's data model**, operator overloading, numeric protocols,
and the importance of testing.

---

## Why I Built This

Python already has a built-in `fractions.Fraction` — so why rebuild it?

The goal was never to replace it. The goal was to understand *how* it works internally:
- How does Python's `==` interact with `hash()`?
- What does `NotImplemented` actually do vs raising `TypeError`?
- Why does `//` behave differently from `int()` for negative numbers?

Building and testing this class answered all of those questions in a way that just reading docs never could.

---

## Features

- Full arithmetic — `+`, `-`, `*`, `/` supporting `int`, `float`, and `Fraction`
- Reverse operators — `__radd__`, `__rsub__`, `__rmul__`, `__rtruediv__`
- All comparison operators — `==`, `!=`, `<`, `>`, `<=`, `>=`
- Automatic GCD normalization on every construction
- Negative denominator handling — `Fraction(1, -2)` correctly stores as `-1/2`
- Correct `__hash__` — consistent with `==` across `int`, `float`, and `Fraction`
- Integer truncation toward zero with no float precision loss
- `from_float()` constructor with configurable precision
- `from_string()` constructor — parses `"3/4"`, `"-1/2"`, `"5"`
- Works correctly in `set`, `dict`, `sorted()`, `min()`, `max()`
- Type hints and docstrings throughout

---

## Usage

```python
from fraction import Fraction

# Basic construction
a = Fraction(1, 2)    # 1/2
b = Fraction(1, 3)    # 1/3

# Arithmetic
print(a + b)          # 5/6
print(a - b)          # 1/6
print(a * b)          # 1/6
print(a / b)          # 3/2

# Mixed types
print(a + 1)          # 3/2
print(a + 0.5)        # 1.0  (float)
print(2 * a)          # 1

# Comparison
print(a > b)          # True
print(a == Fraction(2, 4))  # True

# Conversions
print(int(Fraction(-7, 2)))    # -3  (truncates toward zero)
print(float(Fraction(1, 4)))   # 0.25
print(bool(Fraction(0)))       # False

# From string
print(Fraction.from_string("3/4"))   # 3/4
print(Fraction.from_string("-1/2"))  # -1/2
print(Fraction.from_string("5"))     # 5

# From float
print(Fraction.from_float(0.5))      # 1/2
print(Fraction.from_float(0.3, 6))   # 3/10

# Utility
print(Fraction(2, 3).reciprocal())   # 3/2
print(Fraction(1, 2).is_proper())    # True
print(Fraction(3, 2).is_improper())  # True
print(Fraction(3, 4).to_tuple())     # (3, 4)
print(Fraction(3, 4).to_string())    # "3/4"  (always p/q form)

# Works correctly in sets and dicts
s = {Fraction(1, 2), 0.5, Fraction(2, 4)}
print(len(s))          # 1 — all three are equal

d = {Fraction(2, 1): "two"}
print(d[2])            # "two" — int key finds Fraction entry
```

---

## Bugs Found Through Testing

Writing a comprehensive test suite uncovered three real bugs — the most valuable part of this project.

### Bug 1 — `__eq__` / `__ne__` raising `TypeError` for unknown types
**Problem:** Python's data model requires `__eq__` to return `NotImplemented` for unknown types,
not raise. Raising broke membership tests like `Fraction(1,2) in [Fraction(1,2), "hello", 42]`.

**Fix:** Replace `raise TypeError(...)` with `return NotImplemented` in `__eq__` and `__ne__`.

---

### Bug 2 — `__hash__` inconsistent with `__eq__`
**Problem:** Python requires: *if `a == b`, then `hash(a) == hash(b)`*.
The original implementation used `hash((numerator, denominator))`, which meant:
```
Fraction(1, 2) == 0.5        # True
hash(Fraction(1, 2)) == hash(0.5)  # False ← rule broken
```
This silently broke `dict` and `set` when mixing `Fraction` with `int` or `float`:
```python
d = {Fraction(1, 2): "half"}
d[0.5]   # KeyError — should have worked
```

**Fix:** Use `hash(self.__num / self.__den)` — mirrors Python's own `fractions.Fraction` approach.
This ensures hashes align with float and int comparisons automatically.

> **Note:** The `__hash__` fix was inspired by how Python's standard library `fractions.Fraction`
> solves the same problem. All other logic is original.

---

### Bug 3 — `__int__` using float division (precision risk)
**Problem:** The original `int(self.__num / self.__den)` uses float division, which loses
precision for very large integers (beyond float's 53-bit limit). Also, `//` (floor division)
rounds toward negative infinity, not toward zero — wrong for negative fractions.

```
int(Fraction(-7, 2))  should be  -3  (truncate toward zero)
-7 // 2               gives      -4  (floor — wrong!)
```

**Fix:** Integer-only truncation toward zero, no float involved:
```python
def __int__(self):
    if self.__num < 0:
        return -((-self.__num) // self.__den)  # flip, floor, flip back
    return self.__num // self.__den
```

---

## Design Decisions

Several implementation choices were made intentionally:

- Integer arithmetic was used instead of float conversion to avoid precision loss
- Truncation toward zero was implemented manually instead of using floor division, since floor behaves differently for negative values
- Float-to-fraction conversion uses configurable precision to produce human-readable ratios instead of exact but impractical representations
- __hash__ was aligned with numeric equality to maintain correct behavior in sets and dictionaries

These decisions ensure correctness, predictability, and consistency with Python's numeric model.

## Testing

A full test suite is included covering 130+ cases:

Run tests using pytest:

```bash
pytest -v
```

Tests cover construction and normalization, all arithmetic operators and their reverse variants,
all comparison operators, float/int/bool conversions, `from_float`, `from_string`, hash
consistency, zero-division guards, type error guards, and large integer precision.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/vaibhavkandhare1807/python-fraction
cd python-fraction
```

## Project Structure

```
python-fraction/
│
├── fraction.py        # Main Fraction class
├── test_fraction.py   # Full test suite (130+ tests)
├── README.md
```

---

## What I Learned

- Python's dunder method protocol and when each method is called
- The difference between `return NotImplemented` and `raise TypeError` — and why it matters
- Why `__hash__` must be consistent with `__eq__` and how to fix it when comparing across types
- Why `float.as_integer_ratio()` is exact but impractical for human-readable fractions
- That testing is where the real learning happens — not writing the code
- The difference between floor, ceil, and truncation toward zero, especially for negative numbers