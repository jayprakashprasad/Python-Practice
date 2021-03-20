date=21/9/20

##hhow ot determine
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'ale' is in the fruits tuple")
  
####
x= "    bannn    "
print(*x)#space never works in first line

xi= "bannn"
print("hwllo{}".join(xi))

txt = "     banana     "
x = txt.strip()
print(x)
##

  # Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import math

ages=(22,3,44,50,99,1) # im mutable # cannot change
print(ages) # print all element
print(ages[1:3])

thistuple = ["apple", "banana", "cherry", "orange", "kiwi", "melon",           "mango"]
print(thistuple[1:4])
thistuple.insert(1,'55')
print(thistuple)


thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'ale' is in the fruits tuple")
  
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple =("apple")
print(type(thistuple))

person = dict(name='hello',Age=21)
print(person['name'])
person['name']= 'hell'
print(person['name'])

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x)
    
thisdicts =	{"brand":"Ford","year":1964,"model":"Mustang"}
print(thisdicts)
for xi,y in thisdicts.items():
    print(xi,y)
thisdicts.popitem()
print(thisdicts)

jay = { "name":"jayy"}
jay1 = { "age":1 }
myxx = { 
    "jay":jay,
    "jay1":jay1
}    
print(myxx)

jay = dict(name="jayy")
jay1 = dict(age=1 )
myxx = dict( 
    jay=jay,
    jay1=jay1
)
print(myxx)
myxx.pop('jay')
print(myxx)


xi = math.pow(9,9)
print(xi)
x = math.sqrt(64.00)
print(int(x))
    






