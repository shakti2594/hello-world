#!/usr/bin/python


try:
	name=raw_input('enter your name:')
	print'your name is :',name
	num1=raw_input('enter the first number:')
	num2=raw_input('inetr the seconf number:')
	print num1/num2

except KeyboardInterrupt:
		print 'sorry we are not able to fetch your input,exiting.....'
except TypeError:
	try:
		num1=int(num1)
		num2=int(num2)
		print num1/num2
	except ZeroDivisionError:
		print 'sorry there is no one in world who can divide any number with zero'
finally:
	print 'thanks for using our editor'








