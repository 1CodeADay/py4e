#Finding the largest value

largest_so_far = -1
print('Before', largest_so_far)
for num in [9, 12, 3, 42, 7, 89, 34]:
    if num > largest_so_far:
        largest_so_far = num
    print(num, largest_so_far)
print('After', largest_so_far)