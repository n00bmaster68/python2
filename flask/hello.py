name = input()
print(f"hello,{name}")
x = 28
if x>0:
	print("x is an positive integer")
elif x<0:
	print("x is an negative integer")
else:
    print("x is zero")
for i in range (5):
	print (i)

s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)

ages = {"alice":22, "bob": 27}
ages["char"] = 30
ages["alice"]+=1
print(ages)

def square(x):  
	return x*x
def factorial(x):
	if x==1 or x==0:
		return 1
	else:
		return x*factorial(x-1)
for i in range(10):
	print("{} squared is {}".format(i, square(i)))
	print("factorial of {} is {}".format(i, factorial(i)))

class point:
	def __init__(self,x,y):
		self.x=x
		self.y=y

p= point(5,10)
print(f"p.x= {p.x}")
print(f"p.y= {p.y}")