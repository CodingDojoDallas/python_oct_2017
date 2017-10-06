import requests


r = requests.get('https://api.github.com/events')
print r

r = requests.post('http://httpbin.org/post', data = {'key':'value'})
print r

r = requests.put('http://httpbin.org/put', data = {'key':'value'})
print r

r = requests.delete('http://httpbin.org/delete')
print r

r = requests.head('http://httpbin.org/get')
print r

r = requests.options('http://httpbin.org/get')
print r
