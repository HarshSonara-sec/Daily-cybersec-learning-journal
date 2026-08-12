def constant(n):
    return 1


def linear(n):
    operations = 0

    for i in range(n):
        operations += 1

    return operations


def quadratic(n):
    operations = 0

    for i in range(n):
        for j in range(n):
            operations += 1

    return operations


for n in [10, 100, 1000]:
    print("n =", n)
    print("O(1)   =", constant(n))
    print("O(n)   =", linear(n))
    print("O(n²)  =", quadratic(n))
    print()
