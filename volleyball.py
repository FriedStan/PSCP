"""[Midterm 2022] Volleyball"""


def score_board(team_a, team_b, result, current_set):
    """Make the score board"""
    winning_by = abs(team_a - team_b)
    win_team = ""
    if winning_by >= 2:
        result += "Set {}: A ({}) | B ({})\n".format(current_set,
                                                     team_a, team_b)
        if team_a > team_b:
            win_team = "A"
        elif team_b > team_a:
            win_team = "B"
        team_a, team_b = 0, 0
        current_set += 1
    return result, current_set, team_a, team_b, win_team


def set_checker(score_text, team_a, team_b, score_a, score_b):
    """Count the score in set 1-4"""
    result = ""
    win_team = ""
    current_set = 1
    for char in score_text:
        if char == "A":
            team_a += 1
        elif char == "B":
            team_b += 1
        if current_set < 5:
            if team_a >= 25 or team_b >= 25:
                result, current_set, team_a, team_b, win_team = score_board(
                    team_a, team_b, result, current_set)
        elif current_set == 5:
            if team_a >= 15 or team_b >= 15:
                result, current_set, team_a, team_b, win_team = score_board(
                    team_a, team_b, result, current_set)
        if win_team == "A":
            score_a += 1
        elif win_team == "B":
            score_b += 1
        win_team = ""
    return result, score_a, score_b, team_a, team_b, current_set


def score_counter(score_text):
    """Count the score"""
    team_a, team_b = 0, 0
    score_a, score_b = 0, 0
    result, score_a, score_b, team_a, team_b, current_set = set_checker(
        score_text, team_a, team_b, score_a, score_b)
    if 3 == score_a > score_b:
        result += "A won {0}:{1} set".format(score_a, score_b)
    elif 3 == score_b > score_a:
        result += "B won {1}:{0} set".format(score_a, score_b)
    else:
        result += "Set {}: A ({}) | B ({})\n".format(current_set,
                                                     team_a, team_b)
        result += "The game has not finished yet."
    print(result)


score_counter(str(input()).upper())
