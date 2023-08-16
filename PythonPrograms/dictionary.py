
 
 
d=dict()

class employ:
	def add(self):
		self.name=input("Enter your name: ")
		self.adress=input("Enter your adress: ")
		self.pannumber=input("Enter your pan card number: ")
		self.basic_sal=float(input("Enter your basic salary: "))
		self.da=(float(input("Enter da percentage: "))/100)*self.basic_sal
		self.hra=(float(input("Enter hra percentage: "))/100)*self.basic_sal
		self.gross_sal=self.basic_sal+self.hra+self.da
		self.tax=(float(input("Enter tax percentage: "))/100)*self.gross_sal
		self.pf=float(input("Enter pf amount: "))
		self.lic=float(input("Enter lic amount: "))
		self.hl=float(input("Enter premium of house loan: "))
		self.deduction=self.pf+self.tax+self.lic+self.hl
		self.net_sal=self.gross_sal-self.deduction
		
		self.update()
	def update(self):
		d.update({self.name:{"Name":self.name,"Adress":self.adress,"Pan":self.pannumber,"Basic Salary":self.basic_sal,"da":self.da,"hra":self.hra,"Gross salary":self.gross_sal,"tax":self.tax,"pf":self.pf,"lic":self.lic,"house loan":self.hl,"deduction":self.deduction,"Net salary":self.net_sal}})
	def display(self):
		print(d)
	def search(self,name):
		if name in d:
			for keys in d:
				if keys==name:
					print(d[name])
		else:
			print("Employ not found")
obj=employ()
while True:
	print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
	print("1. to add employ\n 2.to display\n 3.search\n 4.exit\n")
	ch=int(input("Enter your choice: "))
	if ch==1:
		obj.add()
	elif ch==2:
		obj.display()
	elif ch==3:
		name=input("Enter the name of the employee to search: ")
		obj.search(name)
	elif ch==4:
		break
	else:
		print("Enter correct value")
		
