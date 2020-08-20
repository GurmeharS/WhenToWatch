class Game(object):

    def __init__(self, inp_dict):
        self.teams = inp_dict["teams"]
        self.quarter = inp_dict["quarter"]
        self.time_left = inp_dict["time_left"]

    def summarize_points(self):
        if self.quarter == "4th" and self.time_left == "0:00":
            print('Game has ended')
        elif self.quarter == "2nd" and self.time_left == "0:00":
            print('Halftime')
        else:
            print(f'{self.time_left} left in the {self.quarter}')
        for team in self.teams:
            print(team.name, ":")
            for player in self.sort_players_by_points(team):
                print(player)
            print("\n")

    def sort_players_by_points(self, team):
        return sorted(team.players, key=lambda x: x.points, reverse=True)
