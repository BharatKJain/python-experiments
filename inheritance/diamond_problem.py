"""
Code taken from GeeksForGeeks: https://www.geeksforgeeks.org/multiple-inheritance-in-python/

"""

# Python Program to depict multiple inheritance 
# when we try to call m of Class1 from both m of 
# Class2 and m of Class3 

# class Class1: 
# 	def m(self): 
# 		print("In Class1") 
	
# class Class2(Class1): 
# 	def m(self): 
# 		print("In Class2") 
# 		Class1.m(self) 

# class Class3(Class1): 
# 	def m(self): 
# 		print("In Class3") 
# 		Class1.m(self) 
	
# class Class4(Class2, Class3): 
# 	def m(self): 
# 		print("In Class4") 
# 		Class2.m(self) 
# 		Class3.m(self) 
# print("OUTPUT #1")
# obj = Class4() 
# obj.m() 

"""


"""

#Diamond problem solved using super()
# Python program to demonstrate 
# super() 

# class Class1: 
# 	def m(self): 
# 		print("In Class1") 

# class Class2(Class1): 
# 	def m(self): 
# 		print("In Class2") 
# 		super().m() 

# class Class3(Class1): 
# 	def m(self): 
# 		print("In Class3") 
# 		super().m() 

# class Class4(Class2, Class3): 
# 	def m(self): 
# 		print("In Class4") 
# 		super().m() 

# print("OUTPUT #2")
# obj = Class4() 
# obj.m() 



"""
Method resolution order

In Python, every class whether built-in or user-defined is derived from the object class and all the objects are instances of the class object. Hence, object class is the base class for all the other classes.

In the case of multiple inheritance a given attribute is first searched in the current class if it’s not found then it’s searched in the parent classes. The parent classes are searched in a depth-first, left-right fashion and each class is searched once.

If we see the above example then the order of search for the attributes will be Derived, Base1, Base2, object. The order that is followed is known as a linearization of the class Derived and this order is found out using a set of rules called Method Resolution Order (MRO).

To view the MRO of a class:

    Use the mro() method, it returns a list
    Eg. Class4.mro()
    Use the _mro_ attribute, it returns a tuple
    Eg. Class4.__mro__

"""
# Python program to demonstrate 
# super() 

class Class1: 
	def m(self): 
		print("In Class1") 

class Class2(Class1): 
	def m(self): 
		print("In Class2") 
		super().m() 

class Class3(Class1): 
	def m(self): 
		print("In Class3") 
		super().m() 

class Class4(Class2, Class3): 
	def m(self): 
		print("In Class4") 
		super().m() 
print("OUTPUT: #3")
print(Class4.mro())
