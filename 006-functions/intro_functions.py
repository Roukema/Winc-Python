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
