#Functions Challenges (Intermediate)

'''
Challenge 
Create a function which calculates the percentage of games won. In order to do this, we will need to know how 
many total games there were and divide the number of wins by the total number of games. Make sure to return the
result as a percentage (in the range of 0 to 100). 

'''

#Win Percentage

def win_percentage(wins, losses):
  total_games = wins + losses
  win_ratio = wins / total_games
  percentage = win_ratio * 100
  return percentage

print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100