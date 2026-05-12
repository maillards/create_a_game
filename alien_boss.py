import turtle as t
# Imports random for code
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
# Boolean to see if the alien is defeated or not
defeated = False

# Controls where the alien moves(up or down)
step = 5

# While defeated is false
while not defeated:
  # Moves the alien up and down
  alien.sety(alien.ycor() + step)
  
  # Makes sure the alien bounces back the opposite direction if it
  #   goes too far
  if alien.ycor() > 120 or alien.ycor() < -120:
    step = step * -1
    
  # Randomly shoots the laser if a random integer chosen out of 1 to 40
      # Is equivalent to 1
  if random.randint(1, 40) == 1:
    # Shoots the laser
    laser.goto(alien.xcor(), alien.ycor())
    laser.showturtle()
    laser.goto(300, alien.ycor())
    laser.hideturtle()

wn.mainloop()
t.done()
  
    
    
