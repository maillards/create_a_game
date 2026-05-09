#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple (3).gif" # Store the file name of your shape
bg_image = "background.png"
xcor = 0

wn = trtl.Screen()
wn.setup(width=390, height=390)
wn.bgpic(bg_image)
wn.addshape(apple_image) # Make the screen aware of the new file

letterbank = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letter = ''
cleared = True

apps = []
lets = []

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

def make_apple():
  apple = trtl.Turtle()
  wn.tracer(0)
  apple.penup()
  apple.setheading(90)
  apple.goto(xcor, 150)
  return apple

def draw_apple(active_apple):
  global xcor
  active_apple.shape(apple_image)
  active_apple.showturtle()
  wn.update()

def fall(apple):
  global cleared 
  wn.tracer(1)
  apple.goto(apple.xcor(),0)
  apple.clear()
  apple.hideturtle()
  cleared = True

def fall1():
  fall(apps[0])

def fall2():
  fall(apps[1])

def fall3():
  fall(apps[2])

def fall4():
  fall(apps[3])

def fall5():
  fall(apps[4])

def write_letter(active_apple, letter):
  active_apple.backward(40)
  active_apple.setheading(0)
  active_apple.backward(5)
  active_apple.color("white")
  active_apple.write(letter, align='center', font=("Comic Sans MS", 50, "bold"))
  active_apple.forward(5)
  active_apple.setheading(90)
  active_apple.forward(40)

def rand_letter():
  index = rand.randint(0,len(letterbank) - 1)
  letter = letterbank.pop(index)
  return letter

def rand_xcor():
  xcor = rand.randint(-180,180)
  return xcor

#-----function calls-----

wn.listen()

for i in range(5):
  apple = make_apple()
  xcor = rand_xcor()
  draw_apple(apple)
  
  letter = rand_letter()
  
  apps.append(apple)
  lets.append(letter)
  write_letter(apple, letter)

print(apps)
print(lets)

wn.onkeypress(fall1,lets[0])
wn.onkeypress(fall2,lets[1])
wn.onkeypress(fall3,lets[2])
wn.onkeypress(fall4,lets[3])
wn.onkeypress(fall5,lets[4])

wn.mainloop()