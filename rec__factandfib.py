''' |                      |
    |___1*fact(0)__________|  STACK     
    |                      |   
    |___2*fact(1)_________ |  
    |                      |         
    |___2*fact(3)_________ |
    |                      |
    |___3*fact(4)_________ |'''
#fibnocci
def fib(n):
    #Base
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)
v=int(input())
res=fib(v)
print(res)