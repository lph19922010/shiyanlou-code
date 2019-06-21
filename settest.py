#!/usr/bin/env python3

import sys

list = sys.argv[1:]
set1 = set()
for argv in list:
	set1.add(argv)
print(' '.join(set1))
