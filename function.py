def my_function():
  print("Hello from a function") 

my_function()

def my_function(nama):
  print("Hello ", nama) 

my_function("peby")

#void tidak mengembalikan apa-apa

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message) 

#Passing Different Data Types

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits) 

