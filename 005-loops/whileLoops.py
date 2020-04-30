import re

all_countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "American Samoa",
    "Andorra",
    "Angola",
    "Anguilla",
    "Antarctica",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Aruba",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bermuda",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Bouvet Island",
    "Brazil",
    "British Indian Ocean Territory",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Cape Verde",
    "Cayman Islands",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Christmas Island",
    "Cocos (Keeling) Islands",
    "Colombia",
    "Comoros",
    "Congo",
    "The Democratic Republic of Congo",
    "Cook Islands",
    "Costa Rica",
    "Ivory Coast",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor",
    "Ecuador",
    "Egypt",
    "England",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Ethiopia",
    "Falkland Islands",
    "Faroe Islands",
    "Fiji Islands",
    "Finland",
    "France",
    "French Guiana",
    "French Polynesia",
    "French Southern territories",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Gibraltar",
    "Greece",
    "Greenland",
    "Grenada",
    "Guadeloupe",
    "Guam",
    "Guatemala",
    "Guernsey",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Heard Island and McDonald Islands",
    "Holy See (Vatican City State)",
    "Honduras",
    "Hong Kong",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Isle of Man",
    "Italy",
    "Jamaica",
    "Japan",
    "Jersey",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libyan Arab Jamahiriya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Macao",
    "North Macedonia",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Martinique",
    "Mauritania",
    "Mauritius",
    "Mayotte",
    "Mexico",
    "Micronesia, Federated States of",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Montserrat",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "Netherlands Antilles",
    "New Caledonia",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "Niue",
    "Norfolk Island",
    "North Korea",
    "Northern Ireland",
    "Northern Mariana Islands",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Palestine",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Pitcairn",
    "Poland",
    "Portugal",
    "Puerto Rico",
    "Qatar",
    "Reunion",
    "Romania",
    "Russian Federation",
    "Rwanda",
    "Saint Helena",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Pierre and Miquelon",
    "Saint Vincent and the Grenadines",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Scotland",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "South Georgia and the South Sandwich Islands",
    "South Korea",
    "South Sudan",
    "Spain",
    "SriLanka",
    "Sudan",
    "Suriname",
    "Svalbard and Jan Mayen",
    "Swaziland",
    "Sweden",
    "Switzerland",
    "Syria",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Timor-Leste",
    "Togo",
    "Tokelau",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Turks and Caicos Islands",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "United States Minor Outlying Islands",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Venezuela",
    "Vietnam",
    "Virgin Islands, British",
    "Virgin Islands, U.S.",
    "Wales",
    "Wallis and Futuna",
    "Western Sahara",
    "Yemen",
    "Yugoslavia",
    "Zambia",
    "Zimbabwe",
]

nieuwe_lijst_landen = []

# for land in all_countries:
#     nieuwe_lijst_landen[land] = len(land)
# print(nieuwe_lijst_landen)

for land in all_countries:
    landDict = {"naam": land, "aantal": len(land)}
    nieuwe_lijst_landen.append(landDict)


print(nieuwe_lijst_landen)
kortenamenlijst = []
teller = 0
while teller < len(nieuwe_lijst_landen):

    if nieuwe_lijst_landen[teller]["aantal"] < 5:
        kortenamenlijst.append(nieuwe_lijst_landen[teller]["naam"])
        teller += 1
    else:
        teller += 1
        pass

while teller < len(nieuwe_lijst_landen):

    if kortenamenlijst[teller]["aantal"] < 4:
        kortenamenlijst.append(kortenamenlijst[teller]["naam"])
        teller += 1
    else:
        teller += 1
        pass

nieuwe_lijst_landen_klinkers = []
print(kortenamenlijst)
for land in all_countries:
    landDict = {
        "naam": land,
        "aantal": len(land),
        "aantal_klinkers": len(re.sub("[^aeiou]", "", land)) + 1,
    }
    nieuwe_lijst_landen_klinkers.append(landDict)

# 2

meeste_klinkers_lijst = []
teller = 0
aantalKlinkers = 8
while len(meeste_klinkers_lijst) != 3:

    while teller < len(nieuwe_lijst_landen_klinkers):

        if nieuwe_lijst_landen_klinkers[teller]["aantal_klinkers"] > aantalKlinkers:
            meeste_klinkers_lijst.append(nieuwe_lijst_landen[teller]["naam"])
            teller += 1
        else:
            teller += 1
        pass
    aantalKlinkers += 1
    teller = 0
    if len(meeste_klinkers_lijst) + 1 == 3:
        break
    meeste_klinkers_lijst = []


print(meeste_klinkers_lijst)

# 3

verzameldeletters = []
teller = 0
alfabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
letterteller = 0
landen_nodig = []


while teller < len(all_countries) and alfabet != []:
    while letterteller < len(all_countries[teller]):
        letter_aan_de_beurt = all_countries[teller][letterteller].lower()
        if (
            letter_aan_de_beurt not in verzameldeletters
            and letter_aan_de_beurt in alfabet
        ):
            verzameldeletters += letter_aan_de_beurt
            alfabet.remove(letter_aan_de_beurt)
            letterteller += 1
            if all_countries[teller] not in landen_nodig:
                landen_nodig.append(all_countries[teller])
        else:
            letterteller += 1
        pass
    letterteller = 0
    teller += 1


print(landen_nodig)
