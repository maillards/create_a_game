#falling platforms code
import turtle as trtl
import random
import time
#adds background
lvl = 1
background_one = "landscape.gif"
background_two = "city.gif"
background_three = "space.gif"
wn = trtl.Screen()
# sets background for every level
if lvl == 1:
  wn.bgpic(background_one)
if lvl == 2:
  wn.bgpic(background_two)
if lvl == 3:
  wn.bgpic(background_three)
  
cloud = "cloudd.gif"
truck = "truck2.gif"
rock = "rock2.gif"
wn.addshape(cloud)
wn.addshape(truck)
wn.addshape(rock)
#speed of game(for faster game speed needs to be changed/increased)
difficulty = 3
if difficulty == 3:
  speed = 15
if difficulty == 2:
  speed = 10
if difficulty == 1:
  speed = 5
# changes how many clouds there are 
cloud_amount = 10
platforms = []
o = 225
n = 275
for i in range(cloud_amount):
  x = random.randint(-200,200)
  y = random.randint(o,n)
  o += 100
  n += 100
  if lvl == 1:
    platform = trtl.Turtle(shape=cloud)
  if lvl == 2:
    platform = trtl.Turtle(shape=truck)
  if lvl == 3:
    platform = trtl.Turtle(shape=rock)
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

def timerr():
  for t in platforms:
      t.penup()
      t.forward(speed)
      t.pendown()
  wn.ontimer(timerr,1000)
 
      
move_platforms()


wn.mainloop()
