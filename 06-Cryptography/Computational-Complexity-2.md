# MSCCS-104 — Chapter 1: Computational Complexity

**Date:** 2026-08-13

## 1. Big-O, Big-Ω, and Big-Θ

### Big-O — O
Represents an asymptotic **upper bound**.

### Big-Ω — Ω
Represents an asymptotic **lower bound**.

### Big-Θ — Θ
Represents a **tight asymptotic bound**.

For:

```text
T(n) = 7n² + 3n + 100
```

the dominant term is `n²`, therefore:

```text
O(n²)
Ω(n²)
Θ(n²)
```

---

## 2. Dominant Terms

As `n` becomes very large, lower-order terms and constant factors become less important for asymptotic growth.

Example:

```text
T(n) = 5n³ + 100n² + 500n + 1000
```

The dominant term is `n³`.

Therefore:

```text
T(n) = Θ(n³)
```

and also:

```text
T(n) = O(n³)
T(n) = Ω(n³)
```

---

## 3. Formal Asymptotic Intuition

For Big-O:

```text
f(n) ≤ c · g(n)
```

for sufficiently large `n`.

For Big-Ω:

```text
f(n) ≥ c · g(n)
```

for sufficiently large `n`.

For Big-Θ:

```text
c₁g(n) ≤ f(n) ≤ c₂g(n)
```

for sufficiently large `n`.

Asymptotic analysis focuses on behaviour as:

```text
n → ∞
```

rather than exact performance for small inputs.

---

## 4. Polynomial vs. Exponential Complexity

### Polynomial

Examples:

```text
O(n)
O(n²)
O(n³)
O(nᵏ)
```

where `k` is a fixed constant.

### Exponential

A common example is:

```text
O(2ⁿ)
```

Exponential functions grow much more rapidly than polynomial functions.

Example:

```text
n = 20

n³ = 8,000
2²⁰ = 1,048,576
```

---

## 5. Computational Feasibility

A problem can be mathematically solvable while still being computationally impractical.

**Feasible:** solvable using practical computational resources.

**Infeasible:** computational requirements become impractical at the relevant scale.

**Infeasible does not mean mathematically impossible.**

---

## 6. Computational Hardness

Computational hardness concerns how difficult a problem is to solve using available algorithms and computational resources.

A basic number-theory example is:

```text
p × q = N
```

Multiplication is efficient when `p` and `q` are known.

Recovering prime factors from a sufficiently large `N` is the integer factorisation problem.

Another important problem to study later is the discrete logarithm problem.

---

## 7. Brute Force and Search Spaces

For an `n`-bit uniformly random key, the number of possible values is:

```text
2ⁿ
```

The search space therefore grows exponentially with the number of bits.

However, cryptographic security cannot be judged from brute force alone. The best known mathematical or algorithmic attack is also important.

---

## 8. Connection to Cryptography

Conceptually:

```text
Number theory
    ↓
Mathematical problem
    ↓
Computational difficulty
    ↓
Attack feasibility
    ↓
Cryptographic security
```

Important future topics include:

- Integer factorisation
- Modular arithmetic
- Discrete logarithms
- Prime numbers
- Modular inverses
- Euclidean algorithms

These connect computational-complexity foundations to the number-theoretic foundations of cryptography.

---

## 9. Tractable and Intractable Problems

**Tractable:** generally refers to problems that can be solved efficiently, commonly associated with polynomial-time algorithms.

**Intractable:** refers to problems for which efficient solutions are not known or which become impractical at relevant scales.

This does not automatically prove that no efficient algorithm exists.

---

## 10. P and NP — Initial Introduction

The session briefly introduced:

- **P:** problems solvable in polynomial time by deterministic algorithms.
- **NP:** problems for which a proposed solution can be verified in polynomial time.
- The famous open question: `P = NP?`

A detailed study of complexity classes is not yet required at this stage.

---

## Chapter 1 Progress

### Completed
- Computational complexity
- Big-O
- Big-Ω
- Big-Θ
- Dominant terms
- Asymptotic analysis intuition
- Polynomial vs. exponential growth
- Computational feasibility
- Computational hardness
- Brute-force search spaces
- Tractable vs. intractable problems
- Initial P/NP concepts
- Connection between computational complexity and cryptography

### Remaining
- Chapter 1 review/assessment
- Any remaining syllabus-specific Chapter 1 material before progressing

**Status: Chapter 1 — In Progress**
