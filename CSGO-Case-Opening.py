import os
from time import sleep
import random

# CSGO OPENING SIMULATOR

if os.name == "nt":  # Opraveno: Správné testování pro Windows
    sleep(0.3)
    os.system("cls")
    sleep(1)
else:
    sleep(0.3)
    os.system("clear")
    sleep(1)

Snipe_AWP = ["AWP", ["Safary Mesh", "Dragon Lore"]]
Snipe_SSG_08 = ["SSG-08", ["Blood Sport", "Dragonfire"]]
Butter_Fly_knifes = ["Butter Fly", ["Autotronic", "Lore", "Freehand"]]

# CAISKY
PrismaCase = ["M4A4 | The Emperor", "Five-SeveN | Angry Mob", "AUG | Momentum", "XM1014 | Incinegator"]
Prisma2Case = ["M4A1-S | Player Two", "Glock-18 | Bullet Queen", "MAC-10 | Disco Tech", "SSG 08 | Fever Dream"]
Fracture_Case = ["Desert Eagle | Printstream", "AK-47 | Legion of Anubis"]

# Sem treba pridať VŠETKY LISTY SKINOV
# ------------------------------------------------------------ #
FullList = [Snipe_AWP, Snipe_SSG_08, Butter_Fly_knifes]
# ------------------------------------------------------------ #

StatTrak = ["Yes", "No"]
OPOTREBENIE_SKINU = ["Factory New", "Minimal Wear", "Field Tested", "Well Worn"]

print("CSGO - Cases :")
print("1. Prisma Case")
print("2. Prisma 2 Case")
print("3. Fracture Case")
SelectCaseInput = input("napíšte číslo : ")

if SelectCaseInput == "1" or SelectCaseInput == "2" or SelectCaseInput == "3":
    CheckStatTrack = random.choice(StatTrak)

    if CheckStatTrack == "Yes":
        selected_skin = random.choice(FullList[int(SelectCaseInput) - 1][1])
    else:
        selected_skin = random.choice(FullList[int(SelectCaseInput) - 1][1])
    print("Vygenerovane : ")
    print(f"Zýskaný Skin : {selected_skin}")
else:
    print("Zadali jste nesprávný vstup. Zvolte číslo 1, 2 nebo 3 pro výběr krabice.")
