# About the File

| Field       | Details                                      |
|-------------|----------------------------------------------|
| **File Name** | Lec1                                       |
| **Version**   | 1.00                                       |
| **Author**    | Mohamed Bedier Mohamed                     |

## Topics Covered

1. How to use `print()`
2. Comments (single-line and multi-line)
3. Escape sequence characters
4. Variables
5. Conditions
6. Loops

---

# Python

> Python is an **interpreted language** (compiled line by line). If any errors exist in the code, it runs until it reaches the error line.

---

# Interpreter

The Python interpreter consists of:

1. **Compiler** — converts source code to bytecode
2. **Bytecode** — similar to assembly language
3. **Machine Code** — translates bytecode for the target platform (detects if you're on macOS, Linux, or Windows and generates the appropriate machine code). Machine code is a set of instructions the processor understands.

---

# Terminal Commands

### Check Python version

```bash
python --version
```

### Open the live interpreter

```bash
python3
```

### Show disassembly code

```bash
python3 -m dis <filename>
```

### Shebang

Used to run the file with Python 3 via bash (`./filename`) without typing `python3`:

```bash
#!/usr/bin/env python3
```

---

# Comments

```python
# This is a single-line comment

"""
This is a
multi-line comment
"""
```

---

# Strings in Python

| Type | Syntax | Description |
|------|--------|-------------|
| Triple quote | `""" """` | Multi-line string |
| Raw string | `r""" """` | String as typed (ignores escape sequences) |
| Single inside double | `"\' \'"` | Single quotes inside double quotes |
| Double inside single | `'\" \"'` | Double quotes inside single quotes |
| f-string | `f"{variable}"` | Embed variables inside strings |

### String Operations

```python
print("a " * 3)   # Output: a  a  a
print("a" + "b")  # Output: ab
```

### Implicit Concatenation

```python
text = ("Hello, "
        "World!")  # Python joins adjacent string literals automatically
print(text)        # Output: Hello, World!
```

---

# Echo (Bash Command)

`echo` prints a string exactly as typed:

```bash
echo "mohamed \n bedier"
# Output: mohamed \n bedier
```

With `-e` flag, escape sequences are interpreted:

```bash
echo -e "mohamed \n bedier"
# Output:
# mohamed
# bedier
```

---

# Escape Sequences

| Sequence | Meaning |
|----------|---------|
| `\b` | Backspace |
| `\newline` | Escape newline (line continuation with `\`) |
| `\\` | Literal backslash |
| `\'` | Literal single quote |
| `\"` | Literal double quote |
| `\n` | New line |
| `\r` | Carriage return |
| `\t` | Horizontal tab |

---

# Input

```python
name = input("Enter your name: ")       # returns a string
age  = int(input("Enter your age: "))   # convert to int
```

`input()` always returns a `str`. Use type casting (`int()`, `float()`, etc.) to convert.

---

# Variables

Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.

### Two ways to declare a variable

```python
# 1 - Dynamic (type inferred automatically)
number = 5
number = 2.6
number = True

# 2 - Type-annotated (still dynamic, annotation is just a hint)
number: int   = 5
number: float = 2.6
number: bool  = False
```

> **Note:** Python is a **dynamically typed** language — the same variable can hold different types at different points in the code.

### View all Python keywords

```python
print(help("keywords"))
```

---

# Data Types in Python

| # | Type | Example |
|---|------|---------|
| 1 | `int` | `num = 5` |
| 2 | `float` | `num = 5.5` |
| 3 | `bool` | `flag = True` |
| 4 | `str` | `name = "Mohamed"` |
| 5 | `list` | `mylist = [1, 'no', 5.5]` |
| 6 | `dict` | `mydict = {"key": "value"}` |
| 7 | `set` | `myset = {1, 2, 3}` |
| 8 | `tuple` | `mytuple = (1, 2, 3)` |

---

# Data Type Properties

| Property | Meaning |
|----------|---------|
| **Mutable** | Can be edited, deleted, or added to |
| **Immutable** | Cannot be changed after creation |
| **Ordered** | Has a fixed arrangement; accessible by index/slicing |
| **Unordered** | No guaranteed arrangement |
| **Allows duplicates** | Repeated values are allowed |

### Summary Table

| Type | Mutable | Ordered | Duplicates |
|------|---------|---------|------------|
| `list` | ✅ | ✅ | ✅ |
| `tuple` | ❌ | ✅ | ✅ |
| `set` | ✅ | ❌ | ❌ |
| `dict` | ✅ | ✅ (Python 3.7+) | ❌ (keys) |
| `str` | ❌ | ✅ | ✅ |
| `bytes` | ❌ | ✅ | ✅ |
| `bytearray` | ✅ | ✅ | ✅ |

> **Note on `bytes`:** Passed to the compiler as bytes, but prints as a string representation.

---

# Membership & Identity Operators

| Operator | Description |
|----------|-------------|
| `in` | Returns `True` if value exists in sequence |
| `not in` | Returns `True` if value does **not** exist in sequence |
| `is` | Returns `True` if both variables point to the same object |
| `is not` | Returns `True` if they point to different objects |

---

# Conditions

```python
# Simple if-else
if condition:
    code
else:
    code

# if-elif-else chain
if condition:
    code
elif condition:
    code
else:
    code
```

---

# Loops

```python
# for loop
for i in range(0, 100):
    code

# while loop
while condition:
    code
    # don't forget to update the iteration variable!
```

---

# List Methods

| Method | Description |
|--------|-------------|
| `.append(x)` | Add element `x` at the end of the list |
| `.extend(iterable)` | Extend list by appending all items from another iterable |
| `.insert(i, x)` | Insert `x` before index `i` |
| `.remove(x)` | Remove the first occurrence of `x` |
| `.pop(i)` | Remove and return element at index `i` (default: last) |
| `.clear()` | Remove all items from the list |
| `.sort()` | Sort the list in ascending order (in place) |
| `.sort(reverse=True)` | Sort the list in descending order (in place) |
| `.reverse()` | Reverse the list in place |
| `.copy()` | Return a shallow copy of the list |
| `.count(x)` | Return the number of times `x` appears |
| `.index(x)` | Return the index of the first occurrence of `x` |

---

# Set Methods

| Method | Description |
|--------|-------------|
| `.add(x)` | Add element `x` to the set |
| `.remove(x)` | Remove `x`; raises `KeyError` if not found |
| `.discard(x)` | Remove `x`; does **not** raise an error if not found |
| `.pop()` | Remove and return an arbitrary element |
| `.clear()` | Remove all elements |
| `.union(s)` | Return a new set with all elements from both sets |
| `.intersection(s)` | Return elements common to both sets |
| `.intersection_update(s)` | Keep only common elements in the set (in place) |
| `.difference(s)` | Return elements in the set but not in `s` |
| `.difference_update(s)` | Remove elements found in `s` from the set (in place) |
| `.symmetric_difference(s)` | Return elements in either set, but not both |
| `.symmetric_difference_update(s)` | Update set with symmetric difference (in place) |
