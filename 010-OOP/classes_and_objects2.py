class Player:
    def __init__(self, player_id, full_name, team):
        self.id = player_id
        self.full_name = full_name
        self.team = team


class Trainer:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def get_trainer_with_team(team, trainers):
        for trainer in trainers:
            if trainer.team == team:
                return trainer.name


class Team:
    def __init__(self, name, players, trainer):
        self.name = name
        self.players = players
        self.trainer = trainer

    def makeListofPlayers(self, teamlist, teamName):
        for player in teamlist:
            self.players.append(Player(len(self.players), player, teamName))

    # def get_players_with_team(self, player_team):
    #     players = []
    #     for speler in self.players:
    #         if player_team == speler.team:
    #             players.append(speler)
    #     return players


class Goal:
    def __init__(self, minuut, player, team):
        self.minuut = minuut
        self.player = player
        self.team = team


class MatchInformation:
    def __init__(
        self, date, home_team, away_team, stadion, stadion_location, referee, vistors
    ):
        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.stadion = stadion
        self.stadion_location = stadion_location
        self.referee = referee
        self.vistors = str(vistors)


class Match:
    def __init__(self, matchinfo, trainers, home_players, away_players):
        self.matchinfo = matchinfo
        self.trainers = trainers
        self.home_players = home_players
        self.away_players = away_players

        self.home_team = Team(home_players[0].team, home_players, trainers[0])
        self.away_team = Team(away_players[0].team, away_players, trainers[1])
        self.goals = []

        print("voor", self.goals)

    # def addGoal(self, goal):
    #     self.goals.append(goal)

    def addGoal(self, goal):
        for player in self.home_players:
            if player.id == goal[1]:
                return self.goals.append(Goal(goal[0], player.full_name, player.team))

        for player in self.away_players:
            if player.id == goal[1]:
                return self.goals.append(Goal(goal[0], player.full_name, player.team))

    # print("na", self.goals[0].player)


matchinfo = MatchInformation(
    "19 mei 1972", "Ajax", "Vitesse", "de Meer", "Amsterdam", "Joop Vervoort", 6000
)
trainers = [Trainer("Cor Brom", "Vitesse"), Trainer("Stefan Kovács", "Ajax")]

ajax_spelers = [
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
ajax_spelers = [
    {"naam": speler, "id": index} for index, speler in enumerate(ajax_spelers)
]
ajax_spelers = [Player(speler["id"], speler["naam"], "ajax") for speler in ajax_spelers]


vitesse_spelers = [
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
vitesse_spelers = [
    {"naam": speler, "id": index + len(ajax_spelers)}
    for index, speler in enumerate(vitesse_spelers)
]
vitesse_spelers = [
    Player(speler["id"], speler["naam"], "vitesse") for speler in vitesse_spelers
]
doelpunten = [
    (10, 7),
    (28, 7),
    (32, 9),
    (42, 9),
    (47, 9),
    (49, 10),
    (51, 10),
    (63, 5),
    (70, 4),
    (75, 19),
    (78, 9),
    (81, 10),
    (88, 7),
]

ajvi72 = Match(matchinfo, trainers, ajax_spelers, vitesse_spelers)
for goal in doelpunten:
    ajvi72.addGoal(goal)


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
    print(
        f"Op {all_info.matchinfo.date} speelde {all_info.matchinfo.home_team} tegen {all_info.matchinfo.away_team} in het {all_info.matchinfo.stadion} stadion in {all_info.matchinfo.stadion_location}. \n\
    Er waren {all_info.matchinfo.vistors} bezoekers aanwezig in het stadion. \n\
    De wedstrijd werd gefloten door {all_info.matchinfo.referee}. \n\
    De trainer van {all_info.matchinfo.home_team} was {Trainer.get_trainer_with_team(all_info.matchinfo.home_team, Match.trainers)}.\n\
    De trainer van {all_info.matchinfo.away_team} was {Trainer.get_trainer_with_team(all_info.matchinfo.away_team, Match.trainers)}."
    )
    for doelpunt in Match.doelpunten:
        if doelpunt.team == "Ajax":
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
        winnaar = "Ajax"
        verliezer = "Vitesse"
    else:
        winnaar = "Vitesse"
        verliezer = "Ajax"
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
print_match_report(ajvi72)
