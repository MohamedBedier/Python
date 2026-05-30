# About the File

| Field         | Details                   |
|---------------|---------------------------|
| **File Name** | Lec3                      |
| **Version**   | 1.00                      |
| **Author**    | Mohamed Bedier Mohamed    |

## Topics Covered

1. Global variables
2. Memory management in Python (mutable vs immutable)
3. Garbage Collection
4. Lambda expressions
5. Useful third-party & built-in modules

---

# Scope & Global Variables

Python has two main variable scopes:

| Scope | Where it lives | Accessible from |
|-------|---------------|-----------------|
| **Local** | Inside a function | That function only |
| **Global** | Outside all functions | Anywhere in the file |

### Accessing a Global Variable Inside a Function

```python
x = 10  # global variable

def my_func():
    print(x)     # ✅ reading a global — works fine

my_func()        # 10
```

### Modifying a Global Variable Inside a Function

Without the `global` keyword, assigning to a variable inside a function creates a **new local variable** instead of modifying the global one:

```python
x = 10

def my_func():
    x = 99       # ❌ creates a LOCAL x, does NOT touch the global
    print(x)

my_func()        # 99
print(x)         # 10  ← global is unchanged
```

Use the `global` keyword to modify the global variable:

```python
x = 10

def my_func():
    global x     # ✅ now x refers to the global variable
    x = 99

my_func()
print(x)         # 99  ← global is now changed
```

---

# Memory Management in Python

## id() — Object Identity

Every object in Python has a unique memory address accessible via `id()`:

```python
x = 5
print(id(x))     # e.g. 140234567

y = x
print(id(y))     # same address as x — both point to the same object
```

## Immutable vs Mutable — Memory Behavior

Python treats immutable and mutable objects differently in memory:

### Immutable types (`int`, `float`, `str`, `tuple`)

Every time you assign a **new value**, Python creates a **new object at a different address**. The old object stays in memory until garbage collected.

```python
x = 5
print(id(x))     # address A

x = 10           # x now points to a NEW object
print(id(x))     # address B  (different!)
```

### Mutable types (`list`, `dict`, `set`)

Modifying the object **in place** keeps the **same memory address**.

```python
mylist = [1, 2, 3]
print(id(mylist))     # address A

mylist.append(4)      # modify in place
print(id(mylist))     # address A  (same!)

mylist = [1, 2, 3, 4] # reassignment → NEW object
print(id(mylist))     # address B  (different!)
```

---

# Garbage Collection (GC)

Python's garbage collector is an **automatic** process that handles memory allocation and deallocation, ensuring efficient memory use.

## How it works — Reference Counting

Python tracks how many variables (references) point to each object:

```
x = [1, 2, 3]    →  object at address A  (ref count = 1)
y = x             →  object at address A  (ref count = 2)
```

### Rule 1 — Only one reference

If an object is referenced by **only one variable**, the GC **can** reclaim (drop) the address and create a new one when the value changes.

```python
x = 10
# ref count of object "10" = 1
x = 99
# GC frees address of "10", x now points to a new address for "99"
```

### Rule 2 — Multiple references

If an object is referenced by **multiple variables**, the GC **cannot** change the address. It keeps it alive until all references are gone.

```python
x = [1, 2, 3]
y = x            # both x and y point to the same list
del x            # ref count drops to 1 (y still holds it)
del y            # ref count = 0 → GC frees the memory
```

> You can check reference count using the `sys` module:
>
> ```python
> import sys
> x = [1, 2, 3]
> print(sys.getrefcount(x))   # usually count + 1 (getrefcount itself adds a ref)
> ```

---

# Lambda Expressions

A **lambda** is a small, anonymous (nameless) function written in a single line. It is useful for short operations, especially when passed as an argument to other functions.

### Syntax

```python
variable = lambda arg1, arg2, ... : expression
```

### Comparison: regular function vs lambda

```python
# Regular function
def add(a, b):
    return a + b

# Equivalent lambda
add = lambda a, b: a + b

print(add(3, 5))   # 8
```

### Common use cases

```python
# With sorted()
names = ["Mohamed", "Ali", "Ziad"]
names.sort(key=lambda name: len(name))
print(names)   # ['Ali', 'Ziad', 'Mohamed']

# With map()
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)   # [1, 4, 9, 16]

# With filter()
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [2, 4, 6]
```

> ⚠️ Use lambdas only for **simple, single-expression** logic. For anything more complex, use a regular `def` function for readability.

---

# Useful Modules

## PyAutoGUI

Automates mouse and keyboard actions — useful for GUI automation scripts.

```bash
pip install pyautogui
```

```python
import pyautogui

pyautogui.moveTo(100, 200, duration=1)   # move mouse to (100, 200)
pyautogui.click()                         # left click
pyautogui.typewrite("Hello!", interval=0.1)  # type text
pyautogui.hotkey("ctrl", "c")            # press Ctrl+C
```

---

## subprocess

Runs **system commands** from within Python — like running a terminal command inside your script.

```python
import subprocess

# Run a command and capture output
result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(result.stdout)

# Run a shell command as a string
subprocess.run("echo Hello World", shell=True)
```

---

## os

Interacts with the **operating system** — files, directories, environment variables, and more.

```python
import os

print(os.getcwd())              # current working directory
os.mkdir("new_folder")          # create a directory
os.rename("old.txt", "new.txt") # rename a file
os.remove("file.txt")           # delete a file
print(os.listdir("."))          # list files in current dir
print(os.environ.get("PATH"))   # read environment variable
```

---

## BeautifulSoup

Parses and extracts data from **HTML and XML** — used for web scraping.

```bash
pip install beautifulsoup4 requests
```

```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)                        # page title
links = soup.find_all("a")                    # all <a> tags
for link in links:
    print(link.get("href"))                   # print each URL
```

---

# Summary

| Topic | Key Point |
|-------|-----------|
| `global` keyword | Required to **modify** a global variable inside a function |
| Immutable assignment | Creates a **new object** at a different memory address |
| Mutable in-place edit | Keeps the **same** memory address |
| Garbage Collection | Frees memory when **reference count reaches 0** |
| Lambda | Anonymous one-line function: `lambda args: expression` |
| `PyAutoGUI` | Automate mouse & keyboard |
| `subprocess` | Run system/terminal commands from Python |
| `os` | File system & OS interaction |
| `BeautifulSoup` | Parse HTML/XML for web scraping |
