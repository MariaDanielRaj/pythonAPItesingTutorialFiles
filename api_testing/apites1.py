import requests
import json

baseurl="https://reqres.in/"

res = requests.get(baseurl + "api/users", params = {'page':2})

print(json.dumps(res.json(),indent=4))

resp=res.json()
#import ipdb; ipdb.set_trace()
first_names = [d['first_name'] for d in resp['data']]
print(first_names)


