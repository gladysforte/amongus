import turtle

body_color = 'yellow'
glass_color = '#9acedc'

win = turtle.getscreen()
impostor =turtle.Turtle()

def body():
    impostor.pensize(20)

    impostor.fillcolor(body_color)
    impostor.begin_fill()

    impostor.right(90)
    impostor.forward(50)
    impostor.right(180)
    impostor.circle(40, -180)
    impostor.right(180)
    impostor.forward(200)

    impostor.right(180)
    impostor.circle(100, -180)

    impostor.backward(20)
    impostor.left(15)
    impostor.circle(500, -20)
    impostor.backward(20)

    impostor.circle(40, -180)
    impostor.left(7)
    impostor.backward(50)

    impostor.up()
    impostor.left(90)
    impostor.forward(10)
    impostor.right(90)
    impostor.down()
    impostor.right(240)
    impostor.circle(50, -70)

    impostor.end_fill()

def glass():
    impostor.up()
    impostor.right(230)
    impostor.forward(100)
    impostor.left(90)
    impostor.forward(20)
    impostor.right(90)

    impostor.down()
    impostor.fillcolor(glass_color)
    impostor.begin_fill()

    impostor.right(150)
    impostor.circle(90, -55)

    impostor.right(180)
    impostor.forward(1)
    impostor.right(180)
    impostor.circle(10, -65)
    impostor.right(180)
    impostor.forward(110)
    impostor.right(180)

    impostor.circle(50, -190)
    impostor.right(170)
    impostor.forward(80)

    impostor.right(180)
    impostor.circle(45, -30)

    impostor.end_fill()

def backpack():
    impostor.up()
    impostor.right(60)
    impostor.forward(100)
    impostor.right(90)
    impostor.forward(75)

    impostor.fillcolor(body_color)
    impostor.begin_fill()

    impostor.down()
    impostor.forward(30)
    impostor.right(255)

    impostor.circle(300, -30)
    impostor.right(260)
    impostor.forward(30)

    impostor.end_fill()

    impostor.begin_fill()

    impostor.down()
    impostor.forward(30)
    impostor.right(255)

    impostor.circle(300, -30)
    impostor.right(260)
    impostor.forward(30)

    impostor.end_fill()


body()
glass()
backpack()
input("Press any key to continue")