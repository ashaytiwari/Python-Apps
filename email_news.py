import requests

url = "https://jsonplaceholder.typicode.com/posts"

request = requests.get(url)
content = request.text

print(request)
print(content)