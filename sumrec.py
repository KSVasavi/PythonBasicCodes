#sum of digits using recursion
def sum(number):
	if number==0:
		return 0
	return number%10+sum(number//10)
number=int(input())
ans=sum(number)
print(ans)
