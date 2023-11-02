def game_round():
    score=0 #local score
    def increase_score(points):
        nonlocal score
        score+=points
    increase_score(10)
    return score
round_score=game_round()
print("round score:",round_score)