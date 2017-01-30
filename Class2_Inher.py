class Parent:        # define parent class
   def myMethod(self):
      print 'Calling parent method'

class Child(Parent): # define child class
   def myMethod(self):
      print 'Calling child method'

   def cha(self):
       c=Parent()
       print 'cha',c.myMethod()


c = Child()          # instance of child
c.myMethod()
b= Parent()
b.myMethod()

c.cha()
