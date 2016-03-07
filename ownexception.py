#!/usr/bin/python

class A:
	pass
class B:
	pass
class C:
	pass
for ZeroDivisionError  in [A,B,C]:
		try :
			raise ZeroDivisionError
		except A:
			print "i am A"
		except B:
			print "i am B"
		except C:
			print "i am C"

