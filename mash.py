from random import *

Race = ["Human", "Awoken", "Exo"]

Class = ["Hunter", "Titan", "Warlock"]

Element = ["Void", "Arc", "Solar"]

Enemy = ["Hive", "Cabal", "Vex", "the Fallen"]


myRace = raw_input("What race are you")

Race.append(myRace)

randomRace = choice(Race)

print("You're a", randomRace)


myClass = raw_input("What class are you")

Class.append(myClass)

randomClass = choice(Class)

print("You're a", randomClass)


myElement = raw_input("What element do you manipulate")

Element.append(myElement)

randomElement = choice(Element)

print("You are a", randomElement, "user.")


myEnemy = raw_input("Who are your greatest enemies")

Enemy.append(myEnemy)

randomEnemy = choice(Enemy)

print("The", randomEnemy, "are your natural foes")