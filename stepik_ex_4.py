n = int(input())

games = []
teams = dict()


def fill_games():
    for i in range(n):
        entry = input().split(';')
        game = dict()
        game[entry[0]] = entry[1]
        game[entry[2]] = entry[3]
        games.append(game)
        if not teams.__contains__(entry[0]):
            teams[entry[0]] = []
            teams[entry[0]].append(0)
            teams[entry[0]].append(0)
            teams[entry[0]].append(0)
            teams[entry[0]].append(0)
            teams[entry[0]].append(0)
        if not teams.__contains__(entry[2]):
            teams[entry[2]] = []
            teams[entry[2]].append(0)
            teams[entry[2]].append(0)
            teams[entry[2]].append(0)
            teams[entry[2]].append(0)
            teams[entry[2]].append(0)


def fill_results():
    for game1 in games:
        counter = 0
        first_team = ''
        first_result = 0
        second_team = ''
        second_result = 0
        for k, v in game1.items():
            if counter == 0:
                first_team = k
                first_result = int(v)
                counter = 1
            else:
                second_team = k
                second_result = int(v)
                counter = 0
        if first_result > second_result:
            left_win(first_team, second_team)
        elif first_result < second_result:
            left_win(second_team, first_team)
        else:
            draw(first_team, second_team)
            increment_draw_points(first_team)
            increment_draw_points(second_team)


def draw(first_team, second_team):
    increment_game(first_team)
    increment_game(second_team)
    increment_draw(first_team)
    increment_draw(second_team)


def left_win(winner, loser):
    increment_game(winner)
    increment_win(winner)
    increment_win_points(winner)
    increment_game(loser)
    increment_lose(loser)


def increment_draw(second_team):
    value = teams[second_team][2]
    value += 1
    teams[second_team][2] = value


def increment_win_points(team):
    value = teams[team][4]
    value += 3
    teams[team][4] = value


def increment_draw_points(team):
    value = teams[team][4]
    value += 1
    teams[team][4] = value


def increment_lose(team):
    value = teams[team][3]
    value += 1
    teams[team][3] = value


def increment_win(team):
    value = teams[team][1]
    value += 1
    teams[team][1] = value


def increment_game(team):
    value = teams[team][0]
    value += 1
    teams[team][0] = value


fill_games()
fill_results()
for k, v in teams.items():
    print('{}:{} {} {} {} {}'.format(k, v[0], v[1], v[2], v[3], v[4]))
