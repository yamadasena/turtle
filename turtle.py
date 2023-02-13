import turtle
import tkinter as tk

kame= turtle.Turtle()

kame.shape('turtle')
kame.shapesize(2,2,3)
kame.forward(150)
kame.backward(500)
kame.right(500)
kame.left(180)
kame.circle(150)
kame.undo()
kame.home()
kame.clear()

kame.getscreen().window_width()
960
kame.getscreen().window_height()
810
kame.position()
(0.00,0.00)
kame.goto(150,200)
kame.position()
(150.00,200.00)

kame.distance(0,0)
250.0
kame.penup()
kame.circle(150)
kame.isdown()
False
kame.pendown()

tk.mainloop()