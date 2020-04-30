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
    alle_spelers.append({"id": teller, "full_name": ajax[teller], "team": "ajax"})
    teller += 1
while teller < (len(ajax) + len(vitesse)):
    alle_spelers.append(
        {"id": teller, "full_name": vitesse[teller_vitesse], "team": "vitesse"}
    )
    teller += 1
    teller_vitesse += 1


print(alle_spelers)

doelpunten = [
    {"minuut": 10, "id_scoorende_speler": 7},
    {"minuut": 28, "id_scoorende_speler": 7},
    {"minuut": 32, "id_scoorende_speler": 9},
    {"minuut": 42, "id_scoorende_speler": 9},
    {"minuut": 47, "id_scoorende_speler": 9},
    {"minuut": 49, "id_scoorende_speler": 10},
    {"minuut": 51, "id_scoorende_speler": 10},
    {"minuut": 63, "id_scoorende_speler": 5},
    {"minuut": 70, "id_scoorende_speler": 4},
    {"minuut": 75, "id_scoorende_speler": 19},
    {"minuut": 78, "id_scoorende_speler": 9},
    {"minuut": 81, "id_scoorende_speler": 10},
    {"minuut": 88, "id_scoorende_speler": 7},
]


def eindstand(spelers, doelpunten):
    doelpunten_ajax = 0
    doelpunten_vitesse = 0
    winnaar = ""
    verliezer = ""
    for doelpunt in doelpunten:
        for speler in spelers:
            if speler["id"] == doelpunt["id_scoorende_speler"]:
                if speler["team"] == "ajax":
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
            if speler["id"] == doelpunt["id_scoorende_speler"]:
                if speler["team"] == "ajax":
                    doelpunten_ajax += 1
                    print(
                        "In de "
                        + str(doelpunt["minuut"])
                        + "e minuut scoort"
                        + speler["full_name"]
                        + " voor "
                        + speler["team"]
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
                        + str(doelpunt["minuut"])
                        + "e minuut scoort"
                        + speler["full_name"]
                        + " voor "
                        + speler["team"]
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
