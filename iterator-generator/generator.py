a = (e for e in [1,2,3])
print(a)        # generator object
print(next(a))  # 1
print(next(a))  # 2
print(next(a))  # 3
print(next(a))  # raise a StopIteration exception