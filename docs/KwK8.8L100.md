# KwK 8.8 L/100

Our own Python Style Guide, naming expired by PEP 8 that we've directly inherited from and german
tank cannon - 8.8cm KwK 44 L/100 for E-75 Standardpanzer. Contains hell a lot of embedded references:

- 8 - reference to PEP 8, even twice of it
- 8.8 - reference to favourite poker hand of Keter Curtis (pair of eights, also known as snowmen)
- cm - can be an acronime for "coding mandatory"
- KwK - can be an acronime for "Koding writing Konvention", partially translated to german
- 44 - reference to our Python Guru - bozzyk44, that has no relation to this style guide at all but
is a mem person itself for Python related topics, so why not to mention him here
- L/100 - reference to hard limit of 100 characters per line that is different from 80 in PEP 8
- E - honestly, got a bit tired of fabrication of references, so why it won't stand for something
like Extraordinary?
- 75 - reference to numbers that were often used by main author of the guide (Keter Curtis) in his
old childhood nicknames like "NighTHunteR75"

Here won't be described all the rules from A to Z, assuming that if something isn't mentioned here
it'll be the same as in [PEP 8](https://www.python.org/dev/peps/pep-0008/). So it'll be great to
read that before. If something is new or different from PEP 8 or we use strict restrictions for
points that have some possible options - everything will be described bellow. Also just for
convenience some possible troublesome topics can be duplicated just to make more focus on them for
somebody who thinks he is quite familiar with PEP 8 and is sly enough not to read it before or feels
like he may have forgot something.

## Table of Contents

