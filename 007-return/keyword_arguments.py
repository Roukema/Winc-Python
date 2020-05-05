def newton_needed(mass, product, gekozen_planeet="aarde"):
    for planeet in Zwaartekracht:
        if planeet["naam"] == gekozen_planeet:
            gravity = planeet["gravity"]
    newton = mass * gravity
    print(
        f"Het kost {newton} Newton om {product} op de {gekozen_planeet} vast te houden"
    )


Zwaartekracht = [
    {"naam": "Sun", "gravity": 274},
    {"naam": "Jupiter", "gravity": 24.92},
    {"naam": "Neptune", "gravity": 11.15},
    {"naam": "Saturn", "gravity": 10.44},
    {"naam": "Earth", "gravity": 9.798},
    {"naam": "Uranus", "gravity": 8.87},
    {"naam": "Venus", "gravity": 8.87},
    {"naam": "Mars", "gravity": 3.71},
    {"naam": "Mercury", "gravity": 3.7},
    {"naam": "Moon", "gravity": 1.62},
    {"naam": "Pluto", "gravity": 0.58},
]


# newton_needed(0.1)
# newton_needed(800)
newton_needed(0.1, "appel", "Earth")
# newton_needed(0.0015, Sun, "Zon")


# 2
def aantrekking(massa1KG, massa2KG, afstandInMeter):
    constanteG = 6.674 * 10 ** -11
    newton = ((massa1KG * massa2KG) / afstandInMeter ** 2) * constanteG
    return newton  # voor opdacht 3
    # print(newton) opdracht 2


aantrekking(800, 1500, 3)
aantrekking(massa1KG=0.1, massa2KG=5.972 * 10 ** 24, afstandInMeter=6.371 * 10 ** 6)


# 3

# Distance is in AU https://en.wikipedia.org/wiki/Astronomical_unit
distances = [
    {"from": "Mercury", "to": "Venus", "distance": 0.34},
    {"from": "Mercury", "to": "Earth", "distance": 0.61},
    {"from": "Mercury", "to": "Mars", "distance": 1.14},
    {"from": "Mercury", "to": "Jupiter", "distance": 4.82},
    {"from": "Mercury", "to": "Saturn", "distance": 9.14},
    {"from": "Mercury", "to": "Uranus", "distance": 18.82},
    {"from": "Mercury", "to": "Neptune", "distance": 29.70},
    {"from": "Venus", "to": "Earth", "distance": 0.28},
    {"from": "Venus", "to": "Mars", "distance": 0.8},
    {"from": "Venus", "to": "Jupiter", "distance": 4.48},
    {"from": "Venus", "to": "Saturn", "distance": 8.80},
    {"from": "Venus", "to": "Uranus", "distance": 18.49},
    {"from": "Venus", "to": "Neptune", "distance": 29.37},
    {"from": "Earth", "to": "Mars", "distance": 0.52},
    {"from": "Earth", "to": "Jupiter", "distance": 4.2},
    {"from": "Earth", "to": "Saturn", "distance": 8.52},
    {"from": "Earth", "to": "Uranus", "distance": 18.21},
    {"from": "Earth", "to": "Neptune", "distance": 29.09},
    {"from": "Mars", "to": "Jupiter", "distance": 3.68},
    {"from": "Mars", "to": "Saturn", "distance": 7.99},
    {"from": "Mars", "to": "Uranus", "distance": 17.69},
    {"from": "Mars", "to": "Neptune", "distance": 28.56},
    {"from": "Jupiter", "to": "Saturn", "distance": 4.32},
    {"from": "Jupiter", "to": "Uranus", "distance": 14.01},
    {"from": "Jupiter", "to": "Neptune", "distance": 24.89},
    {"from": "Saturn", "to": "Uranus", "distance": 9.7},
    {"from": "Saturn", "to": "Neptune", "distance": 20.57},
    {"from": "Uranus", "to": "Neptune", "distance": 10.88},
]

# Weight is in 10 ** 24 kg
weights = {
    "Mercury": 0.33,
    "Venus": 4.87,
    "Earth": 5.97,
    "Mars": 0.642,
    "Jupiter": 1898,
    "Saturn": 568,
    "Uranus": 86.8,
    "Neptune": 102,
}


def convertAuToMeters(au):
    meters = au * 149597870700
    return meters


def convertKG(weight):
    realWeight = weight * 10 ** 24
    return realWeight


def getAttraction(planetPair):
    planet1 = planetPair["from"]
    planet2 = planetPair["to"]
    massa1 = weights[planet1]
    massa2 = weights[planet2]
    massa1KG = convertKG(massa1)
    massa2KG = convertKG(massa2)
    distances = planetPair["distance"]
    distanceInMeters = convertAuToMeters(distances)

    attraction = aantrekking(massa1KG, massa2KG, distanceInMeters)

    print(
        f"{planet1} and {planet2} attract each other with {attraction} Newtons of force"
    )


for x in distances:
    getAttraction(x)
