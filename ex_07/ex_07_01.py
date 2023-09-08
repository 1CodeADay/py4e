# fhand = open('reserved_words')
# count = 0
# for line in fhand:
#     count = count + 1

# print('Line Count:', count)




# fhand = open('reserved_words')
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])


fhand = open('reserved_words')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('#'):
        continue
    
    print(line)