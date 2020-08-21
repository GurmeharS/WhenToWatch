class Player(object):

    def __init__(self, inp_dict):
        self.name = inp_dict["name"]
        self.team = inp_dict["team"]
        self.points = inp_dict["points"]
        self.assists = inp_dict["assists"]
        self.rebounds = inp_dict["rebounds"]
        self.minutes = inp_dict["minutes"]
        self.fg = inp_dict["fg"]
        self.fg_percentage = self.get_fg_percentage()
        self.three_pt = inp_dict["3pt"]
        self.three_pt_percentage = self.get_fg_percentage(three_pt=True)
        self.made_threes = self.get_made_threes()

    def __str__(self):
        return f'{self.name} on the {self.team}: {self.points} pts on {self.fg} shooting, {self.assists} assists, {self.rebounds} rebounds'

    def get_fg_percentage(self, three_pt=False):
        fg = self.three_pt if three_pt else self.fg
        [shots_made, shots_taken] = fg.split("-")
        shots_made, shots_taken = int(shots_made), int(shots_taken)
        if shots_taken == 0:
            return 0.00
        return float(shots_made/shots_taken) * 100

    def get_made_threes(self):
        return int(self.three_pt.split("-")[0])
