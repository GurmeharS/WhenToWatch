class Team(object):

    def __init__(self, inp_dict):
        self.points = inp_dict["points"]
        self.players = inp_dict["players"]
        self.name = inp_dict["name"]
