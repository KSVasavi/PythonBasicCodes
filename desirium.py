'''count the position and then print armstrong'''
'''disiarum'''
num=int(input())
n1=num
org=num
count=0
ans=0
while(n>0):
    count=count+1
    n=n//10
while n1>0:
    dig=n1%10
    p=dig**count
    count=count-1
    ans=ans+p
    n1=n1//10
if ans==org:
    print("des")
else:
    print("no")