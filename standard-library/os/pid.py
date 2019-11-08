import os
import six

pid = os.getpid()
print(pid)
six_pid = six.text_type(pid)
print(six_pid)