f = open("output.txt", "r")
print(f.read())
#print(f.readlines())
#print(f.readline())
f.close()

f = open("output.txt", "r")
for line in f:
	print(line, end="")
f.close()
