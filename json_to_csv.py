import json
import csv



with open('/home/user3/Documents/Cdac-Project/Activity/Activity_u00.json') as handle:
    dictdump = json.loads(handle.read())

print(dictdump)

newdict={}
for k,v in [(key,d[key]) for d in dictdump for key in d]:
  if k not in newdict: newdict[k]=[v]
  else: newdict[k].append(v)

print(newdict)

with open('/home/user3/Documents/Cdac-Project/Activity/mycsvfile.csv', 'w') as f:
    w = csv.DictWriter(f, newdict.keys())
    w.writeheader()
    w.writerow(newdict)