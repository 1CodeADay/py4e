# counts = {'hello':2, 'sis': 29, 'jo':45}
# for key in counts:
#     print(key, counts[key])





# counts = {'hello':2, 'sis': 29, 'jo':45}
# print(list(counts))
# print(counts.keys())
# print(counts.values())
# print(counts.items())

# eng2esp = dict()

# eng2esp['one'] = 'uno'
# eng2esp['two'] = 'dos'
# eng2esp['three'] = 'tres'
# eng2esp['four'] = 'cuatro'

# print(eng2esp)
# print(eng2esp['four'])
# print(len(eng2esp))


# var = 'b'
# code_var = ord(var)
# print(code_var)



# word = 'brontosaurus'
# d = dict()
# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] = d[c] + 1
# print(d)


# word = 'unticonstitutionnellement'
# d = dict()
# for c in word:
#     if c not in word:
#         d[c] = 1
#     else:
#         d[c] += 1
# print(d)

# word = 'brontosaurus'
# d = dict()
# for c in word:
#     d[c] = d.get(c,0) + 1
# print(d)




# ROMEO JULIET


# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief


# count = 0 
# diction = dict()
# fhand = open('romeo.txt')
# for line in fhand:
#     line = line.rstrip()
#     words = line.split()
#     # print(words)
#     for word in words:
#         count += 1
#         print(word)
#         diction[word] = diction.get(word,0) + 1
# print(diction)
# print(count)


# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# lst = list(counts.keys())
# print(lst)
# lst.sort()
# print(lst)
# for key in lst:
#     print(key, counts[key])


# Advanced text parsing

# But, soft! what light through yonder window breaks?
# It is the east, and Juliet is the sun.
# Arise, fair sun, and kill the envious moon,
# Who is already sick and pale with grief,

name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)






import string

string.punctuation

line = line.translate(line.maketrans('', '', string.punctuation))


