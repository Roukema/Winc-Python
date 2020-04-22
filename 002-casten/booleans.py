

erIsRegen = True
erIsZon = True
hetIsDag = False
deKoeienZijnBinnen = False
erIsVeelWind = True
deGierputIsVol = True
erMoetGemolkenWorden = True
hetIsHerfst = True

# acties
naarBinnen = "haal de koeien naar binnen"
melken = "melk de koeien"
mesten = "bemest het land"
maaien = "maai het gras voor hooi"

# 1
if erMoetGemolkenWorden and not deKoeienZijnBinnen:
    print(naarBinnen + " en "+melken)

# 2
if not deKoeienZijnBinnen and erIsRegen and not hetIsDag:
    print(naarBinnen)

# 3
if not deKoeienZijnBinnen and erIsVeelWind and not erMoetGemolkenWorden:
    print(naarBinnen)
if not deKoeienZijnBinnen and erIsVeelWind and erMoetGemolkenWorden:
    print(naarBinnen + " en " + melken)

# 4
if deGierputIsVol and erIsRegen and not deKoeienZijnBinnen:
    print(naarBinnen + " en " + mesten)
if deGierputIsVol and erIsRegen and deKoeienZijnBinnen:
    print(mesten)

# 5
if hetIsHerfst and erIsZon and deKoeienZijnBinnen:
    print(maaien)
if hetIsHerfst and erIsZon and not deKoeienZijnBinnen:
    print(naarBinnen + " en " + maaien)

# 6
if hetIsHerfst and erIsZon and deKoeienZijnBinnen:
    print("breng die koeien lekker naar buiten joh")
