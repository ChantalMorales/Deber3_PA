import turtle
t=turtle.Pen()
#def letrac()
t.right(180) 
t.forward(130)
t.left(90)
t.forward(300)
t.left(90)
t.forward(130)
t.left(90)
t.forward(20)
t.left(90)
t.forward(110)
t.right(90)
t.forward(260)
t.right(90)
t.forward(110)
t.left(90)
t.forward(20)
t.penup()
t.right(90)
t.forward(10)
t.right(90)
t.forward(260)
t.left(90)
t.pendown()
#def LetraH()
t.left(90)
t.forward(100)
t.left(180)
t.forward(50)
t.left(90)
t.forward(75)
t.left(90)
t.forward(50)
t.left(180)
t.forward(100)

t.penup()
t.left(90)
t.forward(20)
t.pendown()


#def letraA()
for x in range(1,4):
	if x==1:
		t.penup()
	else:
		t.pendown()
	t.forward(100)
	t.left(120)
t.penup()
t.left(60)
t.forward(50)

t.pendown()
t.left(-60)
t.forward(50)


t.penup()
t.forward(40)
t.right(90)
t.forward(50)
t.left(90)
t.pendown()

#def letraN()
t.left(90)
t.forward(100)
t.right(135)
t.forward(130)
t.left(135)
t.forward(100)

t.penup()
t.right(90)
t.forward(20)
t.right(90)
#t.forward(100)
t.left(90)
t.pendown()

#def letraT()
t.forward(100)
t.left(180)
t.forward(50)
t.left(90)
t.forward(100)

t.penup()
t.left(90)
t.forward(40)
t.pendown()

#def letraA()
for x in range(1,4):
    if x==1:
        t.penup()
    else:
        t.pendown()
    t.forward(100)
    t.left(120)
t.penup()
t.left(60)
t.forward(50)

t.pendown()
t.left(-60)
t.forward(50)


t.penup()
t.forward(40)
t.left(90)
t.forward(50)
t.right(90)
t.pendown()

#def letraL()

t.right(90)
t.forward(100)
t.left(90)
t.forward(90)



turtle.getscreen()._root.mainloop()
