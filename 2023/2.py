input = '''Game 1: 1 green, 4 blue; 1 blue, 2 green, 1 red; 1 red, 1 green, 2 blue; 1 green, 1 red; 1 green; 1 green, 1 blue, 1 red
Game 2: 2 blue, 2 red, 6 green; 1 red, 6 green, 7 blue; 10 green, 8 blue, 1 red; 2 green, 18 blue, 2 red; 14 blue, 3 green, 1 red; 8 green, 1 red, 9 blue
Game 3: 6 green, 5 blue, 9 red; 4 blue, 1 green, 13 red; 9 green, 14 red, 1 blue
Game 4: 14 green, 3 blue, 16 red; 20 red; 4 green, 2 red, 1 blue; 10 blue, 11 green, 18 red; 3 red, 3 blue, 6 green; 2 green, 18 red, 9 blue
Game 5: 5 green, 4 blue; 1 red, 3 blue, 2 green; 4 green, 2 red, 15 blue; 11 blue, 8 green, 4 red; 4 red, 3 green; 4 red, 3 green, 7 blue
Game 6: 6 blue, 10 green; 2 red, 6 green, 2 blue; 4 red, 4 blue, 1 green; 2 blue, 7 green, 2 red
Game 7: 14 green, 3 red, 2 blue; 5 blue, 3 green, 2 red; 1 green, 3 blue
Game 8: 7 red; 3 blue, 9 red, 1 green; 5 green, 5 blue, 7 red; 1 red, 2 blue
Game 9: 3 green, 4 blue, 1 red; 3 blue, 12 green, 18 red; 7 green, 9 red, 8 blue; 2 blue, 10 red, 12 green; 4 blue, 1 red, 1 green; 4 blue, 6 green, 6 red
Game 10: 2 blue, 4 green, 2 red; 7 green, 4 red; 5 red, 8 green
Game 11: 1 blue, 10 green, 15 red; 1 blue, 2 green, 2 red; 5 green, 10 blue, 8 red; 13 red, 7 blue; 1 red, 9 green, 4 blue; 9 blue, 9 red, 8 green
Game 12: 1 green, 10 red, 3 blue; 14 red, 1 green, 4 blue; 6 red, 3 green, 12 blue; 13 blue, 1 green, 18 red; 4 green, 14 red, 7 blue
Game 13: 1 red, 3 green; 2 green, 1 red, 5 blue; 1 blue; 1 green, 7 blue, 1 red; 1 red, 2 green, 7 blue
Game 14: 7 blue, 9 red, 1 green; 8 red, 2 blue; 11 red, 18 blue, 4 green; 2 blue, 3 green, 1 red; 1 green, 8 red, 9 blue; 2 blue, 8 red, 1 green
Game 15: 8 blue, 3 green, 15 red; 13 red, 10 blue; 2 red
Game 16: 1 green, 1 red; 1 blue, 2 green, 2 red; 1 blue, 4 red, 1 green; 3 green; 2 blue, 3 green, 4 red
Game 17: 1 green, 3 red, 14 blue; 1 red, 2 blue, 2 green; 3 red
Game 18: 1 red, 2 green, 8 blue; 2 blue, 14 red; 4 blue, 2 red, 2 green; 6 red
Game 19: 2 red, 11 blue, 18 green; 3 red, 6 green, 3 blue; 7 green, 1 red, 10 blue
Game 20: 10 red, 1 blue, 4 green; 4 green, 3 blue; 10 green, 13 red, 4 blue; 2 red, 7 green; 4 red, 3 blue, 5 green; 13 red, 1 green, 4 blue
Game 21: 20 red, 4 green, 5 blue; 10 red, 11 green, 4 blue; 1 red, 8 blue, 14 green; 11 green, 8 blue, 15 red; 8 blue, 2 green, 13 red
Game 22: 2 red, 11 blue, 4 green; 1 blue, 3 red, 6 green; 6 green, 1 red, 1 blue; 4 green, 7 blue, 3 red; 11 blue, 6 green, 4 red
Game 23: 6 green, 3 red, 1 blue; 17 green, 11 red; 1 red, 2 blue, 13 green; 13 green, 19 red
Game 24: 1 blue; 12 red, 1 blue; 1 red; 12 red, 1 green, 1 blue; 11 red, 1 blue; 12 red, 1 green
Game 25: 12 blue, 6 red, 3 green; 8 green, 14 blue; 11 green, 5 blue, 6 red; 4 red, 12 blue, 8 green
Game 26: 15 red, 13 green, 9 blue; 9 blue, 8 green, 7 red; 2 green, 6 red, 3 blue; 1 blue, 7 red, 3 green; 13 blue, 4 green, 18 red
Game 27: 9 blue, 5 red; 15 red, 12 blue, 3 green; 12 red, 12 blue, 1 green
Game 28: 18 red, 4 green; 4 green, 6 red; 1 blue, 6 green, 19 red; 9 green, 17 red; 4 green, 5 blue, 18 red
Game 29: 7 green, 6 red, 6 blue; 6 blue, 19 red, 4 green; 4 green, 4 blue, 13 red; 5 blue, 15 red, 10 green; 2 green, 6 blue, 5 red; 8 red, 10 green, 6 blue
Game 30: 1 green, 13 red, 12 blue; 1 red, 2 blue; 11 blue, 1 red, 1 green
Game 31: 8 green, 18 blue, 17 red; 4 red, 8 green, 6 blue; 9 blue, 7 green; 3 green, 1 blue, 12 red; 5 red, 10 blue, 11 green
Game 32: 17 red, 17 green, 7 blue; 18 red, 16 green; 1 blue
Game 33: 16 blue, 3 red; 9 blue, 1 red, 2 green; 3 green, 7 blue; 1 green, 4 red; 3 green, 1 red, 8 blue; 5 blue
Game 34: 5 blue, 8 red, 1 green; 9 red, 10 blue, 7 green; 1 green, 14 blue; 8 blue, 4 red, 10 green; 15 blue, 8 green, 7 red; 2 red, 6 green, 3 blue
Game 35: 13 red, 9 blue; 7 blue, 16 red, 10 green; 4 red, 6 blue; 3 blue, 12 green, 7 red; 8 blue, 6 red; 10 blue, 3 green, 2 red
Game 36: 1 blue, 9 red, 2 green; 11 red, 3 blue, 2 green; 2 green, 6 red; 8 green, 11 red, 3 blue; 4 green, 7 blue, 11 red; 9 green, 8 red, 2 blue
Game 37: 8 green, 3 blue, 4 red; 14 blue, 10 green, 3 red; 19 green, 2 blue, 7 red
Game 38: 2 green, 3 red, 3 blue; 3 green, 9 red; 13 blue, 8 red; 6 red, 5 green, 13 blue
Game 39: 8 red, 5 blue; 4 green, 5 blue, 3 red; 18 red, 2 green, 6 blue; 2 green, 5 blue, 17 red; 1 green, 2 red; 5 green, 6 blue
Game 40: 12 red, 4 blue, 1 green; 11 green, 20 blue, 4 red; 10 blue, 4 red
Game 41: 2 green, 2 blue; 2 red, 2 green; 2 green, 2 blue, 10 red
Game 42: 6 green, 3 blue; 2 red, 2 green, 1 blue; 3 blue, 5 green, 6 red; 6 red; 1 blue, 6 green, 12 red
Game 43: 1 blue, 4 green; 1 blue; 2 blue, 8 red, 2 green; 2 blue, 1 red, 4 green; 1 blue, 4 red, 4 green; 4 green, 7 red
Game 44: 8 green, 9 red; 1 red, 2 blue, 13 green; 4 blue, 8 green, 17 red; 13 red, 13 green; 1 red, 9 green; 19 red, 3 green, 3 blue
Game 45: 10 blue, 2 red, 1 green; 6 green, 5 red, 8 blue; 3 blue, 1 red; 4 green, 10 blue, 4 red
Game 46: 3 red, 8 blue; 6 blue, 7 green, 6 red; 6 green, 1 blue, 7 red; 8 red, 1 green, 5 blue; 9 red, 12 blue, 10 green; 7 green, 5 red, 1 blue
Game 47: 5 red; 2 blue, 2 green, 5 red; 3 green, 7 red; 14 red, 3 green, 2 blue
Game 48: 7 blue, 12 green, 2 red; 11 green, 10 blue, 1 red; 1 red, 13 blue, 2 green; 14 green, 2 red, 9 blue; 2 red, 12 green, 3 blue; 2 red, 7 blue
Game 49: 4 green, 5 blue; 9 blue; 10 blue, 5 green, 2 red; 10 blue, 2 red, 2 green; 1 red, 1 green, 4 blue; 2 blue
Game 50: 2 red, 2 blue, 7 green; 7 red, 9 green, 3 blue; 5 red, 10 green
Game 51: 15 red, 9 blue, 4 green; 5 red, 2 blue, 15 green; 4 blue, 3 green, 20 red; 12 green, 1 red, 10 blue; 10 green, 5 blue, 13 red; 9 red, 10 green, 11 blue
Game 52: 3 blue, 12 green, 1 red; 6 green; 1 red, 8 green; 1 blue, 1 green, 1 red
Game 53: 10 green, 7 red, 12 blue; 9 blue, 6 green, 2 red; 8 green, 5 blue, 5 red; 7 blue, 16 green, 11 red; 6 red, 8 blue, 13 green
Game 54: 10 green, 6 blue, 3 red; 6 green, 2 red, 8 blue; 9 blue, 11 green, 2 red; 10 green, 1 blue, 3 red
Game 55: 4 blue, 1 red; 3 red, 7 blue; 12 red, 4 green, 8 blue; 3 green, 5 blue, 1 red; 13 blue, 12 red, 1 green
Game 56: 12 blue, 15 green; 1 green, 7 red, 11 blue; 5 green, 9 blue, 1 red; 8 red, 5 green, 6 blue
Game 57: 4 green, 11 blue, 18 red; 14 blue, 14 red, 16 green; 7 red, 15 green, 3 blue; 18 red, 20 green, 8 blue; 12 blue, 9 red, 16 green
Game 58: 10 blue, 9 green, 8 red; 13 green, 6 blue, 8 red; 8 green, 4 red; 4 blue, 1 red, 18 green; 7 red, 10 green, 10 blue; 15 blue, 10 green, 3 red
Game 59: 17 green, 2 blue, 2 red; 2 blue, 1 red, 8 green; 14 green, 1 red, 1 blue; 15 green, 3 blue, 2 red; 2 blue, 8 green, 1 red; 1 blue, 1 red, 8 green
Game 60: 1 green, 1 blue, 1 red; 4 blue, 3 red, 2 green; 13 green; 2 blue, 2 red, 8 green; 4 red, 12 green, 4 blue; 4 green, 4 blue, 4 red
Game 61: 3 blue, 7 red; 5 blue, 8 red, 1 green; 1 blue, 8 red; 10 blue, 2 red, 1 green; 1 green, 5 blue, 2 red
Game 62: 10 red, 2 green; 8 blue, 7 red, 2 green; 4 green, 2 blue, 10 red
Game 63: 1 green, 3 blue, 5 red; 6 green, 5 blue, 2 red; 3 blue, 7 red
Game 64: 6 red, 20 blue; 4 red, 3 blue, 2 green; 3 green, 19 blue, 6 red; 2 green, 6 blue, 3 red; 13 blue, 5 green, 5 red
Game 65: 6 red, 9 blue, 20 green; 6 red, 16 green, 4 blue; 12 red, 6 green, 5 blue
Game 66: 2 blue, 5 red, 4 green; 13 blue, 2 green; 1 green, 6 blue
Game 67: 4 green, 5 blue, 2 red; 1 red, 14 blue, 6 green; 1 green, 14 red, 5 blue; 18 red, 16 blue; 15 blue, 8 red, 18 green; 1 green, 18 red, 6 blue
Game 68: 1 blue, 9 red, 7 green; 7 red, 1 blue, 6 green; 5 green, 1 blue, 8 red
Game 69: 12 green, 3 blue, 4 red; 9 green, 8 red, 7 blue; 4 blue, 5 red, 10 green; 4 red, 5 green, 7 blue; 9 green, 4 red, 2 blue; 3 green, 13 blue, 1 red
Game 70: 9 red, 1 green, 8 blue; 11 green, 13 blue, 12 red; 3 blue, 5 green, 8 red; 1 red, 14 blue
Game 71: 10 blue; 2 green, 8 blue, 9 red; 5 red, 1 blue
Game 72: 3 green, 5 blue, 5 red; 1 blue, 1 red, 2 green; 4 red, 4 blue, 1 green; 5 blue, 4 red, 1 green; 6 blue, 3 green, 5 red; 5 blue, 1 red, 4 green
Game 73: 3 red, 1 green, 1 blue; 7 green, 2 red, 1 blue; 2 green, 1 blue, 3 red; 1 red, 4 green, 1 blue; 3 red, 5 green
Game 74: 5 blue, 1 red, 4 green; 3 red, 2 green; 4 red, 6 blue; 2 red, 2 blue; 1 green, 4 red, 8 blue; 5 blue, 4 red
Game 75: 3 red, 5 blue, 3 green; 9 green, 6 blue, 7 red; 2 green, 3 red, 12 blue; 14 green, 4 blue, 10 red
Game 76: 1 blue, 7 red, 1 green; 6 red, 1 blue, 2 green; 4 red, 2 green; 3 red, 1 blue; 16 red, 1 green
Game 77: 3 red, 10 blue, 1 green; 4 red, 7 blue, 3 green; 7 blue, 6 green, 7 red; 5 green, 15 blue, 7 red; 12 green, 5 red
Game 78: 6 red, 10 blue, 15 green; 6 green, 11 red, 4 blue; 6 blue, 8 red; 4 blue, 7 red, 2 green; 11 green, 7 red, 11 blue; 3 blue, 14 green, 6 red
Game 79: 14 red, 6 green, 4 blue; 13 red, 6 blue; 6 red, 13 green, 4 blue
Game 80: 8 red, 2 blue, 8 green; 6 red, 10 green, 4 blue; 3 red, 9 green; 2 green, 8 blue, 7 red; 7 blue, 3 red, 11 green; 1 red, 12 green, 8 blue
Game 81: 9 red, 4 blue, 11 green; 1 blue, 4 red, 2 green; 5 red; 3 blue, 2 red, 2 green; 14 red, 12 green
Game 82: 5 green; 2 blue; 2 red; 1 blue, 2 red, 11 green; 8 green, 2 red, 1 blue
Game 83: 3 green, 7 red, 6 blue; 7 red, 7 green, 11 blue; 7 blue, 13 green, 7 red; 12 blue, 10 red, 2 green; 1 green, 11 red, 7 blue; 12 blue, 9 red, 9 green
Game 84: 5 blue, 1 green; 16 green, 4 blue, 8 red; 7 red, 5 blue, 16 green
Game 85: 9 green, 20 blue, 7 red; 19 blue, 14 red, 2 green; 10 green, 2 red, 10 blue
Game 86: 1 green, 3 red, 5 blue; 9 red, 2 blue, 6 green; 8 green, 14 red, 3 blue; 18 green, 2 blue, 7 red; 2 blue, 10 red, 14 green; 17 green, 4 blue, 12 red
Game 87: 4 green, 8 red, 13 blue; 7 red, 13 blue, 4 green; 1 green, 8 blue
Game 88: 9 blue, 11 red; 5 green, 7 blue, 12 red; 10 red, 2 green, 1 blue; 2 blue, 5 red, 5 green; 7 red, 6 green, 9 blue; 1 green, 10 red, 5 blue
Game 89: 7 red, 2 green, 1 blue; 1 blue, 2 green; 6 red, 1 green; 7 red, 1 blue; 3 green, 3 red
Game 90: 8 blue, 2 red, 3 green; 9 green, 4 blue, 3 red; 7 green, 11 blue, 2 red; 13 green, 12 blue, 8 red; 10 blue, 2 green; 5 green, 1 red, 9 blue
Game 91: 2 red, 2 green, 4 blue; 5 blue, 2 red, 16 green; 11 green; 3 blue, 2 red, 8 green; 4 green, 3 blue
Game 92: 8 red, 12 blue, 3 green; 11 red, 10 blue, 6 green; 14 red, 8 green, 14 blue
Game 93: 3 green, 2 red, 3 blue; 3 green, 3 red, 1 blue; 2 blue, 16 red, 3 green; 2 green; 5 green, 2 blue, 2 red
Game 94: 5 red, 2 green; 9 red, 3 blue; 2 green, 2 blue, 5 red; 3 blue, 8 red, 2 green; 8 red, 1 blue, 1 green
Game 95: 3 blue, 4 green, 7 red; 7 red, 1 green, 15 blue; 6 blue, 2 green, 7 red
Game 96: 2 blue, 1 red, 6 green; 7 blue, 8 green; 1 red, 7 green; 2 green, 14 blue, 1 red; 3 blue, 1 red, 7 green; 4 blue, 11 green
Game 97: 2 red, 9 blue, 8 green; 3 green, 5 blue; 6 green, 1 red, 9 blue; 2 red, 13 green, 1 blue; 2 green, 2 red, 2 blue
Game 98: 2 blue, 1 green, 1 red; 4 blue, 5 red, 1 green; 4 blue, 3 red, 2 green
Game 99: 17 red, 2 blue, 4 green; 4 green, 8 red, 6 blue; 5 red
Game 100: 6 red, 4 green; 3 red, 2 blue, 9 green; 1 blue, 5 green, 14 red; 1 blue, 2 red, 2 green; 9 red, 1 blue, 14 green; 2 blue, 11 green, 8 red'''

# input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

lines = input.split("\n")
res = 0
for game in lines:
    possible = True
    gameId = int(game.split(':')[0].split()[1])
    print(gameId)
    sets = game.split(':')[1].split("; ")
    h_blue = 0
    h_red = 0
    h_green = 0
    for set in sets:
        dice = {
            "blue": 0,
            "red": 0,
            "green": 0}
        reveals = set.split(", ")
        for reveal in reveals:
            col = reveal.split()[1]
            amount = reveal.split()[0]
            dice[col] += int(amount)
        print(dice)
        if dice["blue"] > h_blue:
            h_blue = dice["blue"]
        if dice["red"] > h_red:
            h_red = dice["red"]
        if dice["green"] > h_green:
            h_green = dice["green"]

    #         possible = False
    # if possible:
    #     res += gameId
    res += h_green*h_blue*h_red
print(res)
