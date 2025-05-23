number1=[1,2,3,4,5]
number2=[6,7,8,9]
result=map(lambda x, y : x + y, number1,number2 )
print("addition of two lists")
print(list(result))
numbers=[1,2,3,4,5,6]
def sq(n):
    return n*n
square=list(map(sq,numbers))
print("squares of numbers in a list")
print(square)