import pymysql
db = pymysql.connect(host="172.16.34.105",user="mca019",passwd="mca019",database="mca019")
cur = db.cursor()
class MyDatabase:
	def display(self):
		cur.execute("Show databases")
		for db in cur:
			print(db)
	def create(self):
		cur.execute("Create table emp(name varchar(20),slno int(20),address varchar(20),empcode varchar(20),dob int(20),age int(20),mobile int(20),status varchar(20),designation varchar(20)")
		print("Table has been created")
	def showtable(self):
		print("The table created is : ")
		cur.execute("Describe table emp")
		cur.execute("Show tables")
		for self.tb in cur:
			print(self.tb)
	def insert(self):
		self.sqlform = "Insert into emp(name,slno,address,empcode,dob,age,mobile,status,designation) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		self.employee = [("Divya",101,"bangalore","em01",2001,21,6363,"single","manager"),("Usha",102,"bangalore","em02",2000,22,6362,"single","manager")]
		cur.executemany(self.sqlform, self.employee)
		db.commit()
		print("Values have been inserted")
	def displaytable(self):
		print("Contents that are in the table are")
		cur.execute("Select * from emp")
		self.result = cur.fetchall()
		for self.row in self.result:
			print(self.row)
	def delete(self,slno):
		self.sql = "Delete from em where slno = '%s'"%(int(slno))
		cur.execute(self.sql)
		db.commit()
		print("Record has been deleted")
	def droptable(self):
		self.delt = "Drop table emp"
		cur.execute(self.delt)
		db.commit()
		print("table has been dropped")

	def describe(self):
		print("table structure of emp is : ")
		self.desc = "desc emp"
		cur.execute(self.desc)
		for self.desc in cur:
			print(self.desc)
data = MyDatabase()
while True:
	print("\n1.DISPLAY DATABASE \n2.CREATE TABLE \n3.DISPLAY TABLE AND STRUCTURE \n4.INSERT VALUES \n5.DISPLAY ALL TABLE CONTENTS \n6.DELETE A RECORD \n7.DROP THE TABLE\n0.EXIT\n")
	ch = int(input("Enter your choice : "))
	if ch==1:
		data.display()
		print("-------------------------------")
	elif ch==2:
		data.create()
		print("------------------------------")
	elif ch==3:
		data.showtable()
		print("---------------------------------")
	elif ch==4:
		data.insert()
		print("---------------------------------")
	elif ch==5:
		data.displaytable()
		print("----------------------------------")
	elif ch==6:
		sl = int(input("Enter the serial no. that to be deleted from DB"))
		data.delete(sl)
		print("------------------------------")
	elif ch==7:
		data.droptable()
		print("-------------------------------")
	elif ch==8:
		data.describe()
		print("------------------------------")
	elif ch==0:
		exit()
	else:
		print("That is a wrong choice")


