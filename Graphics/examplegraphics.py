import turtle 

def circle(pen):
   
    pen.setposition(0, -280)
    pen.pendown()
    pen.begin_fill()
    pen.color('orange')
    pen.pensize(5)
    pen.pencolor('white')
    pen.circle(300)
    pen.end_fill()
    pen.penup()
  

def circle2(pen):
   
    pen.pensize(2)
    pen.setposition(0, -230)
    pen.pendown()
    pen.begin_fill()
    pen.color('black')
    pen.circle(250)
    pen.end_fill()
    pen.penup()

def draw_s(s):
    


    s.speed(1)
    s.penup()
    s.pencolor("white")
    s.pensize(5)
    turtle.bgcolor("black")
    s.setposition(60,180)
    s.pendown()
    s.penup()
    s.pendown()

    s.begin_fill()
    s.color('orange')

    s.right(180)
    s.forward(150)
    s.left(90)


    s.forward(150)
    s.left(90)
    s.forward(150)
    s.right(90)
    s.forward(150)
    s.right(90)
    s.forward(150)
    s.left(55)
    s.forward(40)
    s.left(125)
    s.forward(20)
    s.forward(180)
    s.left(90)
    s.forward(205)
    s.left(90)
    s.forward(150)
    s.right(90)
    s.forward(100)
    s.right(90)
    s.forward(150)
    s.left(130)
    s.forward(36)

    s.left(140)
    s.forward(25)
    s.penup()
    s.backward(25)
    s.right(90)
    s.forward(150)
    s.left(135)
    s.pendown()
    s.forward(36)
    s.right(45)
    s.penup()
    s.forward(105)
    s.pendown()
    s.right(55)
    s.forward(35)
    s.penup()
    s.left(145)
    s.forward(150)
    s.left(43)
    s.pendown()
    s.forward(35)


    

if __name__ == '__main__':
   
    win= turtle.Screen()
    win.bgcolor('black')

    siva = turtle.Turtle()
    siva.speed(10)
    siva.pensize(10)
    siva.penup()

    circle(siva)
    circle2(siva)
    draw_s(siva)
  
    turtle.done()