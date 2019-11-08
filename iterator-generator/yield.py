def foo(l):
    for i in l:
        yield i

a = foo([1,2,3])
print(a)            # generator object
print(list(a))      # [1,2,3]
