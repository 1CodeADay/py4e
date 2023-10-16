# d = {'a':10, 'b':1, 'c':22}
# tmp = list()
# for k,v in d.items():
#     tmp.append((v,k))
# print(tmp)
# tmp = sorted(tmp, reverse=True)
# print(tmp)



# fhand = open('romeo.txt')
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0) + 1
# # print(counts)
# lst = list()
# for k,v in counts.items():
#     newtup = (v,k)
#     lst.append(newtup)
# # print(lst)
# lst = sorted(lst, reverse=True)
# # print(lst)
# for v, k in lst[0:10]:
#     print(v,k)


# txt = 'but soft what light in yonder window breaks'
# words = txt.split()
# t = list()
# for word in words:
#     t.append((len(word), word))

# t.sort(reverse=True)
# # print(t)

# res = list()
# for length, word in t:
#     res.append(word)

# print(res)


# d = {'a':10, 'b':1, 'c':22}
# for key, val in list(d.items()):
#     print(val, key)



# d = {'a':10, 'b':1, 'c':22}
# l = list()
# for key, val in d.items() :
#     l.append( (val, key) )
# print(l)
# l.sort(reverse=True)
# print(l)

# The most common words

import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
        
# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)