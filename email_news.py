import requests
from dotenv import load_dotenv
import os

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

print(NEWS_API_KEY)

# url = "https://jsonplaceholder.typicode.com/posts"

# request = requests.get(url)
# content = request.text

# print(request)
# print(content)