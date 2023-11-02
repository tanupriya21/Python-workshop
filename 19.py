score = 0
def increase_score(points):
    global score
    score += points

increase_score(10)
print("Score:", score)