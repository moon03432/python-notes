import ctypes

lib = ctypes.CDLL("/Users/moon/Workspace/Python/c-module/libadd.so")
print(lib)
print(lib.add(4,5))
