#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    game_1 = Game("Skribbl.io")
    game_2 = Game("Codenames")
    player_1 = Player("Ja'Vonn")
    player_2 = Player("Sarah")
    result_1 = Result(player_1, game_1, 8)
    result_2 = Result(player_1, game_2, 3000)
    result_3 = Result(player_2, game_1, 10)
    result_4 = Result(player_2, game_2, 3050)
    result_5 = Result(player_2, game_2, 5000)

    ipdb.set_trace()
