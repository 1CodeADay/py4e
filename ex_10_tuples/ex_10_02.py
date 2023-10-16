# Exercise 2: This program counts the distribution of the hour of the day for 
# each of the messages. You can pull the hour from the “From” line by finding 
# the time string and then splitting that string into parts using the colon character. 
# Once you have accumulated the counts for each hour, print out the counts, one per line, 
# sorted by hour as shown below.

# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1


count = 0
d_hours = dict()
lst = list()

fhand = open('mbox-short.txt')
for line in fhand:
    # line = line.rstrip()
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    # print(words)

    colon_mark = words[5].find(':')
    hour = words[5][:colon_mark]
    # print(hour)

    d_hours[hour] = d_hours.get(hour, 0) + 1

# print(d_hours)

for key, val in d_hours.items():
    lst.append((key, val))
lst.sort()
for key, val in lst:
    print(key, val)