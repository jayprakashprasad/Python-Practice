# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

import random

thisset = ["apple", "banana", "cherry"]
print(thisset)
#t=thisset.discard("banana")
del thisset[0]
print(thisset)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
lists=str(list2)[1:-1]
list1.append(lists)
print(list1)

test_list = [5, 6, 8, 9, 10, 21] 
res = str(test_list)[1:-1] 
print(res) 

txt = " 'It's \n alright"
print(txt) 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist ="apple", "banana", "cherry"
mylist =list(thislist)
print(mylist)

x=2
y=float(3)
z=x+y
print(z)


x= ("    bannn    ")
y=x.strip()
print(*y)
#space never works in first line

xi= "bannn"
print("hwllo{}".join(xi))

txt = "     banana     "
x = txt.strip()
print(x)

y=(2.44)
print(int(y))
print(random.randint(1, 100))

