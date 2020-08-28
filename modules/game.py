class Game(object):

    def __init__(self, inp_dict):
        self.teams = inp_dict["teams"]
        self.time_left = inp_dict["time_left"]
        self.point_differential = self.get_pt_differential()
        self.quarter = self.get_quarter(inp_dict["quarter"])

    def __str__(self):
        time = f'{self.time_left} left in {"OT" if self.quarter > 5 else "quarter " + str(self.quarter)}'
        if self.time_left == "0:00":
            if self.quarter == 4:
                time = "Final"
            elif self.quarter == 2:
                time = "Halftime"
        return f'{self.teams[0].name} {self.teams[0].points} - {self.teams[1].points} {self.teams[1].name} - ' + time

    def summarize_points(self):
        if self.quarter == "4th" and self.time_left == "0:00":
            print('Game has ended')
        elif self.quarter == "2nd" and self.time_left == "0:00":
            print('Halftime')
        else:
            print(f'{self.time_left} left in the {self.quarter}')
        print(
            f'{self.teams[0].name} {self.teams[0].points} - {self.teams[1].points} {self.teams[1].name}\n')
        for team in self.teams:
            print(team.name, ":")
            for player in self.sort_players_by_points(team):
                print(player)
            print("\n")

    def get_quarter(self, quarter_str):
        if "OT" in quarter_str:
            return 5
        return int(quarter_str[0])

    def get_pt_differential(self):
        return abs(self.teams[0].points - self.teams[1].points)

    def sort_players_by_points(self, team):
        return sorted(team.players, key=lambda x: x.points, reverse=True)

    def compare_time_left(self, operator, time):
        minutes_remaining, minutes_rhs = int(
            self.time_left.split(":")[0]), int(time.split(":")[0])
        seconds_remaining, seconds_rhs = float(
            self.time_left.split(":")[1]), float(time.split(":")[1])
        if operator == "gt":
            return minutes_remaining > minutes_rhs or (minutes_remaining == minutes_rhs and seconds_remaining > seconds_rhs)
        elif operator == "ge":
            return minutes_remaining >= minutes_rhs or (minutes_remaining == minutes_rhs and seconds_remaining >= seconds_rhs)
        elif operator == "eq":
            return minutes_remaining == minutes_rhs and seconds_remaining == seconds_rhs
        elif operator == "ne":
            return minutes_remaining != minutes_rhs or seconds_remaining != seconds_rhs
        elif operator == "le":
            return minutes_remaining <= minutes_rhs or (minutes_remaining == minutes_rhs and seconds_remaining <= seconds_rhs)
        elif operator == "lt":
            return minutes_remaining < minutes_rhs or (minutes_remaining == minutes_rhs and seconds_remaining < seconds_rhs)
        else:
            raise Exception(
                "The comparioson operator '{}' is not valid".format(operator))
