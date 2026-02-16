#class/kelas
class MyClass:
  x = 5
#objek
p1 = MyClass()
print(p1.x) 
#multiple objek

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x) 

#menghapus objek
del p1 

#pass statement
class Person:
  pass

#init method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age) 

#
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age) 

#multiple parameters
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country) 

