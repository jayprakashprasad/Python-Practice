class myclass():
  def __str__(self):
    
   return "4"
print(myclass())

  def my_function(fname,lname):
      print(fname + lname+" Refsnes")
    my_function("Emil","ee")
    my_function("Emiel","ee")

  def my_function(*kids):
    print("The youngest child is " + kids[2])
  my_function("Emil", "Tobias", "Linus")


  def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
  my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

  def my_function(**kid):
    print("His last name is " + kid["lname"])
    my_function(fname = "Tobias", lname = "Refsnes")


  def my_function(**kid):
    print("His last name is " + kid["lname"])
    my_function(fname = "Tobias", lname = "Refsnes")


  def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


