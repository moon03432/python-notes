# A Generator implements __next__() and __iter__(),
# and will raise StopIteration exception when no more elements
g = (e for e in [1,2,3])

print(g)        # g is a generator object
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
print(next(g))  # raise a StopIteration exception