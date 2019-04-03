import csv
import numpy as np

global pos, team_pos
pos = {"ARS": 0, "BOU": 1, "BHA": 2, "BUR": 3, "CHE": 4,
       "CRY": 5, "EVE": 6, "HUD": 7, "LEI": 8, "LIV": 9,
       "MCI": 10, "MUN": 11, "NEW": 12, "SOU": 13, "STK": 14,
       "SWA": 15, "TOT": 16, "WAT": 17, "WBA": 18, "WHU": 19}

team_pos = ("ARS", "BOU", "BHA", "BUR", "CHE", "CRY", "EVE",
            "HUD", "LEI", "LIV", "MCI", "MUN", "NEW", "SOU",
            "STK", "SWA", "TOT", "WAT", "WBA", "WHU")


def strengthMatrix():
    # home_att, home_def, away_att, away_def
    strength = np.zeros((20, 4))
    av_home = 0
    av_away = 0

    # open csv file with results from every match played
    with open('results1.csv') as csvfile:
        results = csv.DictReader(csvfile)

        # loop through the table row by row
        for row in results:
            home_pos = pos[row["Home \\ Away"]]  # get position in array

            # loop through matches in row
            for away_team in pos:
                # team doesn't play against itself
                if away_team == row["Home \\ Away"]:
                    continue

                away_pos = pos[away_team]

                score = row[away_team]
                goal_home, goal_away = list(map(int, score.split("-")))
                strength[home_pos, 0] += goal_home/19
                strength[home_pos, 1] += goal_away/19
                strength[away_pos, 2] += goal_away/19
                strength[away_pos, 3] += goal_home/19

                av_home += goal_home / 380
                av_away += goal_away / 380

    strength[:, 0] = strength[:, 0] / av_home
    strength[:, 1] = strength[:, 1] / av_away
    strength[:, 2] = strength[:, 2] / av_away
    strength[:, 3] = strength[:, 3] / av_home

    return(strength, (av_home, av_away))


def LambdaMatrix(strength=None, av_goals=None):
    if strength is None or av_goals is None:
        strength, av_goals = strengthMatrix()

    lambdas = np.zeros((20, 20, 2))

    for home_pos in range(20):
        for away_pos in range(20):
            # team doesn't play against itself
            if away_pos == home_pos:
                continue

            # calculate lambda for
            home_lambda = av_goals[0] * \
                strength[home_pos, 0] * strength[away_pos, 3]
            away_lambda = av_goals[1] * \
                strength[home_pos, 1] * strength[away_pos, 2]

            lambdas[home_pos][away_pos][0] = home_lambda
            lambdas[home_pos][away_pos][1] = away_lambda

    return(lambdas)


if __name__ == "__main__":
    lambdas = LambdaMatrix()
    np.save("lambdas.npy", lambdas)
    print(lambdas)
