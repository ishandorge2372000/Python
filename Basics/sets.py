'''
fruits = ["apple", "banana", "cherry"]
x= fruits[0]
print(x)
print(y)
print(z)

x = "awesome"
def myfunc():
   x = "fantastic"
   print("Python is " + x)
myfunc()
print("Python is " + x)

x = 'awesome'

def myfunc():
  global x
  print("Inside function : Python is " + x)  
myfunc()
print("Python is " + x)

x = 5
print(type(x))

b = "Hello, World!"
print(b[-5:-2])

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
      print("Yes, 'apple' is in the fruits tuple")

tup = (1,2,3)
print(tup)
tup = ('a','b')
print(tup)

print(tup[0])      
'''
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
