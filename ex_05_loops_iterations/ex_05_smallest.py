#Finding the smallest value

smallest = None
print('Before')
for value in [9, 12, 3, 42, 7, 89, 34]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)

print('After', smallest)
