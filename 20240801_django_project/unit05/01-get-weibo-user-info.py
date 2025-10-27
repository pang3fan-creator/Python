import requests

params = {
    'access_token': '???',
    'uid': 70
}
res = requests.get(url='https://api.weibo.com/2/users/show.json', params=params)

print(res.json())
