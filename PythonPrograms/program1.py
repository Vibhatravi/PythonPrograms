n1=input("Enter a first string")
n2=input("enter second string")
while True:
	print("1.Length of the string")
	print("2.String into uppercase")
	print("3.String into lowercase")
	print("4.reverse of the string")
	print("5.String into title")
	print("6.Count the number of letters")
	print("7.maximum of string")
	print("8.split the string")
	print("9.concatenation of string")
	print("10.replace character")
	ch = int(input("enter the choice")
	if ch == 1:
		print(len(n1))
	elif ch == 2:
		print(n1.upper())
	elif ch == 3:
		print(n1.lower())
	elif ch == 4:
		print(reverse(n1))
	elif ch == 5:
		print(title(n1))
	elif ch == 6:
		print(count(n1))
	elif ch == 7:
		print(max(n1))
	elif ch == 8:
		print(n1.split())
	elif ch == 9:
		print(n1+n2)
	elif ch == 10:
		print(n1.replace("a","b")
	else:
		exit()
