list=[] #4,0,5,0,1,9,0,0
j=0
v=int(input("no. of elements"))
for i in range(v):
    ele=int(input("elements"))
    list.append(ele)
    if list[i]!=0:
        list[j]=list[i]
        j=j+1
while j<v:
    list[j]=0
    j=j+1
print(list)
