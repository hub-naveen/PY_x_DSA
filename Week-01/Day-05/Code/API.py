#API(Request)
import requests

res = requests.get("https://api.github.com/users/octocat")
print(res.json())
