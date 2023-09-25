import random

speler=input("steen, papier, schaar: ")

tegenstander=["steen","papier", "schaar"]
tegenstander= random.choice(tegenstander)
print("Tegenstander: "+ tegenstander)

if speler=="steen" and tegenstander=="schaar":
    print("Je hebt gewonnen")
elif speler=="schaar" and tegenstander=="papier":
    print("Je hebt gewonnen")
elif speler=="papier" and tegenstander=="steen":
    print("Je hebt gewonnen")
elif speler=="steen" and tegenstander=="papier":
    print("Je hebt verloren")
elif speler=="papier" and tegenstander=="schaar":
    print("Je hebt verloren")
elif speler=="schaar" and tegenstander=="steen":
    print("Je hebt verloren")
else: print("Gelijk spel")