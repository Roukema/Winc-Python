preiPrijs = 2
print("Prei kost " + str(preiPrijs) + " euro per kilo")

# deel 2

bestelling = "prei 4"
aantal = bestelling[bestelling.find(" "):]
print("totaalprijs is: ", int(aantal)*preiPrijs, sep=(""))
print("totaalprijs is: " + str(int(aantal)*preiPrijs))

# deel 3
broccoliPrijs = 2.34
bestelling2 = "broccoli 1.6"
totaalkost = round(float(bestelling2[bestelling2.find(" "):])*broccoliPrijs, 2)
print(bestelling2[bestelling2.find(" "):]+" kilo " +
      bestelling2[0:bestelling2.find(" ")] + " kost " + str(totaalkost))
