#!/usr/bin/env python3

import collections

c = collections.Counter(cats=4,dogs=8)
print(c)
print(c['mouse'])
print(c.most_common(2))