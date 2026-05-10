import turtle
import time

# SETUP
screen = turtle.Screen()
screen.title("Falling Platforms Game")
screen.setup(width=800, height=600)
screen.tracer(0)

# heart images
screen.register_shape("fullheart.gif")
screen.register_shape("emptyheart.gif")

# starting screen
screen.bgpic("background.gif")

# title text
title_writer = turtle.Turtle()
title_writer.hideturtle()
title_writer.penup()

title_writer.goto(0, 180)
title_writer.color("black")
title_writer.write("FALLING PLATFORMS", align="center", font=("Times", 36, "bold"))

title_writer.goto(0, 120)
title_writer.color("black")
title_writer.write("survive as long as you can!", align="center", font=("Times", 16, "normal"))

title_writer.goto(0, -200)
title_writer.color("black")
title_writer.write("click OK to choose your speed", align="center", font=("Times", 14, "normal"))

screen.update()

# speed
SPEED_SETTINGS = {
    "easy":   {"fps": 30, "platform_fall": 2, "hazard_speed": 3, "platform_timer": 5.0, "lives": 7},
    "medium": {"fps": 45, "platform_fall": 4, "hazard_speed": 6, "platform_timer": 3.5, "lives": 3},
    "hard":   {"fps": 60, "platform_fall": 6, "hazard_speed": 9, "platform_timer": 2.0, "lives": 1},
}

settings = {}
speed_label = ""

# constants
BOTTOM_EDGE = -280

# lives/score count
lives = 0
score = 0
game_over = False

# player (just a trial not the real player)
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.shapesize(1.5, 1.5)
player.penup()
player.goto(0, 0)
player.vy = 0

# list of platforms (vera's code here)
platforms = []

# heart turtle list
heart_turtles = []

# hud writer
hud = turtle.Turtle()
hud.hideturtle()
hud.penup()
hud.color("black")


# selecting the speed
def choose_speed():
    global speed_label, lives

    raw = screen.textinput("Difficulty", "Choose speed: easy / medium / hard")

    if raw is None:
        choice = "easy"
    else:
        choice = raw.strip().lower()

    if choice not in SPEED_SETTINGS:
        choice = "easy"

    speed_label = "Speed: " + choice.capitalize()
    settings.update(SPEED_SETTINGS[choice])
    lives = settings["lives"]

    title_writer.clear()
    screen.bgpic("nopic")
    screen.bgcolor("skyblue")


# HEARTSSS
def create_heart_turtles():
    for i in range(settings["lives"]):
        h = turtle.Turtle()
        h.shape("fullheart.gif")          # ← fixed
        h.penup()
        h.goto(-380 + (i * 40), 260)
        heart_turtles.append(h)


def draw_hud():
    for i in range(len(heart_turtles)):
        if i < lives:
            heart_turtles[i].shape("fullheart.gif")     # ← fixed
        else:
            heart_turtles[i].shape("emptyheart.gif")    # ← fixed

    hud.clear()
    hud.goto(-380 + (settings["lives"] * 40) + 10, 255)
    hud_text = "Score: " + str(score) + "   " + speed_label
    hud.write(hud_text, font=("Arial", 14, "bold"))


# death + game over
def check_fallen_off_screen():
    if player.ycor() < BOTTOM_EDGE:
        handle_death()


def handle_death():
    global lives, game_over

    lives -= 1

    player.color("red")
    screen.update()
    time.sleep(0.4)

    if lives <= 0:
        game_over = True
        show_game_over_screen()
    else:
        show_lost_life_message()
        respawn_player()


def respawn_player():
    if len(platforms) > 0:
        sorted_platforms = sorted(platforms, key=lambda p: p.ycor(), reverse=True)
        highest = sorted_platforms[0]
        player.goto(highest.xcor(), highest.ycor() + 25)
    else:
        player.goto(0, 0)

    player.color("blue")
    player.vy = 0
    player.showturtle()

    start_y = player.ycor() + 80
    player.goto(player.xcor(), start_y)
    for step in range(8):
        player.sety(player.ycor() - 10)
        screen.update()
        time.sleep(0.03)


def show_lost_life_message():
    hud.clear()
    hud.goto(0, 0)
    message = "Lives left: " + str(lives) + " / " + str(settings["lives"])
    hud.write(message, align="center", font=("Arial", 20, "bold"))
    screen.update()
    time.sleep(1)
    hud.clear()


def show_game_over_screen():
    screen.bgcolor("black")
    hud.color("white")
    hud.goto(0, 80)
    hud.write("GAME OVER", align="center", font=("Arial", 36, "bold"))
    hud.goto(0, 20)
    score_msg = "Final Score: " + str(score)
    hud.write(score_msg, align="center", font=("Arial", 24, "normal"))
    hud.goto(0, -40)
    hud.write("Press ESC to quit", align="center", font=("Arial", 16, "normal"))
    screen.update()


screen.listen()
screen.onkey(turtle.bye, "Escape")


# the loop for the main game
def main_game_loop():
    while not game_over:
        screen.tracer(0)

        # teammates' functions go here:
        # move_platforms()
        # move_player()
        # move_coins()

        check_fallen_off_screen()
        draw_hud()

        screen.update()
        time.sleep(1 / settings["fps"])


# test platform (delete when vera adds real ones)
fake = turtle.Turtle()
fake.shape("square")
fake.shapesize(1, 6)
fake.color("green")
fake.penup()
fake.goto(0, -100)
platforms.append(fake)

choose_speed()
create_heart_turtles()
main_game_loop()
turtle.done()