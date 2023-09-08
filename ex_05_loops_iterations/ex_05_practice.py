#Finding the average in a loop
count = 0
sum = 0
print('Before', count, sum)
for value in [3, 89, 34, 56, 78, 3]:
    count = count + 1
    sum = sum + value
    print(count, value, sum)
print('After', count, sum, sum / count)



