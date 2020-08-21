class Analyzer():

    def compare(self, stat, operator, value) -> bool:
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

    # TODO: Return more bool. Possibly a dict of scope and object of interest.

    def compare_stats(self, game, comparisons) -> bool:
        for comparison in comparisons:
            met_threshold = False
            scope = comparison["scope"]
            stat = comparison["stat"]
            operator = comparison["operator"]
            value = comparison["value"]
            # print(f'{scope}, {stat} {operator} {value}')
            if scope == "game":
                if not hasattr(game, stat):
                    raise AttributeError(
                        "The game does not have attribute {}".format(stat))
                if stat == "time_left" and not game.compare_time_left(
                        operator, value):
                    return False
                met_threshold = self.compare(
                    getattr(game, stat), operator, value)
                if met_threshold:
                    print(game)
            elif scope == "team":
                for team in game.teams:
                    if not hasattr(team, stat):
                        raise AttributeError(
                            "Team {} does not have attribute {}".format(team.name, stat))
                    met_threshold = self.compare(
                        getattr(team, stat), operator, value)
            elif scope == "player":
                qualified_players = []
                for player in game.teams[0].players + game.teams[1].players:
                    if not hasattr(player, stat):
                        raise AttributeError(
                            "Player {} does not have attribute {}".format(player.name, stat))
                    if self.compare(getattr(player, stat), operator, value):
                        qualified_players.append(player)
                        print(player)
                if len(qualified_players) > 0:
                    met_threshold = True
            if not met_threshold:
                return False
        return True
