high_score=0 #global high score
def update_high_score(score):
    global high_score
    if score>high_score:
        high_score=score
update_high_score(50)
print("high score:",high_score)