import urllib.request

url = 'https://www.gutenberg.org/files/11/11-0.txt'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
# print(text) # for testing



