import os

path = "/Users/moon/abc/AI/Data/megaage_asian/train"
for (dirpath, dirnames, filenames) in os.walk(path):
    for f in filenames:
        print(dirpath + '/' + f)
