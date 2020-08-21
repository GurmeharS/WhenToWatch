'''
Each dictionary in the definitions list can include:
comparisons (required) - A list of dicts consisting of: (scope: <scope of the comparison>, stat: <statistic to be compared>, operator: <comparison operator>, value: <threshold value>)
    I.e. {
            scope: <player|team|game>,
            stat: <quarter|time_left|point_differential|points|fg_percentage|3pt_percentage|assists|rebounds|made_threes>, 
            operator: <gt|ge|eq|le|lt|ne>, 
            value: <integer|float>
        }
description - A verbal description/summary of the threshold
'''
THRESHOLD_DEFINITIONS = [
    {
        "comparisons": [
            {
                "scope": "game",
                "stat": "quarter",
                "operator": "gt",
                "value": 4
            }
        ],
        "description": "Game is in OT"
    },
    {
        "comparisons": [
            {
                "scope": "game",
                "stat": "quarter",
                "operator": "le",
                "value": 2
            },
            {
                "scope": "player",
                "stat": "points",
                "operator": "ge",
                "value": 30
            }
        ],
        "description": "Player has 30 or more points before/at halftime"
    }
]


def compare(stat, operator, value) -> bool:
    if operator == "gt":
        return stat > value
    elif operator == "ge":
        return stat >= value
    elif operator == "eq":
        return stat == value
    elif operator == "ne":
        return stat != value
    elif operator == "le":
        return stat <= value
    elif operator == "lt":
        return stat < value
    else:
        raise Exception(
            "The comparioson operator '{}' is not valid".format(operator))


"""
Returns: bool (True if all comparisons passed)
"""


def compare_stats(game, comparisons) -> int:
    for comparison in comparisons:
        met_threshold = False
        scope = comparison["scope"]
        stat = comparison["stat"]
        operator = comparison["operator"]
        value = comparison["value"]
        print(f'{scope}, {stat} {operator} {value}')
        if scope == "game":
            if not hasattr(game, stat):
                raise AttributeError(
                    "The game does not have attribute {}".format(stat))
            if stat == "time_left" and not game.compare_time_left(
                    operator, value):
                return False
            met_threshold = compare(getattr(game, stat), operator, value)
        elif scope == "team":
            for team in game.teams:
                if not hasattr(team, stat):
                    raise AttributeError(
                        "Team {} does not have attribute {}".format(team.name, stat))
                met_threshold = compare(getattr(team, stat), operator, value)
        elif scope == "player":
            qualified_players = []
            for player in game.teams[0].players + game.teams[1].players:
                if not hasattr(player, stat):
                    raise AttributeError(
                        "Player {} does not have attribute {}".format(player.name, stat))
                if compare(getattr(player, stat), operator, value):
                    qualified_players.append(player)
            if len(qualified_players) > 0:
                met_threshold = True
        if not met_threshold:
            return False
    return True
