class Player(object):

    def __init__(self, inp_dict):
        self.name = inp_dict["name"]
        self.team = inp_dict["team"]
        self.points = inp_dict["points"]
        self.assists = inp_dict["assists"]
        self.rebounds = inp_dict["rebounds"]
        self.minutes = inp_dict["minutes"]
        self.fg = inp_dict["fg"]
        self.three_pt = inp_dict["3pt"]

    def __str__(self):
        return f'{self.name} on the {self.team}: {self.points} pts on {self.fg} shooting, {self.assists} assists, {self.rebounds} rebounds'
