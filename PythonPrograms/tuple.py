t1=tuple(input("Enter the elements : "))
t2=tuple(input("Enter the elements : "))
while True:
    print("-"*50)
    print("1.Extract elements \n2.Length \n3.Repetition \n4.Count the elements \n5.Concatenate \n6.Maximum \n7.Minimum \n8.Tuple to list \n9.Last element \n10.Extract part of tuple \n0.Exit")
    print("-"*50)
    print("Tuple1 elements :",t1)
    ch=int(input("Enter the choice :"))
    if ch==1:
         c=int(input("Enter the location :"))
         if c<len(t1):
            print("Extracted element :",t1[c])
         else:
            print("specify proper index")
    elif ch==2:
         print("Length is :",len(t1))
    elif ch==3:
         t1=input()
         print("Repeated Tuple :",t1*2)
    elif ch==4:
         i=input("Enter element to count :")
         if i in t1:
            print("Count is :",t1.count(i))
         else:
            print("Enter valid element")
    elif ch==5:
         print("Concatenated tuple :",(t1+t2))
    elif ch==6:
         print("Maximum is :",max(t1))
    elif ch==7:
         print("Minimum is :",min(t1))
    elif ch==8:
         l=list(t2)
         print("converted to list :",l)
    elif ch==9:
         print("Last element :",t1[-1])
    elif ch==10:
         m=int(input("Start index :"))
         n=int(input("End index :"))
         if m<len(t1) & n<len(t1):
            print("Extracted tuple :",t1[m:n])
         else:
            print("Enter index within the range")
    elif ch==0:
         exit()
    else:
         print("Invalid Choice")
