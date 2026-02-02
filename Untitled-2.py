def find_sum(num1,num2):
    print(num1 + num2)
find_sum(10,20)

def find_square(num):
     print(num*num)
find_square(10)


def recursion(n):
    if n <=1:
        return n
    else:
        return n + recursion(n - 1)
s = recursion(10)
print(s)
    
def message():
    print("Hello World")
message()