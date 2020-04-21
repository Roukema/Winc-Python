""" 
dit is een opdracht van winc
gemaakt door matthijs om python beter te leren kennen
in deze opdracht gaat het om de comments


"""

rijst = 3
kip = 1
ui = 7

aantalrijst = 3
aantalkip = 2
aantalui = 10

kortingspercentage = 35

# totaal =  rijst + kip + ui
totaal = rijst*aantalrijst + kip*aantalkip + ui*aantalui
korting = totaal*(kortingspercentage/100)  # bereken de korting
eindtotaal = round(totaal - korting)
gemmiddeld = round(totaal/3, 2)

print(totaal)
print(gemmiddeld)
print("korting: ", korting)
print("eindtotaal = ", eindtotaal)
