
class Player:
    def __init__(self, player_id, full_name, team):
        self.id = player_id
        self.full_name = full_name
        self.team = team


class Goal:
    def __init__(self, minuut, player):
        self.minuut = minuut
        self.full_name_player = player.full_name

   
class Team:
    def __init__(self, name, players, trainer):
        self.name = name
        self.players = players
        self.trainer = trainer




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
    alle_spelers.append(Player(teller, ajax[teller], "ajax"))
    teller += 1
while teller < (len(ajax) + len(vitesse)):
    alle_spelers.append(Player(teller, vitesse[teller_vitesse], "vitesse"))
    teller += 1
    teller_vitesse += 1


print(alle_spelers)

def get_player_with_id(player_id):
    for speler in alle_spelers:
        if player_id == speler.id:
            print(speler.full_name)
            return speler


doelpunten = [
    Goal(10, get_player_with_id(7)),
    Goal(28, get_player_with_id(7)),
    Goal(32, get_player_with_id(9)),
    Goal(42, get_player_with_id(9)),
    Goal(47, get_player_with_id(9)),
    Goal(49, get_player_with_id(10)),
    Goal(51, get_player_with_id(10)),
    Goal(63, get_player_with_id(5)),
    Goal(70, get_player_with_id(4)),
    Goal(75, get_player_with_id(19)),
    Goal(78, get_player_with_id(9)),
    Goal(81, get_player_with_id(10)),
    Goal(88, get_player_with_id(7)),
]


def eindstand(spelers, doelpunten):
    doelpunten_ajax = 0
    doelpunten_vitesse = 0
    winnaar = ""
    verliezer = ""
    for doelpunt in doelpunten:
        if speler.team == "ajax":
            doelpunten_ajax += 1
        else:
            doelpunten_vitesse += 1
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


# 2


def print_match_report(spelers, doelpunten):
    doelpunten_ajax = 0
    doelpunten_vitesse = 0
    winnaar = ""
    verliezer = ""
    for doelpunt in doelpunten:
        for speler in spelers:
            if speler.id == doelpunt.id_scoorende_speler:
                if speler.team == "ajax":
                    doelpunten_ajax += 1
                    print(
                        "In de "
                        + str(doelpunt.minuut)
                        + "e minuut scoort "
                        + speler.full_name
                        + " voor "
                        + speler.team
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
                        + speler.full_name
                        + " voor "
                        + speler.team
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



eindstand(alle_spelers, doelpunten)
print_match_report(alle_spelers, doelpunten)



