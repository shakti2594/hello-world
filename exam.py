#!/usr/bin/python
class A():
	def print_a(self):
		print 'A'
class B(A):
	def print_b(self):
		print'b'
class C(A):
	def print_c(self):
		print'C'
class D(B,C):
	def print_d(self):
		print'd'
obj=D()
obj.print_a()
obj.print_b()
obj.print_c()
obj.print_d()
