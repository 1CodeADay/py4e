# Exercise 3: Write a program that reads a file and prints the letters 
# in decreasing order of frequency. Your program should convert all the 
# input to lower case and only count the letters a-z. Your program should 
# not count spaces, digits, punctuation, or anything other than the letters a-z. 
# Find text samples from several different languages and see how letter frequency 
# varies between languages. Compare your results with the tables at 
# https://wikipedia.org/wiki/Letter_frequencies.

import string
count = 0
dictionary_letters = dict()
lst = list()

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()

    # Removes numbers and punctuation then sets all letters to lower case


    words = line.split()
    for word in words:
        for letter in word:
            count += 1
            dictionary_letters[letter] = dictionary_letters.get(letter, 0) + 1
# print(count)
# print(dictionary_letters)

for key, val in dictionary_letters.items():
    lst.append((val, key))

lst.sort(reverse=True)
# lst = sorted(lst, reverse=True)

for val, key in lst:
    print(key, val)