#Name:Dhiraj Ghode
#Div:P     Batch:P
'''Write a python program to find whether given value is a palindrome or not'''
x=str(input('enter three digit  a value'))
z=x[::-1]
if x==z:
	print ('is a palindrome')
else:
	print ('is not a palindrome')
