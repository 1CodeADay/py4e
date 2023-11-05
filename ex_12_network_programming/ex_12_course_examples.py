# How to write a socket.

import socket

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# encode() and b'' are equivalent.
mysock.send(cmd)

while True:
    data = mysock.recv(1024)
    if len(data) < 1 :
        break
    print(data.decode(),end='')
    # print(data.decode())
mysock.close()




# ASCII 

# print(ord('n'))

# encode() and b'' are equivalent.


# RETRIEVING AN IMAGE OVER HTTP 

# import socket
# # import time

# HOST = 'data.pr4e.org'
# PORT = 80
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect((HOST, PORT))
# mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
# count = 0
# picture = b''

# while True:
#     data = mysock.recv(5120)
#     if len(data) < 1: break
#     #time.sleep(0.25)
#     count = count + len(data)
#     print(len(data), count)
#     picture = picture + data
# mysock.close()

# # Look for the end of the header (2 CRLF)
# header_pos = picture.find(b'\r\n\r\n')
# print('Header length', header_pos)
# print(picture[:header_pos].decode()) 


# # Skip past the header and save the picture data
# picture = picture[header_pos+4:]
# fhand = open('stuff.jpg', 'wb')
# fhand.write(picture)
# fhand.close()



# RETRIEVING WEB PAGES WITH URLLIB 


# import urllib.request

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())


# import urllib.request
# import urllib.parse
# import urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)


# READING BINARY FILES USING URLLIB

# import urllib.request, urllib.parse, urllib.error

# img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
# fhand = open('cover.jpg', 'wb')
# fhand.write(img)
# fhand.close()

# from bs4 import BeautifulSoup

# html_doc = """
# <html>
# <head>
#     <title>Example HTML Page</title>
# </head>
# <body>
#     <h1>Welcome to Beautiful Soup</h1>
#     <p>This is an example paragraph.</p>
# </body>
# </html>
# """

# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

# AUTOGRADER : Request-Response Cycle

# import socket

# HOST = 'data.pr4e.org'
# PORT = 80
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect((HOST, PORT))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# # encode() and b'' are equivalent.
# mysock.send(cmd)

# while True:
#     data = mysock.recv(1024)
#     if len(data) < 1 :
#         break
#     print(data.decode(),end='')
#     # print(data.decode())
# mysock.close()


# PARSING HTML USING BEAUTIFULSOUP

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# # import ssl


# # Ignore SSL certificate errors
# # ctx = ssl.create_default_context()
# # ctx.check_hostname = False
# # ctx.verify_mode = ssl.CERT_NONE


# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')


# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))




# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

# url = input('Enter a url - ')
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')

# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))
    # print('TAG:', tag)
    # print('Attrs:', tag.attrs)
    # print('content:', tag.contents)
