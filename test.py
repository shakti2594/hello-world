#!/usr/bin/python

while True:
	try:
		s = raw_input()
		int(s)
		print 'Please enter string as value...'
		continue
	except ValueError:
		break


print 'string is', s
