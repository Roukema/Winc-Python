lst1 = [1, 2, 3]
lst2 = lst1
lst1[1] = 6
result = lst1[1] + lst2[1]
# Wat is de waarde van result?
# 12
# En waarom is dat de waarde van result?
# lst1 wordt aangepast en lst2 verwijst naar lst1 dus wordt ook aangepast

dict1 = {"a": 1, "b": 2}
dict2 = dict1
dict1["a"] = 8
result = dict1["a"] + dict2["a"]
# Wat is de waarde van result?
# 18
# En waarom is dat de waarde van result?
# dict 2 verwijst naar 1 en 1 wordt aangepast

lst3 = [{"c": 3, "d": 4}, {"c": 5, "d": 6}]
lst4 = lst3
lst3[0]["c"] = 7
result = 0
for lst in [lst3, lst4]:
    for dct in lst:
        for val in dct.values():
            result += val
# Wat is de waarde van result?
resultaat = (7 + 4 + 5 + 6) * 2  # 44
assert resultaat == result
# En waarom is dat de waarde van result?
