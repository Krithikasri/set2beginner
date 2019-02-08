n,l=map(int,input().split())
for s in range(n,l+1):
	t=0
	temp=s
	while(temp>0):
		x=temp%10
		t=x**3+t
		temp=temp//10
	if(s==t):
		print(s)
