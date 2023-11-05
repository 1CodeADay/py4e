# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document
# from a URL, (2) displaying up to 3000 characters, and (3) counting the overall number of 
# characters in the document. Don’t worry about the headers for this exercise, simply show 
# the first 3000 characters of the document contents.


import urllib.request

url = input('Enter a url: ')
fhand = urllib.request.urlopen(url).read()
fhand = fhand.decode()

print(fhand)
print(len(fhand))




import urllib.request

url = input('Enter a url: ')
fhand = urllib.request.urlopen(url)
for line in fhand:
    # print(line.decode().strip())
    print(line.decode()[:3000])





