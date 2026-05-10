
#falling platforms code
import turtle as trtl
import random
import time
#adds background
background_lvl_one = "Screenshot 2026-05-06 7.55.57 PM.gif"
wn = trtl.Screen()
wn.bgpic(background_lvl_one)
cloud = "2b88ec17-f912-40e5-9049-b3e73bfe1c2c.gif"

wn.addshape(cloud)

# changes how many clouds there are 
cloud_amount = 10
platforms = []
o = 250
n = 300
for i in range(cloud_amount):
  x = random.randint(-200,200)
  y = random.randint(o,n)
  o += 100
  n += 100
  platform = trtl.Turtle(shape=cloud)
  platform.hideturtle()
  platform.penup()
  
  platform.goto(x,y)
  platform.pendown()
  platform.showturtle()
  platforms.append(platform)
  
def move_platforms():
  for t in platforms:
    t.right(90)
  for i in range(5):
    timerr()
#speed of game(for faster game speed needs to be changed)
speed = 1000
def timerr():
  for t in platforms:
      t.penup()
      t.forward(5)
      t.pendown()
  wn.ontimer(timerr,speed)
      
move_platforms()


wn.mainloop()
