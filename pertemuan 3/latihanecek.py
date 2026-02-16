class Person:
  def __init__(hao, name, grup, birth):
    hao.name = name
    hao.grup = grup
    hao.birth = birth
    

  def greet(hao):
    return "hallo, " + hao.name + " of " + hao.grup

  def welcome(hao):
    message = hao.greet()
    print(message + "! Enjoy listening to our song")

p1 = Person("vernon", "seventeen", "1998")
p2 = Person("juhoon", "cortis", "2008")
p3 = Person("mitchel Cave", "chase atlantic", "1996")

p1.welcome() 
print(p2.name, p2.grup)
print(p3.grup)
