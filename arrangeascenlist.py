#[count no. of 0's and 1's]

#0,1,2,Sort


list=[] #2,1,0,1,1,2,0,0
count_0=0
count_1=0
count_2=0
j=0
v=int(input("no. of elements"))
for i in range(v):
    ele=int(input("elements"))
    list.append(ele)
    if list[i]==0:
        count_0=count_0+1
    elif list[i]==1:
        count_1=count_1+1
    else:
        count_2=count_2+1
    print("Count of 0's",count_0,"count of 1's",count_1,"count of 2's",count_2)
while count_0>0:
    list[j]=0
    j=j+1
    count_0=count_0-1                  #compile time-OVERLOADING--------run time-OVERRIDING
while count_1>0:                       #when you use method or constructor overloading its not possible
    list[j]=1                          #for method we get positional arguments as error
    j=j+1                              #but operator overloading is possible
    count_1-=1                         #overriding functionality vil change
while count_2>0:                       #add can do adddition in one function
    list[j]=2                          #same add can do product in another
    j=j+1                              #function overriding,constructor overriding is possible
    count_2-=1                         

print(list)

                