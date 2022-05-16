import urllib3
import json

http = urllib3.PoolManager()
r = http.request('GET', 'http://192.168.0.104:8000/api/capitals/')
print(r.data)

with open('json_data.json', 'w') as outfile:
    my_json = r.data.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    json.dump(data, outfile, indent=4)

with open('json_data.json', 'r') as outfile:
    data = json.load(outfile)
    for item in data:
        print(item)
