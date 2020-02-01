import requests

root_url = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('dataset_3378_3.txt', encoding='utf8') as inf:
    url = inf.readline().strip()

response = requests.get(url)

while True:
    text = response.text
    print(text)
    if text.splitlines()[0].split(' ')[0] == 'We':
        break
    url = root_url + text
    response = requests.get(url)
print("----------")
print(text)


