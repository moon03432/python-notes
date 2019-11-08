#f = open("output.txt", "w")
#f.write("first line\n")
#f.write("second line\n")
#f.close()

#f = open("output.txt", "a")
#f.write("third line\n")
#f.close()

with open("output.txt", "a") as f:
	f.write("fourth line\n")
