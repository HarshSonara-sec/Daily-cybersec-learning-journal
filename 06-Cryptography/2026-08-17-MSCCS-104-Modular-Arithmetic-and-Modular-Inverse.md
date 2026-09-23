# MSCCS-104 — Modular Arithmetic and Modular Inverse

**Date:** 17 August 2026  
**Subject:** MSCCS-104 — Computational Number Theory and Cryptography

## 1. Modular Congruence

For integers `a`, `b`, and positive integer `n`:

```text
a ≡ b (mod n)
```

means that `a` and `b` leave the **same remainder** when divided by `n`.

Equivalent definition:

```text
n | (a - b)
```

Read `a ≡ b (mod n)` as:

> **a is congruent to b modulo n.**

### Example

```text
17 ≡ 2 (mod 5)
```

because:

```text
17 - 2 = 15
5 | 15
```

Another useful example with a negative number:

```text
-2 ≡ 5 (mod 7)
```

because:

```text
-2 - 5 = -7
7 | -7
```

The important idea is that congruence is about **difference being divisible by the modulus**, not about both numbers having to look like ordinary positive remainders.

---

# 2. Modular Inverse

The modular inverse of `a` modulo `n` is a number `x` satisfying:

```text
a × x ≡ 1 (mod n)
```

We write:

```text
a⁻¹ ≡ x (mod n)
```

### Example: inverse of 4 modulo 7

We want:

```text
4x ≡ 1 (mod 7)
```

Try small values:

```text
4 × 1 = 4
4 × 2 = 8 ≡ 1 (mod 7)
```

Therefore:

```text
4⁻¹ ≡ 2 (mod 7)
```

Verification:

```text
4 × 2 = 8
8 mod 7 = 1
```

---

# 3. When Does a Modular Inverse Exist?

The modular inverse of `a` modulo `n` exists **if and only if**:

```text
gcd(a, n) = 1
```

In other words, `a` and `n` must be **coprime**.

### Example

For `4 mod 7`:

```text
gcd(4, 7) = 1
```

So an inverse exists.

For `6 mod 9`:

```text
gcd(6, 9) = 3
```

So a modular inverse does **not** exist.

This gives a reliable test instead of guessing.

---

# 4. Finding the Inverse by Searching

For small numbers, we can test values of `x` until:

```text
a × x mod n = 1
```

Example: find `3⁻¹ mod 7`.

```text
3 × 1 = 3
3 × 2 = 6
3 × 3 = 9 ≡ 2
3 × 4 = 12 ≡ 5
3 × 5 = 15 ≡ 1
```

Therefore:

```text
3⁻¹ ≡ 5 (mod 7)
```

For larger values, trial-and-error becomes inefficient. This leads to the **Extended Euclidean Algorithm**.

---

# 5. Extended Euclidean Algorithm

The Extended Euclidean Algorithm finds integers `x` and `y` such that:

```text
a×x + n×y = gcd(a,n)
```

If:

```text
gcd(a,n) = 1
```

then:

```text
a×x + n×y = 1
```

Taking both sides modulo `n`:

```text
a×x ≡ 1 (mod n)
```

Therefore `x` is the modular inverse of `a` modulo `n`.

### Example: inverse of 3 modulo 5

Euclidean Algorithm:

```text
5 = 3×1 + 2
3 = 2×1 + 1
2 = 1×2 + 0
```

Back-substitute:

```text
1 = 3 - 2×1
```

From the first equation:

```text
2 = 5 - 3×1
```

Substitute:

```text
1 = 3 - (5 - 3)
1 = 2×3 - 5
```

Therefore:

```text
1 = 3×2 + 5×(-1)
```

So:

```text
3×2 ≡ 1 (mod 5)
```

Hence:

```text
3⁻¹ ≡ 2 (mod 5)
```

---

# 6. Common Mistake: Confusing Modulo and Congruence

It is useful to distinguish:

### Modulo operation

```text
23 mod 5 = 3
```

This asks for the remainder after division.

### Congruence

```text
23 ≡ 3 (mod 5)
```

This says that 23 and 3 belong to the same congruence class modulo 5.

Verification:

```text
23 - 3 = 20
5 | 20
```

A congruence statement can therefore be checked without performing ordinary long division:

```text
a ≡ b (mod n)
```

if and only if:

```text
n divides (a-b)
```

---

# 7. Practical Problem-Solving Method

When given:

```text
a⁻¹ mod n
```

use this workflow:

### Step 1 — Check the gcd

```text
gcd(a,n)
```

If it is not `1`, stop: the inverse does not exist.

### Step 2 — For small numbers

Search for `x` such that:

```text
a×x ≡ 1 (mod n)
```

### Step 3 — For larger numbers

Use the Extended Euclidean Algorithm.

### Step 4 — Verify

Always check:

```text
a×x mod n = 1
```

This verification step helps avoid arithmetic mistakes.

---

# 8. Key Examples

| Problem | Result | Reason |
|---|---:|---|
| `17 ≡ 2 (mod 5)` | True | Difference `15` is divisible by `5` |
| `-2 ≡ 5 (mod 7)` | True | Difference `-7` is divisible by `7` |
| `4⁻¹ (mod 7)` | `2` | `4×2 = 8 ≡ 1` |
| `3⁻¹ (mod 5)` | `2` | `3×2 = 6 ≡ 1` |
| `6⁻¹ (mod 9)` | Does not exist | `gcd(6,9)=3` |

---

# 9. Important Terms

- **Congruence** — equality of remainders modulo a number.
- **Modulus** — the number after `mod`.
- **Coprime** — two numbers whose greatest common divisor is `1`.
- **GCD** — Greatest Common Divisor.
- **Modular inverse** — a number that multiplies with `a` to give `1` modulo `n`.
- **Extended Euclidean Algorithm** — an algorithm used to find Bézout coefficients and modular inverses.
- **Bézout identity** — an equation of the form `ax + by = gcd(a,b)`.

## Symbol Pronunciation

- `≡` — **congruent to**
- `mod` — **modulo**
- `∣` — **divides** / **is a divisor of**
- `gcd` — **greatest common divisor**
- `⁻¹` — **inverse** / **multiplicative inverse**
- `x` — **x**
- `n` — **n**

---

## Study Note

The main difficulty today was not the formulas themselves, but developing intuition for what congruence means and how to reason about modular inverses without relying only on memorised tricks. The recommended approach is to verify every answer using the defining equation:

```text
a×x ≡ 1 (mod n)
```

and to use `gcd(a,n)=1` as the existence test.

### Next Step

Continue with the **Extended Euclidean Algorithm** through several small worked examples before moving into more advanced number-theoretic topics.
