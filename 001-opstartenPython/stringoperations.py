
# team
hans = "Hans van Breukelen"
berry = "Berry van Aerle"
ronald = "Ronald Koeman"
adri = "Adri van Tiggelen"
gerald = 'Gerald Vanenburg'
arnold = 'Arnold Mühren'
jan = 'Jan Wouters'
erwin = 'Erwin Koeman'
marco = 'Marco van Basten'
ruud = 'Ruud Gullit'

# wissels
joop = 'Joop Hiele'
wilbert = 'Wilbert Suvrijn'
john = "John van 't Schip"
johnb = 'John Bosman'
wim = 'Wim Kieft'

# doelpunten
eersteDoelPunt = 35
tweedeDoelPunt = 54

print(ruud + " scoorde in de ", eersteDoelPunt,
      "e minuut." + "\n" + marco + " scoorde in de ", tweedeDoelPunt, "e minuut.", sep="")


Voornaam = wim[0: wim.find(" ")]
print(Voornaam)
lengteAchternaam = len(wim[wim.find(" ") + 1:])
print('lengte van kieft is', lengteAchternaam, 'letters')

letterEnAchternaam = wim[0: 1] + ". " + wim[wim.find(" ")+1:]
print(letterEnAchternaam)

vierKeerWim = (len(wim[0:wim.find(" ")]) *
               (wim[0:wim.find(" ")]+"! ")).strip(" ")
print(vierKeerWim)

print(vierKeerWim[-1] == " ")
