import json

data = {"name":"Nav"}

with open("data.json","w") as f:
    json.dump(data,f)
