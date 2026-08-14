# MSCCS-104 — Chapter 1: Computational Complexity — 2026-08-14

## Study Context

Primary material: **BAOU MSCCS-104 SLM**.

This session continued Chapter 1 and focused on understanding what mathematical preparation is required to perform well in the subject.

## 1. Mathematical Areas to Build

The main mathematical toolkit we identified for MSCCS-104 includes:

- GCD and Euclidean algorithms
- Extended Euclidean algorithm
- Modular arithmetic
- Modular inverses
- Finite groups
- Prime numbers
- Factorisation
- Primality testing
- Elliptic-curve mathematics
- Cryptographic mathematics

These areas should be learned progressively as they appear in the SLM rather than treated as a separate mathematics course.

## 2. Complexity and Asymptotic Reasoning

Previously established notation:

- `O` — Big-O: asymptotic upper bound
- `Ω` (Omega) — asymptotic lower bound
- `Θ` (Theta) — tight asymptotic bound

Example:

```text
T(n) = 7n² + 3n + 100
```

The dominant term is `n²`, so:

```text
T(n) = Θ(n²)
T(n) = O(n²)
T(n) = Ω(n²)
```

Asymptotic reasoning considers behaviour as:

```text
n → ∞
```

## 3. Polynomial vs Exponential Growth

Polynomial examples:

```text
O(n)
O(n²)
O(n³)
O(nᵏ)
```

where `k` is a fixed constant.

A common exponential example:

```text
O(2ⁿ)
```

Exponential growth becomes much larger than polynomial growth as the input size increases.

## 4. Computational Feasibility

A problem can be mathematically solvable while being computationally impractical at the relevant scale.

- **Feasible:** practical computational resources can solve the problem.
- **Infeasible:** the required resources become impractical.

Important distinction:

> Computationally infeasible does not mean mathematically impossible.

## 5. Computational Hardness and Cryptography

A central connection is:

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

Examples that become important later include:

- integer factorisation
- modular arithmetic
- discrete logarithms
- prime numbers
- modular inverses
- Euclidean algorithms

For example:

```text
p × q = N
```

is easy to compute when `p` and `q` are known, while recovering the prime factors of a sufficiently large `N` is the integer factorisation problem.

## 6. Brute Force and Search Spaces

For an `n`-bit uniformly random key:

```text
number of possible values = 2ⁿ
```

Therefore the brute-force search space grows exponentially with key length.

However, cryptographic security cannot be evaluated using brute force alone. The best known mathematical or algorithmic attack also matters.

## 7. P and NP — Initial Understanding

Current working definitions:

- **P:** problems solvable in polynomial time by deterministic algorithms.
- **NP:** problems for which a proposed solution can be verified in polynomial time.

The famous open question is:

```text
P = NP?
```

We are studying these concepts progressively and will return to the formal definitions and proofs as required by the SLM.

## 8. Exam Preparation Strategy

For an A-grade attempt, the target is not simply memorising definitions.

For each mathematical topic, the study progression should be:

```text
Recognise notation
      ↓
Understand meaning
      ↓
Work a calculation
      ↓
Explain the reasoning
      ↓
Solve an exam-style problem
      ↓
Handle proof/application questions
```

Particular attention should be given to mathematical notation and pronunciation so that symbols do not become a barrier to understanding.

## Chapter 1 Status

**In progress.**

Previously covered:

- Big-O
- Big-Ω (Omega)
- Big-Θ (Theta)
- Dominant terms
- Asymptotic reasoning
- Polynomial vs exponential growth
- Computational feasibility
- Computational hardness
- Brute-force search spaces
- Tractable vs intractable problems
- Initial P/NP concepts
- Connection between computational complexity and cryptography

Next work should continue with the remaining Chapter 1 material and assessment before moving forward.
