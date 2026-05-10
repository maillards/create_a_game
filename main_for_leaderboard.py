# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb
#game config
score = 0
#placeholder to say that the game has finsihed
#after code for game is plugged in this should be removed/put into code where game is finished
game_finished = True


font_setup = ("Arial", 20, "normal")
leaderboard_file_name = "leaderboard.txt"
#sias codev
player_name = input("What is your name? ")
#sias code^


score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(75,175)
score_writer.showturtle()
score_writer.pendown()


# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  global score

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)
  leaderboard_writer = trtl.Turtle()
  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, score_writer, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, score_writer, score)

def update_score():
  score_writer.clear()
  global score
  score += 1
  score_writer.write(score, font=font_setup)

#add game code here







wn = trtl.Screen()
if game_finished == True:
  manage_leaderboard()
  
wn.mainloop()
