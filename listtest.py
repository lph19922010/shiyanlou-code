#!/usr/bin/env python3

import sys

if __name__ == '__main__':
	list1 = sys.argv[1:]

	list2 = []
	list3 = []
	for argv in list1:
		if len(argv) <= 3:
			list2.append(argv)
		else:
			list3.append(argv)

	print(' '.join(list2))
	print(' '.join(list3))
			
	
