import random


class Throw:
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class PlayerType:
    AlwaysRock = 0
    AlwaysPaper = 1
    AlwaysScissors = 2
    Random = 3
    AlwaysCopy = 4
    AlwaysAnswer = 5
    AlwaysCycle = 6


class Result:
    TIE = 0
    LOSE = 1
    WIN = 2


class RockPaperScissorsGame:

    def __init__(self, p1, p2):
        self.players = []
        self.players.append(p1)
        self.players.append(p2)
        self.round = 0
        self.rounds = 9

    def start_game(self):
        for r in range(0, self.rounds):
            self.start_round()
        if self.players[0].score > self.players[1].score:
            self.players[0].give_win()
        elif self.players[0].score < self.players[1].score:
            self.players[1].give_win()
        self.players[0].reset()
        self.players[1].reset()

    def start_round(self):
        throw1 = self.players[0].throw()
        print("vs\t", end='')
        throw2 = self.players[1].throw()
        self.players[1].watched(throw1)
        self.players[0].watched(throw2)

        r = determine_winner(throw1, throw2)
        if r == Result.WIN:
            self.players[0].give_point()
        elif r == Result.LOSE:
            self.players[1].give_point()
        else:
            print(" -  Tie!")


class Player:

    def __init__(self, name, player_type):
        self.name = name
        self.player_type = player_type
        self.my_throws = []
        self.their_throws = []
        self.score = 0
        self.wins = 0

    def add_my_throw(self, throw):
        self.my_throws.append(throw)

    def give_point(self):
        self.score += 1
        print(" - ", self.name, "won the Round!")

    def give_win(self):
        self.wins += 1
        print(self.name, "wins the Game!", self.score, "out of 9")

    def reset(self):
        self.my_throws = []
        self.their_throws = []
        self.score = 0

    def watched(self, throw):
        self.their_throws.append(throw)

    def throw(self):
        throw = get_throw(self)
        print(get_throw_string(throw),"\t", end='')
        self.add_my_throw(throw)
        return throw


def determine_winner(throw1, throw2):
    if throw1 == Throw.ROCK:
        if throw2 == Throw.ROCK:
            return 0
        elif throw2 == Throw.PAPER:
            return 1
        elif throw2 == Throw.SCISSORS:
            return 2
    elif throw1 == Throw.PAPER:
        if throw2 == Throw.PAPER:
            return 0
        elif throw2 == Throw.SCISSORS:
            return 1
        elif throw2 == Throw.ROCK:
            return 2
    elif throw1 == Throw.SCISSORS:
        if throw2 == Throw.SCISSORS:
            return 0
        elif throw2 == Throw.ROCK:
            return 1
        elif throw2 == Throw.PAPER:
            return 2


def get_throw(player):
    if player.player_type == PlayerType.AlwaysRock:
        return Throw.ROCK
    elif player.player_type == PlayerType.AlwaysPaper:
        return Throw.PAPER
    elif player.player_type == PlayerType.AlwaysScissors:
        return Throw.SCISSORS
    elif player.player_type == PlayerType.Random:
        return random.randint(0, 2)
    elif player.player_type == PlayerType.AlwaysCopy:
        if not player.their_throws:
            return random.randint(0, 2)
        else:
            return player.their_throws[len(player.their_throws)-1]
    elif player.player_type == PlayerType.AlwaysAnswer:
        if not player.their_throws:
            return random.randint(0, 2)
        else:
            return get_answer(player.their_throws[len(player.their_throws)-1])
    elif player.player_type == PlayerType.AlwaysCycle:
        if not player.my_throws:
            return random.randint(0, 2)
        else:
            return get_answer(player.my_throws[len(player.my_throws) - 1])


def get_throw_string(throw):
    if throw == Throw.ROCK:
        return "Rock"
    elif throw == Throw.PAPER:
        return "Paper"
    elif throw == Throw.SCISSORS:
        return "Sciss"
    else:
        return "N/A"


def get_answer(throw):
    if throw == Throw.ROCK:
        return Throw.PAPER
    elif throw == Throw.PAPER:
        return Throw.SCISSORS
    elif throw == Throw.SCISSORS:
        return Throw.ROCK
