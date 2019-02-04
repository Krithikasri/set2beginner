r,f=map(int,input().split())
for v in range(r,f+1):
	if(v>1):
		for n in range(2,v):
			if(v%n==0):
				break
		else:
			print(v)
