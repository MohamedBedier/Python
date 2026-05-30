# About the File

| Field         | Details                   |
|---------------|---------------------------|
| **File Name** | Lec2                      |
| **Version**   | 1.00                      |
| **Author**    | Mohamed Bedier Mohamed    |

## Topics Covered

1. pip & package management
2. Virtual environments
3. Useful third-party modules
4. Strings — declaration & type conversion
5. String built-in methods (all categories)
6. Best practices

---

# pip

`pip` is Python's package manager, downloaded automatically with Python. It allows you to:

- **Install** packages
- **Uninstall** packages
- **Freeze** (list all installed packages)

```bash
pip --help
pip --version
pip freeze                   # list all installed packages
pip freeze > requirements.txt  # save them to a file
```

> **Note:** Every Python version has its own `pip` version.

| pip scope | Executable path |
|-----------|----------------|
| System-wide | `/usr/bin/pip` |
| Virtual environment | `venv/bin/pip` |

---

# Virtual Environment (venv)

A virtual environment isolates your project's packages from the system Python, preventing version conflicts between projects.

### Full Workflow

```bash
# 1. Create a virtual environment
python3 -m venv myvenv

# 2. Activate it
source myvenv/bin/activate       # macOS / Linux
myvenv\Scripts\activate          # Windows

# 3. Install packages inside it
pip install <package-name>

# 4. Deactivate when done
deactivate
```

### Install a Package

```bash
pip install <package-name>
# or (system-level via apt)
sudo apt-get install <package-name>
```

> ⚠️ Always **activate** the venv before installing packages, otherwise they install system-wide.

### Force Install (break system packages)

```bash
pip install <package-name> --break-system-packages
```

### Show Package Details

```bash
sudo apt-cache show <package-name>
pip show <package-name>           # pip alternative
```

---

# Useful Third-Party Modules

### pyfiglet

Converts plain text into large stylized **ASCII art** fonts.

```bash
pip install pyfiglet
```

```python
import pyfiglet
print(pyfiglet.figlet_format("Hello!"))
```

### gTTS (Google Text-to-Speech)

Converts text into spoken audio in any language.

```bash
pip install gTTS
```

```python
from gtts import gTTS
tts = gTTS("Hello, World!", lang="en")
tts.save("output.mp3")
```

---

# Strings

### Declaration

```python
mystring = "hello"
mystring = 'hello'
mystring: str = "hello"
```

### Type Conversion

```python
num = 42
converted = str(num)     # "42"
print(type(converted))   # <class 'str'>
```

### Check Variable Type

```python
x = "hello"
print(type(x))           # <class 'str'>
```

> **Remember:** Strings are **immutable** — all methods return a **new** string; the original is never changed.

---

# String Methods

## 1. Case Conversion

| Method | Description | Example |
|--------|-------------|---------|
| `.upper()` | All characters to uppercase | `"hello".upper()` → `"HELLO"` |
| `.lower()` | All characters to lowercase | `"HELLO".lower()` → `"hello"` |
| `.capitalize()` | First character uppercase, rest lowercase | `"hello world".capitalize()` → `"Hello world"` |
| `.title()` | First letter of each word uppercase | `"hello world".title()` → `"Hello World"` |
| `.swapcase()` | Swap upper↔lower for each character | `"Hello".swapcase()` → `"hELLO"` |
| `.casefold()` | Aggressive lowercase (best for comparisons) | `"ß".casefold()` → `"ss"` |

```python
text = "hello World"
print(text.upper())       # HELLO WORLD
print(text.lower())       # hello world
print(text.capitalize())  # Hello world
print(text.title())       # Hello World
print(text.swapcase())    # HELLO wORLD
print(text.casefold())    # hello world
```

---

## 2. Testing / Validation Methods

All return `True` or `False`.

| Method | Returns `True` when... |
|--------|------------------------|
| `.isalnum()` | All characters are letters **or** digits |
| `.isalpha()` | All characters are letters only |
| `.isdigit()` | All characters are digits (`0-9`) |
| `.isdecimal()` | All characters are decimal digits |
| `.isnumeric()` | All characters are numeric (includes ², ½, etc.) |
| `.isspace()` | All characters are whitespace |
| `.isupper()` | All cased characters are uppercase |
| `.islower()` | All cased characters are lowercase |
| `.istitle()` | String follows title casing rules |
| `.isidentifier()` | Valid Python identifier (variable name) |
| `.isascii()` | All characters are ASCII (0–127) |
| `.isprintable()` | All characters are printable |

```python
print("abc123".isalnum())    # True
print("abc".isalpha())       # True
print("123".isdigit())       # True
print("   ".isspace())       # True
print("Hello World".istitle()) # True
print("myVar".isidentifier()) # True
```

---

## 3. Search & Find

| Method | Description |
|--------|-------------|
| `.find(sub)` | Returns index of first occurrence, or `-1` if not found |
| `.rfind(sub)` | Like `find()` but searches from the **right** |
| `.index(sub)` | Like `find()` but raises `ValueError` if not found |
| `.rindex(sub)` | Like `index()` but searches from the **right** |
| `.count(sub)` | Returns number of non-overlapping occurrences |
| `.startswith(prefix)` | Returns `True` if string starts with prefix |
| `.endswith(suffix)` | Returns `True` if string ends with suffix |

