k=int(input())
q=0
temp=k
while(temp>0):
	r=temp%10
	q=r**3+q
	temp=temp//10
if(k==q):
	print("yes")
else:
	print("no")
