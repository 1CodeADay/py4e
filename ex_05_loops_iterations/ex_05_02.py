#Exercise 2: Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and
# put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

# smallest = None
# largest = None
# count = 0

# print('Before')
# while True:
#     sval = input('Enter a number: ')
#     if sval == 'done' :
#         break
   
#     try:
#         fval = float(sval)
        
#         if smallest is None :
#             smallest = fval
#         elif fval < smallest :
#             smallest = fval
#         elif largest is None :
#             largest = fval
#         elif fval > largest :
#             largest = fval
#     except:
        
#         print('Enter a valid number')
#         continue
#     count = count + 1
        
# print('Minimum is', smallest)
# print('Maximum is', largest)
# print(count)



largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum = float(num)
        
        if smallest is None:
            smallest = fnum
        elif fnum < smallest:
            smallest = fnum
        elif largest is None:
            largest = fnum
        elif fnum > largest:
            largest = fnum
    except:
        print("Invalid input")
        continue

print("Maximum is", int(largest))
print("Minimum is", smallest)
