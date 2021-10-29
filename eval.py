import json

f = open('data.json',)
f_read = f.read()
f.close()
f_json = json.dumps(f_read)
data = json.loads(f_json)
