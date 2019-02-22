import urllib.request

url = 'http://www.berkshirehathaway.com/ownman.pdf'
urllib.request.urlretrieve(url, 'sample.pdf')
print("Completed")
