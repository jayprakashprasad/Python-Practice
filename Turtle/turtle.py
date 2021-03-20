import turtle  
t=turtle.Turtle()
list1=['yellow','red','blue','black']

t.up()
t.goto(200,0)
for  i in range(4):
    t.down()
    t.color(list1[i])
    t.pensize(10)
    t.circle(50)
    t.up()
    t.bk(100)

    ###
import turtle
t=turtle.Turtle()
list1=['silver','red','white','white','white']
#list1=['#C70039','#EE3510','#05302C','#0D57A0','black','#051730','green','red','silver']

for i in range(140):
    t.color(list1[i%1])
    t.pensize(i/10)
    t.forward(i)
    t.left(40)

#chancge the color,pensize,left