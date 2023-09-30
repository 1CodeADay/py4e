# Exercise 4: Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created, look through the dictionary
# using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages
# and print how many messages the person has.

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195

count = 0
dictio = dict()
maximum = 0
maximum_address = ''

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    dictio[words[1]] = dictio.get(words[1], 0) + 1
    count += 1

for address in dictio:
    if dictio[address] > maximum:
        maximum = dictio[address]
        maximum_address = address
    
# print(dictio)
# print(count)
print(maximum_address, maximum)

# This was challeging but I am happy I kept on trying. 