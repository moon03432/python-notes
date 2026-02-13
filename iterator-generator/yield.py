# foo() is a generator function, which returns a generator object
def foo(l):
    for i in l:
        yield i # yield will return a value, and pause the function until next() is called

a = foo([1,2,3])

print(a)            # generator object
print(list(a))      # convert a generator object to a list [1,2,3]
