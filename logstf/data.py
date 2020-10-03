# Idea is we can do stuff like this:

# dat = l.get_data(put id here)
#
# my_dpm = dat.player_with_steamid(me).dpm()
#
# drops = dat.round_number(1).total_drops()
#
# for (_, name, msg) in dat.chat():
#   print(f'{name}: {msg}')

class LogData:
    def __init__(self, log_text):
        """Returns a complete LogData object
        after parsing the json log_text
        retrieved from logs.tf"""
        self.raw = log_text

    def as_json(self):
        """Returns raw json of the log,
        if you want to parse it yourself."""
        return self.raw

    def round_number(self, n):
        """Return Round object for the nth round."""

    def player_with_steamid(self, steamid):
        """Returns Player object of user with given steamid,
        if they appear in the log."""
        pass

    def team_stats(self, team):
        """Returns stats like total kills and damage for the
        given team, 'red' or 'blu'."""

    def players_on_team(self, team):
        """Returns list of Player objects
        representing each player on a team.
        `team` can be 'red' or 'blu'"""
        pass

    def chat(self):
        """Returns list of tuples (steamid, playername, string)
        representing each chat message in the game."""
        pass

class Player:
    """A player's stats, like damage per minute, headshots, kills,
    etc."""

class Team:
    """A team's stats, like total damage or total kills."""

class Round:
    """Stats for a given round, including events like medic kills
    or ubercharges."""

class Weapon:
    """Stats for a weapon like accuracy, total damage, etc."""
