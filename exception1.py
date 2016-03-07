#!/usr/bin/python

try:
	print "Enter your username"
	username=raw_input()
	username
	
except (KeyboardInterrupt,ValueError):
		print "sorry try again"
		Username=raw_input()
		print "username is always a string"
		
try:
	print "Enter your password"
	password=int(raw_input())
except ValueError:
		print "oops!that was not  valid number,the password contains only numbers...try again,"
		Password=int(raw_input())
except ValueError:
		print "sorry user name and password not valid...try later"
try:
	print "enter the number for the divison of two  number"
	print "number1"
	number1=int(raw_input())
	print"number2"
	number2=int(raw_input())
	print "division of above two number is",number1/number2
except ValueError:
	print "input should be number"
	number1=int(raw_input())
	number2=int(raw_input())
	print "division of above two number is",number1/number2

finally:
	print" thankyou visiting"

