import requests

t = requests.get('http://example.com')
print(t.text)

url = 'http://example.com'
params = {'key1': 'value1', 'key2': 'value2'}
cookies = {'cookie': 'working'}
r = requests.get(url, params=params, cookies=cookies)
print(r.url)
