# import os
# import shutil
#
# print(os.getcwd())
# print(os.listdir(os.getcwd()))
# print(os.listdir("/Users/Sadhana/"))
#

# for f in os.listdir("/Users/Sadhana/AppData/Local/Programs/Python/Python37-32"):
#     print(f)
#     print(os.path.join("/Users/Sadhana/AppData/Local/Programs/Python/Python37-32", f))
#     print()

#Used to make requests
# import urllib.request
# import urllib.parse

# x = urllib.request.urlopen('http://www.berkshirehathaway.com/')
# print(x)
# print("hi")
# print(type(x))
# print("bye")
# print(x.read())
#
# print("used to parse values into the url")
# import urllib.parse
#

# url = 'http://www.berkshirehathaway.com/'
# values = {'q' : 'python programming tutorials'}
#
# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8') # data should be bytes
# req = urllib.request.Request(url, data)
# resp = urllib.request.urlopen(req)
# respData = resp.read()
#
# print(respData)

# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8') # data should be bytes
# req = urllib.request.Request(url, data)
# resp = urllib.request.urlopen(req)
# respData = resp.read()

import urllib.request
#import urllib.parse


url = 'http://www.berkshirehathaway.com/'
resp = urllib.request.urlopen(url)
respData = resp.read()
strng = str(respData)
print(strng)
print()

print("HTML Page contains "+str(len(strng))+" characters")
print()
searchh = "href"
countt = strng.count(searchh)
print("Number of urls =  "+str(countt))
print()
indx = 0
indx2 = 0

closee = "\">"

while indx < len(strng):
    indx = strng.find(searchh,indx)
    if indx==-1:
        break
    indx2 = strng.find(closee,indx)
    #print string from index+6 to indx2-1
    temp1 = indx + 6
    print(strng[temp1:indx2])
    #print("Found at:: ",str(indx)+" and "+str(indx2))
    indx += 4
