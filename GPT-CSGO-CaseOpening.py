import random
import time
from termcolor import colored
import os

os.system("clear")

red = "\033[91m"
yellow = "\033[93m"
gold = "\033[33m"
blue = "\033[94m"  # Farba modrej
reset = "\033[0m"

def CaseOpening():
    print("+" + "-"*27 + "+")
    print("CSGO Case Opening Simulator")
    print("+" + "-"*27 + "+\n")
    print("Started opening '10' Cases ...")

CaseOpening()
time.sleep(0.2)

skins = [
    {"meno": f"{red}AK-47 | Bloodsport{reset}", "sance": 15},
    {"meno": f"{blue}M4A1-S | Knight{reset}", "sance": 6},
    {"meno": f"{gold}AWP | Dragon Lore{reset}", "sance": 2},  # Zmenená šanca na 2
    {"meno": f"{yellow}M4A4 | Howl{reset}", "sance": 3},  # Zmenená šanca na 3
    {"meno": f"{blue}AK-47 | Head Shot{reset}", "sance": 19},
    {"meno": f"{blue}P2000 | Wicked Sick{reset}", "sance": 21},
    {"meno": f"{blue}AWP | Duality{reset}", "sance": 13},
    {"meno": f"{blue}UMP-45 | Wild Child{reset}", "sance": 6},
    {"meno": f"{blue}P90 | Neoqueen{reset}", "sance": 18},
    {"meno": f"{blue}M4A1-S | Emphorosaur-S{reset}", "sance": 16},
    {"meno": f"{blue}MAC-10 | Sakkaku{reset}", "sance": 10},
    {"meno": f"{blue}R8 Revolver | Banana Cannon{reset}", "sance": 10},
    {"meno": f"{blue}MP5-SD | Liquidation{reset}", "sance": 20}
    # Pridajte ďalšie skiny s menami a percentuálnymi šancami
]

# Celková šanca všetkých skinov
celkova_sanca = sum(skin["sance"] for skin in skins)

for i in range(99):
    akt_skins = skins.copy()
    vygenerovane_skiny = []

    while celkova_sanca > 0:
        nahodny_skin = random.choice(akt_skins)
        if random.random() * 100 < nahodny_skin["sance"]:
            vygenerovane_skiny.append(nahodny_skin)
            celkova_sanca -= nahodny_skin["sance"]

    for vygenerovany_skin in vygenerovane_skiny:
        time.sleep(1)
        vypis = f"Vygenerovaný náhodný skin: {colored(vygenerovany_skin['meno'], 'white')}"
        print(vypis)
