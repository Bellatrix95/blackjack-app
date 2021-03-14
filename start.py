from classes.Game import Game
from argparse import ArgumentParser


def parseArgs():
        parser = ArgumentParser()
        parser.add_argument("-s", "--simulations", help = "Number of Blackjack simulations.", dest = "simulations")
        args = parser.parse_args()
        return args


if __name__=='__main__':
    args = parseArgs()
    if args.simulations is not None:
        game = Game(int(args.simulations))
    else: 
        game = Game()

    game.start_round()

    print(game)