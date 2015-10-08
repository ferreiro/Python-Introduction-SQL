import json

with open('test.json') as data_file:    
    data = json.load(data_file)

for d in data['contacts']:
    print d['name']
    print d['surname1']
    print d['surname2']
    print d['phone']