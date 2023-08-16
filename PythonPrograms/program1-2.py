t1=tuple(input("Enter the tuple:"))
while True:
	print("----------------------------------------------------")
	print("1.length \n2.min \n3.max \n4.concatenation \n5.single element tuple \n6.reverse \n7.index \n8.extract \n9.print last element \n10.count \n11.repetation \n12.tuple to list \n0.exit")
	ch=int(input("Enter your choice:"))
	if ch==1:
		print(len(t1))
	elif ch==2:
		print(min(t1))
	elif ch==3:
		print(max(t1))
	elif ch==4:
		t2=tuple(input("enter another tuple"))
		print(t1+t2)
	elif ch==5:
		t3=tuple(input("enter one element",))
		print(t3)
	elif ch==6: 
		print(t1[::-1])
	elif ch==7:
		i=input("enter element")
		print(t1.index(i))
	elif ch==8:
		p=int(input("enter starting index"))
		q=int(input("enter ending index"))
		print(t1[p:q])
	elif ch==9:
		print(t1[-1])
	elif ch==10:
		j=input("enter element")
		print(t1.count(j))
	elif ch==11:
		k=int(input("enter times"))
		print(t1*k)
	elif ch==12:
		l=list(t1)
		print(l)
	else:
		exit()
