
import requests
import json

baseurl="https://reqres.in/"
data = {
    "name": "morpheus",
    "job": "zion resident"
}
res = requests.del(baseurl + "api/users", data=data)
print(json.dumps(res.json(), indent=4))
#print(res)
#print(res.json())
