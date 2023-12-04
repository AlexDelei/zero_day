"""
Classes and instances recap

Class Definition and syntax.

class ClassName:
    <statement1>
    ...
    ...
    <statement-n>
Class objects support two kinds of operations; attribute references and instantiation

Attribute references use the standard syntax used for all attribute references in Python: obj.name. 
Valid attribute names are all the names that were in the class's namespace when the class object was created. 

"""
class Myclass:
    """Example class"""
    i = 2345 # class attribute/ instance

    def fun(self, name): #class object fun
        self.name = name
        print("Hi {}".format(self.name))

print(Myclass.i) #attribute reference returning integer
exp = Myclass() #Class instatiation , creatind a new instance of the class and assigning it to the local variable exp
exp1 = exp.fun("Alex")
print(exp1) #attribute reference returning a function object
print(Myclass.__doc__) #Is also a valid attribute returning the docstring

##########

"""
Many classes like to create objects with instances customized to a specific initial state.
Therefore a class may define a special method named __init__(), like this:
"""
class Complex:
    """Class containing the __init__ method that creates an initial state"""

    def __init__(self, f_name, s_name): #an intial state methosd, it will be instatiated whenever the complex class is instatiated.\
        """initial state of the func"""  #holds the parameters f_name and s_name
        self.name1 = f_name # assigning the parameter f_name to the self parameter to be used when the method is instatiated
        self.name2 = s_name #same as above

x = Complex("Alex", "Delei")
print(x.name1) # referencing to the fisrtname in the objct 
print(x.name2) # referencing to the second name in the object

#dont mind about this for now
##########
x.counter = 1
while x.counter < 10:
    x.counter *= 2
print(x.counter)
##########

"""
Instances are variables for data unique to each instance.
Class variables are for attributes and methods shared by all instances of the class

"""
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Rex')
e = Dog('Billy')
print(d.kind) # shared by all
print(e.kind) # shared by all
print(d.name) # unique to d
print(e.name) # unique to e

##########

"""
Mistaken use of class variable
"""
class Dog:

    tricks = [] # creates a list to store the tricks

    def __init__(self, name): # initial state of the class instance , always executed first whenever an object is created
        self.name =  name # method instance

    def add_tricks(self, trick): # adding function
        self.tricks.append(trick)

d = Dog('Biggy') # first point where the init method is instantiated
e = Dog('Gift') # second point  '    '     '    '     '    '
d.add_tricks('Roll over')
e.add_tricks('Play dead :)')
print(e.tricks) # same as d.tricks because they refer to the class variable which is shared by all
print() # just an empty line

############

"""
Creating a list for each dog instead
"""

class Dog:
    """a unique list"""

    def __init__(self, name):
        self.name =  name
        self.tricks = [] # an empty list to store the tricks to a specific dog
    
    def add_tricks(self, trick):
        self.tricks.append(trick) # appending to our list

d = Dog('rotwilly')
e = Dog('john')
d.add_tricks('play dead :)')
e.add_tricks('roll over')
print(d.tricks, d.name) # not a class instance so its only specific to object vairable
print(e.tricks)

#############

"""
Methods may call other methods by using method attributes of the self argument.

Class that adds anything to a list.
"""

class Colors: # ClassName MUST begin with a capital letter
    
    def __init__(self): # initializing class
        self.data = [] # storage list

    def add(self, y): 
        self.data.append(y) # add argument to the  data list
    
    def add_twice(self, y):
        self.add(y) # referring the add method to add the argument y
        self.add(y)

a = Colors() # instatiating our class into an object
a.add("red") # adds once
a.add_twice("yellow") # adds twice 
print(a.data) # elements in our list

############

"""
Inheritance

syntax 
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>

The name BaseClassName must be defined in a namespace accessible from the scope containing the derived class definition.
There's nothing special about instantiation of derived classes: DerivedClassName() creates a new instance of the class.
Method references are resolved as follows: the corresponding class attribute is searched, descending down the chain of base classes if necessary, 
and the method reference is valid if this yields a function object.


There is a simple way to call the base class method directly: just call BaseClassName.methodname(self, arguments).
This is occasionally useful to clients as well.
(Note that this only works if the base class is accessible as BaseClassName in the global scope.)

Python has two inbuilt functions that work with inheritance
--> isinstance() - checks an instance's type
--> issubclass()  -  checks class inheritance
--> isinstance(obj, int) - returns true only if obj.__class__ is int or some class derived from int
--> issubclass(bool, int) - returns true since bool is a subclass of int
--> issubclass(False, int) - returns false since false is not a subclass of int  
"""
"""
Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}
"""
# Demonstration of inheritance

class Me(object):
    #Parent Class

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # printing function
    def Display_User(self):
        print(self.name , self.age)

y = Me("Alex", 19) # instatiating Me class
y.Display_User() # referencing to Display_user method

class Me2(Me): # Child process / inheriting the Me class

    def s_name(self): # printing function
        print("Delei")

y_2 = Me2("Saitoti", 20) # using the child class which will perform the same as Me / the parent class

y_2.Display_User() # display the y_2 object from the Parent class

y_2.s_name() # display y_2 object from the child class

##############

"""
Demonstrating how python constructors are called.
"""
class Person(object): # this is a parent class because of the object parameter

    def __init__(self, name, id_num): # __init__ constructor
        self.name = name # method variable name
        self.id = id_num # method variable id

    def display(self):  # printing method
        print(self.name , self.id) # name and id number

class Employee(Person): #Child class , it has inherited Person class

    def __init__(self, name, id_num, salary, post): # initial state of the class, so whenever the class is instatiated, the arguments to the parameters must be there!
        self.salary = salary # method variabel salary
        self.post = post # method variable post

        Person.__init__(self, name, id_num) # invoking the __init__ of the parent class
    
b = Employee("Sarah", 567, 56000, "IT department") # instatiating the class into an object variable b. Note the parameters must be there since we initialized the class with the paramaters.
b.display() # referencing the display method using the object b

##############

"""
super() function

The super() function is a built-in function that returns the objects that represent the parent class.
It allows to access the parent class's methods and attributes in the child class.
"""
class Person: # parent class Person , NB: missing the object parameter
    """lets see how this works"""

    def __init__(self, name, age): # initializing the class.
        self.name = name # method variable instatiatoin
        self.age = age # method variable instatiation

    def diplay(self): # printing method
        print(self.name , self.age)

class Student(Person): # child class, inheriting the parent class
    """we conitnue"""

    def __init__(self, name, age): # initializing my class
        self.s_name = name # method variable instatiation
        self.s_age = age # method variable instatiation

        super().__init__("Alex Delei", 19) #  this function , returns the objects in the parent class

    def diplay2(self): # printing method
        print(self.s_name, self.s_age)

obj = Student("Delei Saitoti", 44) # class instatiation into an object obj.
obj.diplay() # object referencing , refers to the parent class
obj.diplay2() # object referencing, refers to the child class