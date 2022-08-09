# single inheritance
class Parent():
       def first(self):
           print('first function')
 
class Child(Parent):
       def second(self):
          print('second function')
 
ob = Child()
ob.first()
ob.second()

# multiple inheritance
class Parent:
   def func1(self):
        print("this is function 1")
class Parent2:
   def func2(self):
        print("this is function 2")
class Child(Parent , Parent2):
    def func3(self):
        print("this is function 3")
 
ob = Child()
ob.func1()
ob.func2()
ob.func3()

# Multilevel Inheritance
class Parent:
      def func1(self):
          print("this is function 1")
class Child(Parent):
      def func2(self):
          print("this is function 2")
class Child2(Child):
      def func3(self):
        print("this is function 3")
ob = Child2()
ob.func1()
ob.func2()
ob.func3()


# Hierarchical Inheritance
class Parent:
      def func1(self):
          print("this is function 1")
class Child(Parent):
      def func2(self):
          print("this is function 2")
class Child2(Parent):
      def func3(self):
          print("this is function 3")
 
ob = Child()
ob1 = Child2()
ob.func1()
ob.func2()

# Hybrid Inheritance
class Parent:
     def func1(self):
         print("this is function one")
 
class Child(Parent):
     def func2(self):
         print("this is function 2")
 
class Child1(Parent):
     def func3(self):
         print(" this is function 3")
 
class Child3(Child1,Parent):
     def func4(self):
         print(" this is function 4")
 
ob = Child3()
ob.func1()
