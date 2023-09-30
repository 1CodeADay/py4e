# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt

# Write a program that reads the words in words.txt and stores them as 
# keys in a dictionary. It doesn’t matter what the values are. Then you 
# can use the in operator as a fast way to check whether a string is in the dictionary.

# count = 0
# di = dict()
# fname = input('Enter a File: ')
# if len(fname) < 1:
#     fname = 'words.txt'
# fhandle = open(fname)
# for line in fhandle:
#     line = line.rstrip()
#     words = line.split()
#     # print(words)
#     for word in words:
#         count += 1
#         # print(word)
#         if word not in di:
#             di[word] = 1
#         else:
#             di[word] += 1
# print(di)
# print(count)

# if 'python' in di:
#     print('True')
# else:
#     print('False')

# very rewarding exercise







# count = 0 
# dictio = dict()

# fname = input('Enter a File: ')
# if len(fname) < 1:
#     fname = 'words.txt'
# fhandle = open(fname)
# for line in fhandle:
#     line = line.rstrip()
#     # print(line)
#     words = line.split()
#     # print(words)
#     for word in words:
#         dictio[word] = dictio.get(word,0) + 1

#         count += 1
#     #     if word not in dictio:
#     #         dictio[word] = 1
#     #     else:
#     #         dictio[word] += 1
#     # val = list(dictio.values())

# print(dictio)
# print(count)
# # print(val)

count = 0
dictio = dict()
fhand = open('words.txt')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        dictio[word] = dictio.get(word,0) + 1
        count += 1
print(dictio)
print(count)
