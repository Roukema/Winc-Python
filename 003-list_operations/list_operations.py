
Nicholas = ['Nicholas "Nik Napalm" Bullen',
            ['lead vocals', 'bass'], [1981, 1986]]
Miles = ['Miles "Rat" Ratledge', 'drums', [1981, 1985]]
Simon = ['Simon "Si O" Oppenheimer', 'guitars', [1981, 1982]]
Graham = ['Graham "Grayhard" Robertson', ['guitars', 'bass'], [1982, 1985]]
Daryl = ['Daryl "Daz F" Fedeski', 'guitars', 1982]
Finbar = ['Finbar "Fin" Quinn', 'bass', [1983, 1984]]
Marian = ['Marian Williams',  'lead vocals', 1984]
Damien = ['Damien Errington',  'guitars', 1985]
Justin = ['Justin Broadrick', ['guitars',
                               'backing vocals', 'lead vocals'], [1985, 1986]]
Peter = ['Peter "P-Nut" Shaw', 'bass', 1985]
Mick = ['Mick Harris', ['drums', 'backing vocals'], [1985, 1991]]
Jim = ['Jim Whitely',  'bass', [1986, 1987]]
Frank = ['Frank Healy', 'guitars', 1986]
Bill = ['Bill Steer', 'guitars', [1987, 1989]]
Lee = ['Lee Dorrian',  'lead vocals', [1987, 1989]]
Jesse = ['Jesse Pintado',   'guitars',  [1989, 2004]]
Phil = ['Phil Vane', 'lead vocals', [1996, 1997]]
Erik = ['Phil Burke',  'guitars', 2015]
Jesper = ['Jesper Liveröd', 'bass', 2017]
Shane = ['Shane Embury', ['bass', 'backing vocals'], [1987, 2021]]
Mark = ['Mark "Barney" Greenway', 'lead vocals',  [1997, 2021]]  # (1989–1996,
Danny = ['Danny Herrera', 'drums', [1991, 2021]]

alle_band_leden = [Nicholas, Miles, Simon,
                   Graham, Daryl, Finbar, Marian, Damien, Justin, Peter, Mick, Jim, Frank,
                   Bill, Lee, Jesse, Phil, Erik, Jesper, Shane, Mark, Danny]

jaartal = int(input("vul een jaartal in tussen 1981 en 2020:"))
zat_in_de_band = []
zat_in_de_band_tekst = ""


for x in alle_band_leden:
    if type(x[-1]) == list:
        if x[-1][0] <= jaartal and x[-1][1] >= jaartal:
            zat_in_de_band.append(x)
    elif x[-1] == jaartal:
        zat_in_de_band.append(x)

print(zat_in_de_band)

for x in zat_in_de_band:
    if type(x[-2]) == list:
        zat_in_de_band_tekst += (
            f" {x[0]} speelt {x[-2][0]} en doet {x[-2][1]},")
    else:
        zat_in_de_band_tekst += (
            f" {x[0]} speelt {x[-2]},")

zat_in_de_band_tekst = zat_in_de_band_tekst.strip(",")
zat_in_de_band_tekst += (".")

print("Het jaar is " + str(jaartal) + "."+zat_in_de_band_tekst)

# sommige leden spelen 3 instrumenten dat is hier nog niet goed in opgenomen.
# er verschijnt nog niet de juiste tekst bij instrumenten moet het spelen zijn
# en bij vocals moet het doet zijn.
