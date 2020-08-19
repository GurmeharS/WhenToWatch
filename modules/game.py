class Game(object):

    def __init__(self, inp_dict):
        self.teams = inp_dict["teams"]
        self.quarter = inp_dict["quarter"]
        self.time_left = inp_dict["time_left"]

    def summarize_points(self):
        print(f'{self.time_left} left in the {self.quarter}')
        for team in self.teams:
            print(team.name, ":")
            for player in sorted(team.players, key=lambda x: x.points, reverse=True):
                print(player)
            print("\n")
