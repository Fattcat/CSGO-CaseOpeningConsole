import random

# Zoznam skinov s menami a prislusnymi percentualnymi sancami
skins = [
    {"meno": "AK-47 | Bloodsport", "sance": 1},
    {"meno": "M4A1-S | Knight", "sance": 2},
    {"meno": "AWP | Dragon Lore", "sance": 0.1},
    # Pridajte ďalšie skiny s menami a percentuálnymi šancami
]

# Funkcia pre náhodný výber skinu
def nahodny_skin(skins):
    sance = [skin["sance"] for skin in skins]
    vybrany_skin = random.choices(skins, weights=sance, k=1)[0]
    return vybrany_skin

# Volanie funkcie pre získanie náhodného skinu
vygenerovany_skin = nahodny_skin(skins)

# Výpis náhodneho skinu
print(f"Vygenerovaný náhodný skin: {vygenerovany_skin['meno']}")

# Sem môžete pridať kód na otvorenie CS:GO Fracture Bedne
