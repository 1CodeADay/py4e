#Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try and except
# and print an error message and skip to the next number.
#Enter a number: 4
#Enter a number: 5
#Enter a number: bad data
#Invalid input
#Enter a number: 7
#Enter a number: done
#16 3 5.333333333333333


# count = 0
# sum = 0

# while True:
    
#     str_val = input('Enter a number :')
#     if str_val == 'done':
#         break
#     try:
#         val = float(str_val)
#     except:
#         print("Invalid input")
#         continue
    
#     sum = sum + val
#     count = count + 1    
# print(sum, count, sum / count)

count = 0
total = 0.0

while True:
    sval = input('Enter a number: ')
    # an input gives us a string value
    if sval == 'done' :
        break
    
    try:
        fval = float(sval)
    except:
        print('Invalid input')

    print(fval)
    count = count + 1
    total = total + fval

print('ALL DONE')
print(total, count, total/count)