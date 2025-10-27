import requests

url = 'https://api.weibo.com/2/statuses/show.json'
params = {
    'access_token': '???',
    'id': 50
}
res = requests.get(url=url, params=params)

print(res.json())
