import turtle as t

#Images of the sprites I'll be using
bird = 'bird.png'
lion = "lion.png"
cat = "cat.png"
fish = 'fish.png'
boy = 'boy.png'
robot = 'robot.png'
girl = 'girl.png'


# Make the background
wn = t.Screen()
wn.bgpic("start.jpg")

# Adding the images as shapes
wn.addshape(lion)
wn.addshape(bird)
wn.addshape(cat)
wn.addshape(fish)
wn.addshape(boy)
wn.addshape(robot)
wn.addshape(girl)

# Add the button shape
button_img = "button.png"
wn.addshape(button_img)

# Assign an index variable to each sprite
choose = 0
# List of sprites user can pick
char =[girl, lion, cat, fish, boy, robot, bird]
lvl = 0

# Creates the user turtle
usr = t.Turtle()
usr.hideturtle()
usr.left(90)
usr.shape(char[choose])
usr.showturtle()

# Adds the button turtle
button = t.Turtle()
button.speed(50)
button.hideturtle()
button.left(90)
button.shape(button_img)
button.penup()
button.goto(0, -150)
button.showturtle()

# Adds the text
txt = t.Turtle()
txt.speed(50)
txt.hideturtle()
txt.penup()
txt.goto(0, 170)
txt.write("Choose your character!", align="center", font=("Arial", 16, 'bold'))
txt.goto(0, 150)
txt.write("USE LEFT RIGHT ARROWS", align="center", font=("Arial", 16, 'bold'))

# A boolean that checks if the player chose a character
chosen = False

# When the user clicks right the choose index adds by 1.
# If it reaches 6(last sprite), it starts back to 0
def plus():
  global choose
  if not chosen:
    choose += 1
    if choose>6:
      choose = 0
    usr.shape(char[choose])

# Same with plus function but opposite
def minus():
  global choose
  if not chosen:
    choose -= 1
    if choose<0:
      choose = 6
    usr.shape(char[choose])
  
# Confirms if the user clicked the button or not
def confirm(x, y):
  global chosen
  if -87 < x < 87 and -190 < y < -110 and not chosen:
    chosen = True
    txt.clear()
    button.hideturtle()
    
wn.onkey(plus, "Right")
wn.onkey(minus, "Left")

wn.onclick(confirm)

wn.listen()
wn.mainloop()
t.done()
