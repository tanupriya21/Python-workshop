player_stats={
    "name":"player1",
    "score":100,
    "level":5
}
def display_player_info():
    print(f"name:{player_stats['name']}")
    print(f"score:{player_stats['score']}")
    print(f"level:{player_stats['level']}")

display_player_info()