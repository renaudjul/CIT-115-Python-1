# Name: Julie Renaud
# Date: 2/16/2022
# Course: CIT 115
# Email: jmrenaud2001@student.stcc.edu
# Assignment: InterPlanetaryWeights


# constants of each planet's surface gravity factor
MERCURY = 0.38
VENUS = 0.91
MOON = 0.165
MARS = 0.38
JUPITER = 2.34
SATURN = 0.93
URANUS = 0.92
NEPTUNE = 1.12
PLUTO = 0.066


# Inputs
sName = input("Enter your name: ")
fEarthWeight = float(input("Enter your earth weight: \n"))

# Calculations
fMercuryWeight = fEarthWeight * MERCURY
fVenusWeight = fEarthWeight * VENUS
fMoonWeight = fEarthWeight * MOON
fMarsWeight = fEarthWeight * MARS
fJupiterWeight = fEarthWeight * JUPITER
fSaturnWeight = fEarthWeight * SATURN
fUranusWeight = fEarthWeight * URANUS
fNeptuneWeight = fEarthWeight * NEPTUNE
fPlutoWeight = fEarthWeight * PLUTO


# Output
print(sName + ", here are your weights on our Solar System's planets: \n")
print("Weight on Mercury: " + format(fMercuryWeight, '.2f'))
print("Weight on Venus: " + format(fVenusWeight, '.2f'))
print("Weight on Moon: " + format(fMoonWeight, '.2f'))
print("Weight on Mars: " + format(fMarsWeight, '.2f'))
print("Weight on Jupiter: " + format(fJupiterWeight, '.2f'))
print("Weight on Saturn: " + format(fSaturnWeight, '.2f'))
print("Weight on Uranus: " + format(fUranusWeight, '.2f'))
print("Weight on Neptune: " + format(fNeptuneWeight, '.2f'))
print("Weight on Pluto: " + format(fPlutoWeight, '.2f'))
print("\nThanks for playing!")
