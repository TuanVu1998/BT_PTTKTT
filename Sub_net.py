Array=[7,1,4,3,5,6]
M=11
s=[]
def tong_day(i):
	if i<len(Array):
		for j in range(i,len(Array)):
			if(sum(s)+Array[j])<=M:
				s.append(Array[j])
				if(sum(s))==M:
					print(s)
				else:
					tong_day(j+1)
				del s[len(s)-1]
tong_day(0)
