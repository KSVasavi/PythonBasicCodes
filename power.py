def power(m,n):
    if m!=0 and n==0:
        return 1
    return m*power(m,n-1)
bas=int(input())
exp=int(input())
res=power(bas,exp)
print(res)