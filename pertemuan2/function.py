def my_function():
  print("Hello from a function") 

my_function()

#Arguments

def my_function(nama):
  print("Hello ", nama) 

my_function("peby")

#

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") 

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes") 


#scope local

def myfunc():
  x = 300
  print(x)

myfunc() 
#
x = 300

def myfunc():
  print(x)

myfunc()

print(x) 


#void tidak mengembalikan apa-apa

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message) 

#

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

#

x = lambda a : a + 10
print(x(5)) 
#
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5) 
#

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value) 
  #

total = sum(x * x for x in range(10))
print(total) 

#Passing Different Data Types

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits) 

