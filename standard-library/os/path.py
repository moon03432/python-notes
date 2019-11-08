import os

print(__file__)
abspath = os.path.abspath(__file__)
print(abspath)
dirname = os.path.dirname(abspath)
print(dirname)
conf = os.path.join(dirname, 'conf')
print(conf)
root = os.path.normpath(dirname)
print(root)