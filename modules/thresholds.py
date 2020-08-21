'''
Each dictionary in the definitions list can include:
comparisons (required) - A list of dicts consisting of: (scope: <scope of the comparison>, stat: <statistic to be compared>, operator: <comparison operator>, value: <threshold value>)
    I.e. {
            scope: <player|team|game>,
            stat: <quarter|time_left|point_differential|points|fg_percentage|three_pt_percentage|assists|rebounds|made_threes>, 
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
        "description": "Game is in OT."
    },
    {
        "comparisons": [
            {
                "scope": "game",
                "stat": "quarter",
                "operator": "ge",
                "value": 4
            },
            {
                "scope": "game",
                "stat": "time_left",
                "operator": "le",
                "value": "2:00"
            },
            {
                "scope": "game",
                "stat": "point_differential",
                "operator": "le",
                "value": 6
            }
        ],
        "description": "Close game with under 2 minutes remaining."
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
        "description": "Player has 30 or more points before/at halftime."
    },
    {
        "comparisons": [
            {
                "scope": "player",
                "stat": "points",
                "operator": "ge",
                "value": 50
            }
        ],
        "description": "Player has 50+ points."
    },
    {
        "comparisons": [
            {
                "scope": "player",
                "stat": "made_threes",
                "operator": "ge",
                "value": 10
            }
        ],
        "description": "Player has 10 or more threes."
    }
]
