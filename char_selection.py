import turtle as t

bird = 'bird.png'
lion = "lion.png"
cat = "cat.png"
fish = 'fish.png'
boy = 'boy.png'
robot = 'robot.png'
girl = 'girl.png'



wn = t.Screen()
wn.bgpic("start.jpg")

wn.addshape(lion)
wn.addshape(bird)
wn.addshape(cat)
wn.addshape(fish)
wn.addshape(boy)
wn.addshape(robot)
wn.addshape(girl)

button_img = "button.png"
wn.addshape(button_img)

choose = 0
char =[girl, lion, cat, fish, boy, robot, bird]
lvl = 0

usr = t.Turtle()
usr.hideturtle()
usr.left(90)
usr.shape(char[choose])
usr.showturtle()

button = t.Turtle()
button.speed(50)
button.hideturtle()
button.left(90)
button.shape(button_img)
button.penup()
button.goto(0, -150)
button.showturtle()

txt = t.Turtle()
txt.speed(50)
txt.hideturtle()
txt.penup()
txt.goto(0, 170)
txt.write("Choose your character!", align="center", font=("Arial", 16, 'bold'))
txt.goto(0, 150)
txt.write("USE LEFT RIGHT ARROWS", align="center", font=("Arial", 16, 'bold'))

chosen = False

def plus():
  global choose
  if not chosen:
    choose += 1
    if choose>6:
      choose = 0
    usr.shape(char[choose])

def minus():
  global choose
  if not chosen:
    choose -= 1
    if choose<0:
      choose = 6
    usr.shape(char[choose])
  
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
