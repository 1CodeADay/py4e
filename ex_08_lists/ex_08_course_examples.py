# Summary of the chapter 8

# Concept of a collection 
# Lists and definite loops
# Indexing a Lookup
# List mutability
# Slicing lists
# List methods: append, remove
# Sorting lists
# Splitting strings into lists of words



# friends = ['jos', 'sam', 'toto']
# print(len(friends))
# print(range(len(friends)))




# x = [1, 2, 3]
# y = [4, 5, 6]
# z = x + y
# print(z)





# stuff = list()
# stuff.append('book')
# print(stuff)
# stuff.append(99)
# print(stuff)




# some = [9, 4, 5, 6, 20]
# 9 in some





# total = 0
# count = 0
# while True:
#     var = input('Enter a number:')
#     if var == 'Done':
#         break
#     value = float(var)
#     total = total + value
#     count = count + 1
# average = total / count

# print('Total', total, 'Average:', average)




# numlist = list()
# while True:
#     try:
#         inp = input('Enter a number:')
#         value = float(inp)
#         if inp == 'done': 
#             break
#     except:
#         print('Enter a valid number')
#         continue
    
#     numlist.append(inp)
# average = sum(numlist) / len(numlist)
# print('Average:', average)




# numlist = list()
# while True:
#     inp = input('Enter a number:')
#     if inp == "done": 
#         break
#     value = float(inp)
#     numlist.append(value)

# average = sum(numlist) / len(numlist)
# print('Average:', average)


# SPLIT
# this code looks fine but it is not running

# # fname = input('Enter a file name: ')
# fhand = open('mbox-short.txt')
# # fhand = open(fname)

# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     words = line.split()
#     print(words[2])



# t = ['d', 'c', 'e', 'b', 'a']
# t = t.sort()
# print(t)

#list
# s = 'pining for the fjords'
# t = list(s)
# print(t)

#Split
# s = 'pining for the fjords'
# t = s.split()
# print(t)

# t1 = [1, 2]
# t2 = t1.append(3)
# print(t1)
# print(t2)


# def delete_head(t):
#     del t[0]
# letters = ['a', 'b', 'c']
# delete_head(letters)
# print(letters)


fruit = 'Banana'
# fruit[0] = 'b'
print(fruit[0])