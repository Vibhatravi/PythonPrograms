class BaseClass1:
    def method1(self):
        print("Method 1 from BaseClass1")


class BaseClass2:
    def method2(self):
        print("Method 2 from BaseClass2")


class DerivedClass(BaseClass1, BaseClass2):
    def method3(self):
        print("Method 3 from DerivedClass")
        

obj = DerivedClass()


obj.method1()
obj.method2()


obj.method3()
