'''how many no. of digits
ask the number
find extract of number
power them to no. of digits value
add the number'''
num=int(input())
n1=num
org=n1
count=0
ans=0
while num>0:
    count=count+1
    num=num//10
while n1>0:
    dig=n1%10
    p=dig**count
    ans=ans+p
    n1=n1//10
if ans==org:
    print("arm")
else:
    print("no")