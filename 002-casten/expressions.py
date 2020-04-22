# is het een expressie

3  # wel
3 + 3  # wel
prijs = 5  # niet
aantal = 3  # niet
prijs * aantal  # wel
totaalPrijs = prijs * aantal  # niet

totaalPrijs  # wel
print(totaalPrijs)  # wel
frank = "Frank Rijkaard"  # niet
print(f'Hallo {frank}')  # wel
f'Hoi {frank}'  # wel
f'Zeg {frank}, jouw voornaam heeft {len(frank[:5])} karakters.'  # wel
