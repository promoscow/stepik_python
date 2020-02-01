import requests

with open('dataset_3378_2.txt', encoding='utf8') as inf:
    url = inf.readline().strip()
text = requests.get(url).text
result = len(text.splitlines())
print(result)
