from urllib.parse import urlparse

url = 'http://127.0.0.1:8000/news/12345.html;lang=en?id=1&cid=6#ab'
parsed_url = urlparse(url)
print(parsed_url)
print(type(parsed_url))
