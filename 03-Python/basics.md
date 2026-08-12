# Python Supporting Notes — Computational Complexity

## Purpose

Python is being used as a supporting tool for cybersecurity and MSCCS-104 computational experiments. Dedicated Python study has not yet been completed, so concepts are introduced when required by a lab.

## Concepts Reviewed

### Variables

```python
n = 10
```

Python variables do not require an explicit type declaration.

### Arithmetic

```python
n + 5
n * n
n ** 2
```

* `*` — multiplication
* `**` — exponentiation
* `//` — integer division

### `range()`

```python
range(5)
```

produces values from `0` through `4`.

Common forms:

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

### `for` Loops

```python
for i in range(n):
    print(i)
```

A Python `for` loop iterates over values supplied by an iterable such as `range()`.

### Nested Loops

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

The inner operation executes approximately `n × n` times, demonstrating `O(n²)` behaviour.

### `while` Loops

```python
while condition:
    # repeated code
```

A `while` loop continues while its condition is true.

### Binary Search Support

The binary-search lab introduced:

* `left` and `right` boundaries
* calculating a midpoint with `//`
* list indexing
* `if / elif / else`
* `break`

These concepts were used to demonstrate `O(log n)` behaviour.

## Learning Approach

Python will be learned incrementally alongside cybersecurity and computational-number-theory labs rather than through a separate full Python course at this stage.
