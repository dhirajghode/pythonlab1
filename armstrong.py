#Name: Dhiraj Ghode
#Div: P         Batch:P1
'''Write a python programme to find user entered no is a armstrong number or not'''
x=int(input('Enter three digit  value'))
a=x//100
r1=x%100
b=r1//10
r2=r1%10
c=r2
z=a**3+b**3+c**3
if x==z:
	print('armgstrong number ')
else:
	print('not an armstrong number')
