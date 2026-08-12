# MSCCS-104 — Computational Number Theory and Cryptography

## Chapter 1: Computational Complexity

### Study Session

**Date:** 2026-08-12

## 1. Computational Complexity

Computational complexity studies how the resources required by an algorithm change as the size of its input increases.

The main resources considered are:

* **Time complexity** — how much computational work is required.
* **Space complexity** — how much memory is required.

For algorithm analysis, the input size is commonly represented by `n`.

## 2. Big-O Notation

Big-O describes the growth behaviour of an algorithm as the input size increases.

Important examples studied:

| Complexity | Name        | Basic idea                          |
| ---------- | ----------- | ----------------------------------- |
| `O(1)`     | Constant    | Work does not depend on `n`         |
| `O(log n)` | Logarithmic | Problem is repeatedly reduced       |
| `O(n)`     | Linear      | Work grows with `n`                 |
| `O(n²)`    | Quadratic   | Work grows approximately as `n × n` |

## 3. Nested Loops and `O(n²)`

A loop running `n` times has approximately `n` iterations:

```python
for i in range(n):
    ...
```

Two nested loops produce approximately:

```text
n × n = n²
```

Therefore:

```text
O(n²)
```

The important reasoning is to count how many times the fundamental operation executes rather than simply memorising rules.

## 4. Binary Search and `O(log n)`

Binary search works on sorted data by repeatedly examining the middle and discarding the half that cannot contain the target.

Conceptually:

```text
n
↓
n/2
↓
n/4
↓
n/8
↓
...
```

Because the search space is repeatedly divided by approximately two, its complexity is:

```text
O(log n)
```

This provides an important practical example of logarithmic complexity.

## 5. Logarithm Intuition

A logarithm can be understood as asking:

> What exponent produces this value?

For example:

```text
2⁶ = 64
```

therefore:

```text
log₂(64) = 6
```

This explains why repeatedly dividing a problem by two produces logarithmic behaviour.

## 6. Connection to Cryptography

Computational complexity is important in cryptography because secure cryptographic systems often rely on mathematical problems that are easy to perform in one direction but computationally difficult to reverse.

Examples that will become important later include:

* Integer factorisation
* Discrete logarithms
* Large-integer modular arithmetic
* Primality testing
* Elliptic-curve problems

The objective is not simply to make an operation mathematically complicated, but to make the relevant problem computationally infeasible at an appropriate security size.

## 7. Current Progress

### Completed

* Basic computational-complexity concepts
* Big-O notation
* `O(1)`
* `O(n)`
* `O(n²)`
* `O(log n)`
* Loop-based complexity analysis
* Binary-search reasoning
* Initial Python implementation

### Remaining in Chapter 1

* Big-Ω
* Big-Θ
* Formal asymptotic analysis
* Polynomial vs. exponential complexity
* Computational hardness
* Chapter 1 assessment

**Chapter status:** In progress.
