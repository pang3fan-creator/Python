import requests

response = requests.get(url="http://httpbin.org/get",
                        headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"})
html = response.text
html_1 = response.content
# print(html)
print(html_1)
