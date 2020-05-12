
class Player:
    def __init__(self, player_id, full_name, team):
        self.id = player_id
        self.full_name = full_name
        self.team = team


class Goal:
    def __init__(self, minuut, player):
        self.minuut = minuut
        self.player = player.full_name
        self.team = player.team

class Team:
    def __init__(self, name, players, trainer):
        self.name = name
        self.players = players
        self.trainer = trainer

    def get_players_with_team(player_team):
        players = []
        for speler in alle_spelers:
            if player_team == speler.team:
                players.append(speler)
        return players    

    def get_player_with_id(player_id):
        for speler in alle_spelers:
            if player_id == speler.id:
                return speler

class Trainer: 
    def __init__(self, name, team):
        self.name = name
        self.team = team
    
    def get_trainer_with_team(team):
        for trainer in Match.trainers:
            if trainer.team == team:
                return trainer.name


class MatchInformation: 
    def __init__(self, date, home_team, away_team, stadion, stadion_location, referee, vistors):
        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.stadion = stadion
        self.stadion_location = stadion_location
        self.referee = referee
        self.vistors = str(vistors)

class Match:
    def __init__(self, teams, goals):
        self.teams = teams
        self.trainers = self.trainers
        self.goals = goals

    matchinfo = MatchInformation("19 mei 1972", "Ajax", "Vitesse", "de Meer", "Amsterdam", "Joop Vervoort", 6000)
    trainers =[
        Trainer("Cor Brom", "Vitesse"),
        Trainer("Stefan Kovács", "Ajax")]



ajax = [
    "Heinz Stuy",
    "Ruud Krol",
    "Wim Suurbier",
    "Horst Blankenburg",
    "Barry Hulshoff",
    "Gerrie Mühren",
    "Arie Haan",
    "Johan Neeskens",
    "Sjaak Swart",
    "Johan Cruyff",
    "Dick van Dijk",
    "Johnny Rep",
]

vitesse = [
    "Dick Beukhof",
    "Willy Melchers",
    "Ben Bosma",
    "Nico Kunst",
    "Ben Gerritsen",
    "Willy Veenstra",
    "Bram van Kerkhof",
    "Herman Veenendaal",
    "Co Prins",
    "Theo Rutten",
    "Henk Vleeming",
    "Henk Hofs",
    "John Meeuwsen",
]


alle_spelers = []
teller = 0
teller_vitesse = 0
while teller < len(ajax):
    alle_spelers.append(Player(teller, ajax[teller], "Ajax"))
    teller += 1
while teller < (len(ajax) + len(vitesse)):
    alle_spelers.append(Player(teller, vitesse[teller_vitesse], "Vitesse"))
    teller += 1
    teller_vitesse += 1





doelpunten = [
    Goal(10, Team.get_player_with_id(7)),
    Goal(28, Team.get_player_with_id(7)),
    Goal(32, Team.get_player_with_id(9)),
    Goal(42, Team.get_player_with_id(9)),
    Goal(47, Team.get_player_with_id(9)),
    Goal(49, Team.get_player_with_id(10)),
    Goal(51, Team.get_player_with_id(10)),
    Goal(63, Team.get_player_with_id(5)),
    Goal(70, Team.get_player_with_id(4)),
    Goal(75, Team.get_player_with_id(19)),
    Goal(78, Team.get_player_with_id(9)),
    Goal(81, Team.get_player_with_id(10)),
    Goal(88, Team.get_player_with_id(7)),
]
teams = [
    Team("Ajax", Team.get_players_with_team("Ajax"), Trainer.get_trainer_with_team("Ajax")),
    Team("Vitesse", Team.get_players_with_team("Vitesse"), Trainer.get_trainer_with_team("Vitesse"))
]

all_info = Match(teams, doelpunten)
 
# def eindstand(spelers, doelpunten):
#     doelpunten_ajax = 0
#     doelpunten_vitesse = 0
#     winnaar = ""
#     verliezer = ""
#     for doelpunt in doelpunten:
#         if doelpunt.team == "ajax":
#             doelpunten_ajax += 1
#         else:
#             doelpunten_vitesse += 1
#     if doelpunten_ajax > doelpunten_vitesse:
#         winnaar = "ajax"
#         verliezer = "vitesse"
#     else:
#         winnaar = "vitesse"
#         verliezer = "ajax"
#     print(
#         winnaar,
#         "wint van",
#         verliezer,
#         "met",
#         str(doelpunten_ajax),
#         "-",
#         str(doelpunten_vitesse),
#     )


# 2


def print_match_report(all_info):
    doelpunten_ajax = 0
    doelpunten_vitesse = 0
    winnaar = ""
    verliezer = ""
    print(f'Op {all_info.matchinfo.date} speelde {all_info.matchinfo.home_team} tegen {all_info.matchinfo.away_team} in het {all_info.matchinfo.stadion} stadion in {all_info.matchinfo.stadion_location}. \n\
    Er waren {all_info.matchinfo.vistors} bezoekers aanwezig in het stadion. \n\
    De wedstrijd werd gefloten door {all_info.matchinfo.referee}. \n\
    De trainer van {all_info.matchinfo.home_team} was {Trainer.get_trainer_with_team(all_info.matchinfo.home_team)}.\n\
    De trainer van {all_info.matchinfo.away_team} was {Trainer.get_trainer_with_team(all_info.matchinfo.away_team)}.')
    for doelpunt in doelpunten:
        if doelpunt.team == "ajax":
            doelpunten_ajax += 1
            print(
                "In de "
                + str(doelpunt.minuut)
                + "e minuut scoort "
                + doelpunt.player
                + " voor "
                + doelpunt.team
                + ", het is "
                + str(doelpunten_ajax)
                + " - "
                + str(doelpunten_vitesse)
                + "."
            )
        else:
            doelpunten_vitesse += 1
            print(
                "In de "
                + str(doelpunt.minuut)
                + "e minuut scoort "
                + doelpunt.player
                + " voor "
                + doelpunt.team
                + ", het is "
                + str(doelpunten_ajax)
                + " - "
                + str(doelpunten_vitesse)
                + "."
            )
    if doelpunten_ajax > doelpunten_vitesse:
        winnaar = "ajax"
        verliezer = "vitesse"
    else:
        winnaar = "vitesse"
        verliezer = "ajax"
    print(
        winnaar,
        "wint van",
        verliezer,
        "met",
        str(doelpunten_ajax),
        "-",
        str(doelpunten_vitesse),
    )



# eindstand(alle_spelers, doelpunten, teams, trainers)
print_match_report(all_info)



