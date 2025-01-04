#Control Flow Challenges (Advanced)

'''
Challenge

Create a function that will rate movies. The function will split the ratings into different ranges 
and tell the user how the movie was based on the rating. 

'''

#Movie Review

def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  if rating > 5 and rating < 9:
    return "This one was fun."
  return "Outstanding!" 


print(movie_review(9))
print(movie_review(4))
print(movie_review(6))
