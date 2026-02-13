def my_range(start, stop, step = 1):
    if stop <= start:
        raise RuntimeError("start must be smaller than stop")
    i = start
    while i < stop:
        yield i
        i += step

try:
    # this code will print from 10 to 50, with step 3
    for k in my_range(10, 50, 3):
        print(k)
except RuntimeError as e:
    print(e)
except:
    print("Unknown error occurred")
