# Python Function Call Tutorial

## 1. Function Definition
```python
def greet(name):
    return f"Hello, {name}!"
```

## 2. Positional Arguments
```python
def add(a, b):
    return a + b

result = add(2, 3)  # a=2, b=3 (positional)
```

## 3. Keyword Arguments
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

msg = greet(name="Alice", greeting="Hi")
```

## 4. *args – Variable Positional Arguments
```python
def sum_all(*args):
    return sum(args)

total = sum_all(1, 2, 3, 4)
```

## 5. **kwargs – Variable Keyword Arguments
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Bob", age=30)
```

## 6. / – Positional‑Only Parameters (Python 3.8+)
```python
def func(a, b, /, c, d):
    return a + b + c + d

# a and b must be passed positionally
result = func(1, 2, c=3, d=4)
```

## 7. Summary Table
| Syntax | Meaning |
|---|---|
| `func(a, b)` | positional arguments |
| `func(a=1, b=2)` | keyword arguments |
| `*args` | collect extra positional arguments |
| `**kwargs` | collect extra keyword arguments |
| `func(a, /, b)` | `a` is positional‑only |
