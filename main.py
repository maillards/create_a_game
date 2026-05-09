
import turtle

# screen setup
screen = turtle.Screen()
screen.title("Falling Platforms Game")
screen.setup(width=800, height=600)
screen.tracer(0)
# starting gif
screen.bgpic("background.gif")
# text
title_writer = turtle.Turtle()
title_writer.hideturtle()
title_writer.penup()

title_writer.goto(0, 180)
title_writer.color("black")
title_writer.write("FALLING PLATFORMS", align="center", font=("Times New Roman", 36, "bold"))

title_writer.goto(0, 120)
title_writer.color("black")
title_writer.write("survive as long as you can!", align="center", font=("Times New Roman", 16, "bold"))

title_writer.goto(0, -200)
title_writer.color("black")
title_writer.write("click OK below to choose your speed", align="center", font=("Times New Roman", 14, "normal"))

screen.update()
# speed
SPEED_SETTINGS = {
    "easy":   {"fps": 30, "platform_fall": 2, "hazard_speed": 3, "platform_timer": 5.0},
    "medium": {"fps": 45, "platform_fall": 4, "hazard_speed": 6, "platform_timer": 3.5},
    "hard":   {"fps": 60, "platform_fall": 6, "hazard_speed": 9, "platform_timer": 2.0},
}

settings = {}
speed_label = ""

def choose_speed():
    global speed_label

    raw = screen.textinput("Difficulty", "Choose speed: easy / medium / hard")

    if raw is None:
        choice = "medium"
    else:
        choice = raw.strip().lower()

    if choice not in SPEED_SETTINGS:  
        choice = "medium"              

    speed_label = "Speed: " + choice.capitalize()
    settings.update(SPEED_SETTINGS[choice])  

    title_writer.clear()
    screen.bgpic("nopic")
    print(speed_label + " → " + str(settings))
# run
choose_speed()
turtle.done()

