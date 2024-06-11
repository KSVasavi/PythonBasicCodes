'''no of prisoners, no. of chocolates, which person to start'''
n=6#int(input)
c=10#int(input)
s=3#int(input)
ans=(s+c-1)%n
if ans==0:
    print(n)

