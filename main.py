import os
import click
import glob
import time
import random
import pyttsx3

from config import d_symbols


# engine

engine = pyttsx3.init()
engine.setProperty('rate', 75)  # change speech rate
engine.setProperty("voice", "english")  # speech voice


def select_random(folder='pgns'):

    fns = list(glob.glob(os.path.join(folder, '*')))
    return random.choice(fns)



def pgn_to_list(fn):

    with open(fn, 'rt') as f:
        for l in f.readlines():
            if not l.startswith('1'):
                pass
            else:
                game = l.split('.')[1:]

    parsed = []
    for move in game:
        parsed.append(move.lstrip(' ').split(' ')[:-1])

    return parsed


def aloud(engine, s):

    engine.say(s)
    engine.runAndWait()


def read_move(engine, move, rate=75, gap=10):

    speech = []
    list(move)

    if (move == 'O-O') or (move == 'O-O-O'):
        speech.append(d_symbols[move])
    else:
        piecewise = list(map(lambda x: d_symbols.get(x, x), list(move)))
        speech = '-'.join(piecewise)

    aloud(engine, speech)


def read_pgn(fn, step=5):

    parsed = pgn_to_list(fn)

    for i, move in enumerate(parsed):
        print(move[0] + ' ' + move[1])
        read_move(engine, move[0])
        read_move(engine, move[1])
        if (i+1) % step == 0:
            input()

    engine.stop()


@click.command()
@click.option('--step', type=click.INT)
@click.option('--pgn', type=click.Path())
def cli(pgn, step):
    read_pgn(pgn, step=step)


if __name__ == '__main__':

    cli()
