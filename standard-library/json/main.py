import json

j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print j
print type(j)

e = j.encode('utf-8')
print e
print type(e)