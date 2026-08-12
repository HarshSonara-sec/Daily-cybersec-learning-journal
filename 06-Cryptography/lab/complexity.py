import time
import math


# --------------------------------------------------
# O(1) - Constant
# --------------------------------------------------

def constant(n):
    return 1


# --------------------------------------------------
# O(n) - Linear
# --------------------------------------------------

def linear(n):
    operations = 0

    for i in range(n):
        operations += 1

    return operations


# --------------------------------------------------
# O(n^2) - Quadratic
# --------------------------------------------------

def quadratic(n):
    operations = 0

    for i in range(n):
        for j in range(n):
            operations += 1

    return operations


# --------------------------------------------------
# O(log n) - Binary Search
# --------------------------------------------------

def binary_search(array, target):
    left = 0
    right = len(array) - 1
    operations = 0

    while left <= right:
        operations += 1

        middle = (left + right) // 2

        if array[middle] == target:
            return operations

        elif array[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return operations


# --------------------------------------------------
# O(n log n) - Merge Sort
# --------------------------------------------------

def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2

    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    return merge(left, right)


def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# --------------------------------------------------
# Complexity Comparison
# --------------------------------------------------

print("\n=== COMPLEXITY GROWTH ===\n")

for n in [10, 100, 1000, 10000]:

    print(f"n = {n}")

    print(f"O(1)     = {constant(n)}")
    print(f"O(n)     = {linear(n)}")
    print(f"O(n^2)   = {quadratic(n)}")

    print(f"O(log n) ≈ {math.log2(n):.2f}")

    print(f"O(n log n) ≈ {int(n * math.log2(n))}")

    print()


# --------------------------------------------------
# Binary Search Experiment
# --------------------------------------------------

print("\n=== BINARY SEARCH ===\n")

for n in [10, 100, 1000, 10000, 100000, 1000000]:

    numbers = list(range(n))

    target = n - 1

    operations = binary_search(numbers, target)

    print(
        f"n = {n:>8} | "
        f"operations = {operations:>3} | "
        f"log2(n) ≈ {math.log2(n):>6.2f}"
    )


# --------------------------------------------------
# Merge Sort Experiment
# --------------------------------------------------

print("\n=== MERGE SORT ===\n")

for n in [10, 100, 1000, 5000]:

    numbers = list(range(n, 0, -1))

    start = time.perf_counter()

    sorted_numbers = merge_sort(numbers)

    end = time.perf_counter()

    elapsed = end - start

    print(
        f"n = {n:>5} | "
        f"time = {elapsed:.6f} seconds | "
        f"correct = {sorted_numbers == sorted(numbers)}"
    )


# --------------------------------------------------
# Number Representation Experiment
# --------------------------------------------------

print("\n=== INTEGER BIT LENGTH ===\n")

numbers = [
    10,
    100,
    1000,
    1000000,
    2**32,
    2**64,
    2**128,
    2**256
]

for number in numbers:

    print(
        f"Number: {number}"
    )

    print(
        f"Bit length: {number.bit_length()}"
    )

    print()
