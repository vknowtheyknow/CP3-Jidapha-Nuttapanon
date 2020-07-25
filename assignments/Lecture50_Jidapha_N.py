def addNumber(x,y): 
    print(f'{x}+{y} = {x+y}')
def minus(x,y):
    print(f'{x}-{y} = {x-y}')
def multiply(x,y): 
    print(f'{x}*{y} = {x*y}')
def divide(x,y): 
    print(f'{x}/{y} = {x/y :.2f}')

x = int(input('x = '))
y = int(input('y = '))

addNumber(x,y)
minus(x,y)
multiply(x,y)
divide(x,y)
