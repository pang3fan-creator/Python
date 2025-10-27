from urllib.parse import urlparse

url = 'http://127.0.0.1:8000/news/12345.html;lang=en?id=1&cid=6#ab'

parsed_url = urlparse(url)

print(parsed_url.scheme)
print(parsed_url.netloc)
print(parsed_url.path)
# 转换为字典
print(parsed_url._asdict())
