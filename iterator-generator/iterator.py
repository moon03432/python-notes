#!/usr/bin/env python3

import random

# any class implements __next__() and __iter__() is an Iterator
class RandomIterable:
    def __init__(self):
        self.count = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if random.choice(["go", "go", "stop"]) == "stop":
            raise StopIteration
        else:
            print("go")
        self.count += 1
        return self.count

if __name__ == '__main__':
	r = RandomIterable()
	# Using the iterator with a for loop (Pythonic way)
	for item in r:
		print(f"Got: {item}")
          
	print("Iteration stopped")