```python
text = "hello world hello"
print(text.find("hello"))       # 0
print(text.rfind("hello"))      # 12
print(text.count("hello"))      # 2
print(text.startswith("hello")) # True
print(text.endswith("world"))   # False
```

---

## 4. Replace & Modify

| Method | Description |
|--------|-------------|
| `.replace(old, new)` | Replace all occurrences of `old` with `new` |
| `.maketrans(x, y)` | Create a translation table |
| `.translate(table)` | Apply a translation table to the string |

```python
text = "hello world"
print(text.replace("world", "Python"))   # hello Python

table = str.maketrans("aeiou", "12345")
print("hello".translate(table))           # h2ll4
```

---

## 5. Split & Join

| Method | Description |
|--------|-------------|
| `.split(sep)` | Split string by separator (default: whitespace) |
| `.rsplit(sep)` | Split from the **right** |
| `.splitlines()` | Split at line boundaries (`\n`, `\r\n`, etc.) |
| `.partition(sep)` | Split into 3 parts: before, sep, after (first match) |
| `.rpartition(sep)` | Like `partition()` but from the **right** |
| `.join(iterable)` | Join iterable elements with the string as separator |

```python
text = "hello world python"
print(text.split())                    # ['hello', 'world', 'python']
print(text.split(" ", 1))             # ['hello', 'world python']
print(text.partition("world"))        # ('hello ', 'world', ' python')

words = ["hello", "world"]
print(" ".join(words))                # hello world
print(",".join(words))                # hello,world

multiline = "line1\nline2\nline3"
print(multiline.splitlines())         # ['line1', 'line2', 'line3']
```

---

## 6. Formatting

| Method | Description |
|--------|-------------|
| `.format(*args, **kwargs)` | Insert values into `{}` placeholders |
| `.format_map(mapping)` | Like `format()` but takes a dictionary directly |

```python
# .format()
print("Hello, {}! You are {} years old.".format("Mohamed", 20))
print("Hello, {name}!".format(name="Mohamed"))

# f-string (modern preferred alternative)
name = "Mohamed"
print(f"Hello, {name}!")

# .format_map()
data = {"name": "Mohamed", "age": 20}
print("Hello, {name}! Age: {age}".format_map(data))
```

---

## 7. Trim & Pad

| Method | Description |
|--------|-------------|
| `.strip(chars)` | Remove leading & trailing characters (default: whitespace) |
| `.lstrip(chars)` | Remove leading (left) characters |
| `.rstrip(chars)` | Remove trailing (right) characters |
| `.center(width, fill)` | Center string in a field of given width |
| `.ljust(width, fill)` | Left-align string |
| `.rjust(width, fill)` | Right-align string |
| `.zfill(width)` | Pad with zeros on the left |

```python
text = "  hello  "
print(text.strip())          # "hello"
print(text.lstrip())         # "hello  "
print(text.rstrip())         # "  hello"

print("hi".center(10, "-"))  # ----hi----
print("hi".ljust(10, "."))   # hi........
print("hi".rjust(10, "."))   # ........hi
print("42".zfill(6))         # 000042
```

---

## 8. Encoding

| Method | Description |
|--------|-------------|
| `.encode(encoding)` | Encode string to `bytes` (default: UTF-8) |
| `.decode(encoding)` | Decode `bytes` back to `str` (called on `bytes`, not `str`) |

```python
text = "hello"
encoded = text.encode("utf-8")    # b'hello'
decoded = encoded.decode("utf-8") # 'hello'

print(type(encoded))   # <class 'bytes'>
print(type(decoded))   # <class 'str'>
```

---

# Summary Table — All String Methods

| Category | Methods |
|----------|---------|
| Case Conversion | `upper()`, `lower()`, `capitalize()`, `title()`, `swapcase()`, `casefold()` |
| Testing | `isalnum()`, `isalpha()`, `isdigit()`, `isspace()`, `isupper()`, `islower()`, `istitle()`, `isidentifier()`, `isdecimal()`, `isnumeric()`, `isascii()`, `isprintable()` |
| Search & Find | `find()`, `rfind()`, `index()`, `rindex()`, `count()`, `startswith()`, `endswith()` |
| Replace & Modify | `replace()`, `translate()`, `maketrans()` |
| Split & Join | `split()`, `rsplit()`, `splitlines()`, `partition()`, `rpartition()`, `join()` |
| Formatting | `format()`, `format_map()` |
| Trim & Pad | `strip()`, `lstrip()`, `rstrip()`, `center()`, `ljust()`, `rjust()`, `zfill()` |
| Encoding | `encode()`, `decode()` |

---

# Best Practices

- ✅ Use **f-strings** for modern, readable string formatting
- ✅ Use `.casefold()` instead of `.lower()` when comparing strings across languages
- ✅ Always handle `encoding`/`decoding` errors with `errors="ignore"` or `errors="replace"` when needed
- ✅ Chain multiple methods for cleaner code: `text.strip().lower().replace(" ", "_")`
- ✅ Remember: strings are **immutable** — every method returns a **new** string
- ✅ Use `pip freeze > requirements.txt` to save your project's dependencies
