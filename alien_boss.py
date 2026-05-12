import turtle as t
import random

alien_img = "alien.png"
laser_img = "laser.png"

wn = t.Screen()
wn.bgpic('space.jpg')

wn.addshape(alien_img)
wn.addshape(laser_img)

alien = t.Turtle()
alien.hideturtle()
alien.left(90)
alien.shape(alien_img)
alien.penup()
alien.goto(-190, 0)
alien.showturtle()

move_amount = 5

laser = t.Turtle()
laser.hideturtle()
laser.left(90)
laser.shape(laser_img)
laser.penup()


alien.speed(2)
defeated = False

step = 5

while True:
  alien.sety(alien.ycor() + step)
  
  if alien.ycor() > 120 or alien.ycor() < -120:
    step = step * -1
    
  if random.randint(1, 40) == 1:
    laser.goto(alien.xcor(), alien.ycor())
    laser.showturtle()
    laser.goto(300, alien.ycor())
    laser.hideturtle()

wn.mainloop()
t.done()
  
    
    
