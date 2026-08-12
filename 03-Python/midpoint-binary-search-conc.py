numbers = [1, 2, 3, 4, 5, 6, 7, 8,
           9, 10, 11, 12, 13, 14, 15, 16]

target = 14

left = 0
right = len(numbers) - 1

print("\nnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]\n")
print("Target = 14\n")

while left <= right:

    middle = (left + right) // 2

    print("Middle:", numbers[middle])

    if numbers[middle] == target:
        print("Found:", target)
        break

    elif numbers[middle] < target:
        left = middle + 1

    else:
        right = middle - 1
