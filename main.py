# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb
#-----game configuration----
spot_color = "pink"
size = 2
shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 3
counter_interval = 1000   #1000 represents 1 second
timer_up = False
colors = ["blue","green","yellow","purple","orange"]
leaderboard_file_name = "leaderboard.txt"
player_name = input("What is your name? ")
#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(shape)
spot.shapesize(size)
spot.fillcolor(spot_color)

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(75,175)
score_writer.showturtle()
score_writer.pendown()

counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(100,175)
counter.showturtle()
counter.pendown()
#-----game functions--------
# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)
  leaderboard_writer = trtl.Turtle()
  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)


def add_color():
  spot.fillcolor(rand.choice(colors))
  spot.stamp()
  spot.fillcolor(spot_color)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 



def update_score():
  score_writer.clear()
  global score
  score += 1
  score_writer.write(score, font=font_setup)


def change_position():
  new_xpos = rand.randint(-200,200)
  new_ypos = rand.randint(-200,200)
  spot.penup()
  spot.hideturtle()
  spot.goto(new_xpos,new_ypos)
  spot.pendown()
  spot.showturtle()
 
def spot_clicked(x,y):
  global timer_up
  if timer_up == False:
     update_score()
     change_position()
     add_color()
  else:
    spot.hideturtle()
  

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.bgcolor("red")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()