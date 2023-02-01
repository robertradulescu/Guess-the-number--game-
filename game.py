import argparse
import random
from datetime import datetime


def check_Answer(user_Input, random_Number):
    return user_Input == random_Number


def pass_player(index, ignore_winner, ignore_loser):

    return index in ignore_winner or index in ignore_loser


def switch_index(index, length, ignore_winner, ignore_loser):
    while (True):
        if pass_player(index, ignore_winner, ignore_loser):
            index += 1
            continue

        elif (index+1 >= length):
            index = 0
            break
        else:
            index += 1
            break

    return index


def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--min', type=int, required=True)
    parser.add_argument('--max', type=int, required=True)
    parser.add_argument('--players', type=int, required=True)
    return parser.parse_args()

if __name__ == "__main__":
    while (True):

        args = args_parse()
        who_play = 0

        winners = dict()
        losers = dict()
        contor = args.players

        player_Score = []
        random_Number = []
        wrong_Guess = []

        for i in range(0, args.players):
            player_Score.insert(i, args.max/2)
            random_Number.insert(i, random.randint(args.min, args.max))
            wrong_Guess.insert(i, 0)
            print(i)

        while (True):
            who_play = switch_index(who_play, args.players,
                                    winners.keys(), losers.keys())

            user_Input = int(
                input('Guess the number!, is the turn of {}  '.format(who_play)))
            validate = check_Answer(user_Input, random_Number[who_play])

            if validate and player_Score[who_play] > 0:
                print("Congratulations , you won ! :) ", player_Score[who_play])
                winners[who_play] = player_Score[who_play]
                print(winners)
                contor -= 1
                if (contor != 0):
                    continue
                break

            elif random_Number[who_play] > user_Input and player_Score[who_play] > 0:
                wrong_Guess[who_play] += 1
                player_Score[who_play] -= (wrong_Guess[who_play]*2)
                print("HINT! The hidden number is bigger ")

            elif random_Number[who_play] < user_Input and player_Score[who_play] > 0:
                wrong_Guess[who_play] += 1
                player_Score[who_play] -= (wrong_Guess[who_play]*2)
                print("Hint! The hidden number is smaller ")

            else:
                print("You lost :(, but you can try again ")
                contor -= 1
                losers[who_play] = player_Score[who_play]
                if (contor != 0):
                    continue
                break

        current_datetime = datetime.now()
        str_current_datetime = str(current_datetime)
        file_name = str_current_datetime+"_number_guessing.txt"
        file = open(file_name, 'w')
        print("Leaderbord created : ", file.name)

        with open(file.name, 'w') as f:
            f.write("Leaderbord: \n")
            for key, value in winners.items():
                f.write('%s:%s\n' % (key, value))

        check = input(
            "Do you want to play again? Type Yes/No ")
        if check.lower() == "no":
            print("You lost :(, but you can try again ")
            break