- [KwK 8.8 L/100](#kwk-88-l100)
  - [Table of Contents](#table-of-contents)
  - [Code Lay-out](#code-lay-out)
    - [Indentation](#indentation)
    - [Maximum Line Length](#maximum-line-length)
    - [Should a Line Break Before or After a Binary Operator?](#should-a-line-break-before-or-after-a-binary-operator)
    - [Imports](#imports)
    - [Module Level Dunder Names](#module-level-dunder-names)
  - [String Quotes](#string-quotes)
  - [Whitespace in Expressions and Statements](#whitespace-in-expressions-and-statements)
  - [When to Use Trailing Commas](#when-to-use-trailing-commas)
  - [Comments](#comments)
  - [Naming Conventions](#naming-conventions)
    - [Descriptive: Naming Styles](#descriptive-naming-styles)
  - [Programming Recommendations](#programming-recommendations)

## [Code Lay-out](https://www.python.org/dev/peps/pep-0008/#code-lay-out)

### [Indentation](https://www.python.org/dev/peps/pep-0008/#indentation)

**Forbidden:** Hanging indents *may* be indented to other than 4 spaces.

**Mandatory:** Break only before binary operators.

The closing brace/bracket/parenthesis on multiline constructs must be lined up under the first
character of the line that starts the multiline construct, as in:

```python
# Correct:
my_list = [
    1, 2, 3,
    4, 5, 6,
]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)

# Wrong:
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
```

### [Maximum Line Length](https://www.python.org/dev/peps/pep-0008/#maximum-line-length)

Line length limit is 100 characters, motivation is that such limit supports of opening two files
side by side and a console/file explorer tab on 24" monitor.

It's not a hard cap, though, having a small part of word or string over limit is fine, but having
multiply words/operators/whatever constructions over it should be omitted.

*Small tip:* for better auto formatting it's useful to toggle hard cap for formatters at something
like 120 characters, not to make everything line breaking immediately when you have only some
characters over 100, this way you could decide manually whether line break or not.

### [Should a Line Break Before or After a Binary Operator?](https://www.python.org/dev/peps/pep-0008/#should-a-line-break-before-or-after-a-binary-operator)

In opposite to PEP 8 here we're strict, the rule is to always break before binary operations.

```python
# Correct:
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

# Wrong:
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

### [Imports](https://www.python.org/dev/peps/pep-0008/#imports)

*Repeating:*

Imports should be grouped in the following order:

1. Standard library imports.
2. Related third party imports.
3. Local application/library specific imports.

You should put a blank line between each group of imports.

*Differences:*

Imports for every 3 major groups should be also subgrouped, `import package` should go first,
`from package import *` should go second, every subgroup should be ordered alphabetically.

### [Module Level Dunder Names](https://www.python.org/dev/peps/pep-0008/#module-level-dunder-names)

*Repeating:*

Module level "dunders" (i.e. names with two leading and two trailing underscores) such as `__all__`,
`__author__`, `__version__`, etc. should be placed after the module docstring but before any import
statements except from `__future__` imports. Python mandates that future-imports must appear in the
module before any other code except docstrings:

```python
"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys
```

## [String Quotes](https://www.python.org/dev/peps/pep-0008/#string-quotes)

All strings should be single-quoted except interpolation cases.

## [Whitespace in Expressions and Statements](https://www.python.org/dev/peps/pep-0008/#whitespace-in-expressions-and-statements)

*Repeating:*

However, in a slice the colon acts like a binary operator, and should have equal amounts on either
side (treating it as the operator with the lowest priority). In an extended slice, both colons must
have the same amount of spacing applied. Exception: when a slice parameter is omitted, the space is
omitted:

```python
# Correct:
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]

# Wrong:
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]
```

*Differences:*

PEP 8 forbides more than one space around an assignment (or other) operator to align it with another,
but our style permites it for cases where it will raise readability.

```python
# Permitted, but this example is quite bad as has small readability benefits
x             = 1
y             = 2
long_variable = 3

# Recommended usage example
ultra_very_long_variable = 1
long_variable            = 2
very_long_veriable       = 3
variable                 = 4
a_bit_longer_variable    = 5
```

PEP 8 recommends to consider adding whitespace around the operators with the lowest priority(ies) if
operators with different priorities are used, we prohibit it.

```python
# Correct:
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# Wrong:
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```

## [When to Use Trailing Commas](https://www.python.org/dev/peps/pep-0008/#when-to-use-trailing-commas)

PEP 8 only recommendes adding a trailing come to list or dictionaries, but our convention insists on
it.

```python
# Correct:
some_list = [
    value_1,
    value_2,
]

some_dict = {
    'key_1': value_1,
    'key_2': value_2,
}

# Wrong:
some_list = [
    value_1,
    value_2
]

some_dict = {
    'key_1': value_1,
    'key_2': value_2
}
```

## [Comments](https://www.python.org/dev/peps/pep-0008/#comments)

Completely skip everything from PEP 8, for comments and docstrings we have our own convention - TBD.

## [Naming Conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

### [Descriptive: Naming Styles](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles)

*Repeating:*

- `_single_leading_underscore`: weak "internal use" indicator. E.g. `from M import *` does not
import objects whose names start with an underscore.
- `single_trailing_underscore_`: used by convention to avoid conflicts with Python keyword, e.g.

```python
tkinter.Toplevel(master, class_='ClassName')
```

- `__double_leading_underscore`: when naming a class attribute, invokes name mangling (inside class
`FooBar`, `__boo` becomes `_FooBar__boo`

## [Programming Recommendations](https://www.python.org/dev/peps/pep-0008/#programming-recommendations)

PEP 8 forbids assigning a lambda expression directly to an identifier, but our style permits such
usage.

```python
# Permitted:
f = lambda x: 2 * x
```

*Repeating:*

- Be consistent in return statements. Either all return statements in a function should return an
expression, or none of them should. If any return statement returns an expression, any return
statements where no value is returned should explicitly state this as `return None`, and an explicit
return statement should be present at the end of the function (if reachable):

```python
# Correct:
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)

# Wrong:
def foo(x):
    if x >= 0:
        return math.sqrt(x)

def bar(x):
    if x < 0:
        return
    return math.sqrt(x)
```

- Use `''.startswith()` and `''.endswith()` instead of string slicing to check for prefixes or
suffixes.

`startswith()` and `endswith()` are cleaner and less error prone:

```python
# Correct:
if foo.startswith('bar'):

# Wrong:
if foo[:3] == 'bar':
```

- Don't compare boolean values to `True` or `False` using `==`:

```python
# Correct:
if greeting:

# Wrong:
if greeting == True:

# Worse wrong:
if greeting is True:
```
