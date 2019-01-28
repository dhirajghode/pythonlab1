#Name:Dhiraj Ghode
#Div=P    Batch:P1
'''Write a program to find user entered sequence is a palindrome or not'''
x=list(input('Enter sequence'))
y=x[::-1]
print(x)
print(y)
if x==y:
	print('is a palindrome')
else:
	print('is not a palindrome')
