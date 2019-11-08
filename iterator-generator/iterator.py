#!/usr/bin/env python3

import random

class RandomIterable:
    def __iter__(self):
        return self

    def next(self):
        if random.choice(["go", "go", "stop"]) == "stop":
            raise StopIteration
        else:
            print("go")
        return 1

if __name__ == '__main__':
	r = RandomIterable()
	while True:
		r.next()

