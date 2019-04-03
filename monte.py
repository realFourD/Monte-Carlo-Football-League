import numpy as np
import sys
import os
from StrengthCalc import LambdaMatrix, pos, team_pos


global team_pos, pos
lambdas = LambdaMatrix()


def season(lambdas):
    # won, draw, lost, for, against, points
    table = np.zeros((20, 6), dtype=int)

    # max goals score in the season
    max_game = [0, 0, 0]

    for home_pos in range(20):
        for away_pos in range(20):
            # team doesn't play against itself
            if away_pos == home_pos:
                continue

            # get lambdas
            home_lambda = lambdas[home_pos][away_pos][0]
            away_lambda = lambdas[home_pos][away_pos][1]

            # random sample distribution
            home_goal = np.random.poisson(home_lambda)
            away_goal = np.random.poisson(away_lambda)

            # update table array
            if home_goal > away_goal:
                table[home_pos][5] += 3
                table[home_pos][0] += 1
                table[away_pos][2] += 1

            elif home_goal == away_goal:
                table[home_pos][5] += 1
                table[home_pos][1] += 1
                table[away_pos][5] += 1
                table[away_pos][1] += 1
            elif home_goal < away_goal:
                table[away_pos][5] += 3
                table[away_pos][0] += 1
                table[home_pos][2] += 1

            table[home_pos][3] += home_goal
            table[home_pos][4] += away_goal
            table[away_pos][3] += away_goal
            table[away_pos][4] += home_goal

    return(table)


if __name__ == "__main__":
    if len(sys.argv) > 1 and int(sys.argv[1]) > 0:
        k = int(sys.argv[1])
    else:
        k = 1
    print("Interations:", k)

    # array for results organized by team
    output = np.memmap("output_{}.npy".format(k),
                       dtype='int', mode='w+', shape=(k, 20, 6))

    for j in range(k):
        # get season results and store output
        output[j, :, :] = season(lambdas)

        if j % 500 == 0:
            print("Completed:",j)
