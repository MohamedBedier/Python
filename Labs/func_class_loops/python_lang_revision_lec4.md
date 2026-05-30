# About the File

| Field         | Details                   |
|---------------|---------------------------|
| **File Name** | Lec4                      |
| **Version**   | 1.00                      |
| **Author**    | Mohamed Bedier Mohamed    |

## Topics Covered

1. Object-Oriented Programming (OOP) concepts
2. Class & Object
3. `__init__` constructor
4. Instance vs Class variables
5. Methods (instance, class, static)
6. The four pillars of OOP
7. Magic / Dunder methods

---

# Object-Oriented Programming (OOP)

OOP is a programming paradigm that organizes code around **objects** rather than functions and logic. An object bundles **data (attributes)** and **behavior (methods)** together.

| Term | Meaning |
|------|---------|
| **Class** | A blueprint / template for creating objects |
| **Object** | An instance created from a class |
| **Attribute** | A variable that belongs to a class or object |
| **Method** | A function that belongs to a class |

---

# Class & Object

### Syntax

```python
class ClassName:
    # attributes and methods go here
    pass
```

### Creating an Object (Instance)

```python
class Car:
    pass

my_car = Car()    # my_car is an object (instance) of Car
print(type(my_car))  # <class '__main__.Car'>
```

---

# The `__init__` Constructor

`__init__` is a **special method** (called a magic/dunder method) that runs automatically when an object is created. It is used to initialize the object's attributes.

```python
class Car:
    def __init__(self, brand, color, year):
        self.brand = brand    # instance attribute
        self.color = color
        self.year  = year

my_car = Car("Toyota", "Red", 2022)
print(my_car.brand)   # Toyota
print(my_car.color)   # Red
print(my_car.year)    # 2022
```

> `self` refers to the **current object** being created or used. It must be the first parameter of every instance method.

---

# Instance Variables vs Class Variables

| Type | Defined | Shared? | Example |
|------|---------|---------|---------|
| **Instance variable** | Inside `__init__` using `self` | ❌ Each object has its own copy | `self.name = name` |
| **Class variable** | Inside the class, outside any method | ✅ Shared across all objects | `count = 0` |

```python
class Car:
    total_cars = 0          # class variable — shared by all objects

    def __init__(self, brand):
        self.brand = brand  # instance variable — unique per object
        Car.total_cars += 1

car1 = Car("Toyota")
car2 = Car("BMW")

print(car1.brand)       # Toyota
print(car2.brand)       # BMW
print(Car.total_cars)   # 2
```

---

# Methods

## Instance Method

The most common type. Has access to the object via `self`.

```python
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        print(f"{self.brand} goes {self.speed} km/h")

my_car = Car("Toyota", 180)
my_car.describe()    # Toyota goes 180 km/h
```

## Class Method

Has access to the **class itself** (not the object) via `cls`. Defined with `@classmethod`.

```python
class Car:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1

    @classmethod
    def get_total(cls):
        print(f"Total cars: {cls.total_cars}")

Car("Toyota")
Car("BMW")
Car.get_total()    # Total cars: 2
```

## Static Method

Has **no access** to the object or class. It's just a utility function placed inside the class for organization. Defined with `@staticmethod`.

```python
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

print(MathHelper.add(3, 5))    # 8
```

---

# The Four Pillars of OOP

## 1. Encapsulation

Bundling data and methods together, and **restricting direct access** to some of the object's components.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # private attribute (name mangling)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance       # controlled access via method

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())   # 1500
# print(account.__balance)     # ❌ AttributeError — can't access directly
```

| Prefix | Access Level | Example |
|--------|-------------|---------|
| No prefix | Public — accessible anywhere | `self.name` |
| `_` | Protected — accessible but signals "internal use" | `self._name` |
| `__` | Private — name-mangled, not directly accessible | `self.__name` |

---

## 2. Inheritance

A class (**child**) can **inherit** attributes and methods from another class (**parent**), promoting code reuse.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):              # Dog inherits from Animal
    def speak(self):            # override the parent method
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

dog = Dog("Rex")
cat = Cat("Luna")
dog.speak()    # Rex says Woof!
cat.speak()    # Luna says Meow!
```

### `super()` — Call the Parent's Method

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call Animal's __init__
        self.breed = breed

dog = Dog("Rex", "Labrador")
print(dog.name, dog.breed)   # Rex Labrador
```

---

## 3. Polymorphism

The ability of **different classes** to be used through the **same interface**, each responding differently.

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())   # each responds correctly
# 78.5
# 24
```

---

## 4. Abstraction

Hiding complex implementation details and exposing only what is necessary. Done using the `abc` module.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass     # no implementation here — subclasses MUST implement it

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())   # 78.5

# Shape()  ❌ TypeError — cannot instantiate abstract class
```

---

# Magic / Dunder Methods

Magic methods (surrounded by double underscores) let you define how objects behave with built-in Python operations.

| Method | Triggered by |
|--------|-------------|
| `__init__` | Object creation: `Car()` |
| `__str__` | `print(obj)` or `str(obj)` |
| `__repr__` | Developer-facing representation: `repr(obj)` |
| `__len__` | `len(obj)` |
| `__add__` | `obj1 + obj2` |
| `__eq__` | `obj1 == obj2` |
| `__lt__` | `obj1 < obj2` |

```python
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year  = year

    def __str__(self):
        return f"{self.brand} ({self.year})"

    def __eq__(self, other):
        return self.year == other.year

    def __lt__(self, other):
        return self.year < other.year

car1 = Car("Toyota", 2020)
car2 = Car("BMW",    2022)

print(car1)           # Toyota (2020)
print(car1 == car2)   # False
print(car1 < car2)    # True
```

---

# Summary

| Concept | Key Point |
|---------|-----------|
| **Class** | Blueprint for objects |
| **Object** | Instance of a class |
| `__init__` | Constructor — runs on object creation |
| `self` | Refers to the current object |
| **Instance variable** | Unique per object (`self.x`) |
| **Class variable** | Shared across all objects |
| **Encapsulation** | Restrict access with `_` / `__` |
| **Inheritance** | Child class reuses parent class code |
| **Polymorphism** | Same method name, different behavior per class |
| **Abstraction** | Hide details, expose only the interface (`ABC`) |
| **Magic methods** | Customize built-in behavior (`__str__`, `__add__`, etc.) |
