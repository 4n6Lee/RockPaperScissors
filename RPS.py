from RockPaperScissorsGame import *

Rocky = Player("Rocky", PlayerType.AlwaysRock)
Pappy = Player("Pappy", PlayerType.AlwaysPaper)
Sissy = Player("Sissy", PlayerType.AlwaysScissors)
Randy = Player("Randy",PlayerType.Random)
Kitty = Player("Kitty",PlayerType.AlwaysCopy)
Andy = Player("Andy",PlayerType.AlwaysAnswer)
Cecil = Player("Cecil",PlayerType.AlwaysCycle)

list = []
list.append(Randy)
list.append(Andy)
list.append(Cecil)

for l in list:
    for m in list:
        if l == m:
            continue
        else:
            for x in range(0, 100):
                theGame = RockPaperScissorsGame(l, m)
                theGame.start_game()

print(" ")
print("Rocky has ",Rocky.wins," Wins")
print("Pappy has ",Pappy.wins," Wins")
print("Sissy has ",Sissy.wins," Wins")
print("Randy has ",Randy.wins," Wins")
print("Kitty has ",Kitty.wins," Wins")
print("Andy has ",Andy.wins," Wins")
print("Cecil has ",Cecil.wins," Wins")
