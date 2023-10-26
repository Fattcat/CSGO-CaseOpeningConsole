import os as vycistiMa

# Zoznam skinov s menami a prislusnymi percentualnymi sancami
skins = [
    {"meno": "AK-47 | Bloodsport", "sance": 1},
    {"meno": "M4A1-S | Knight", "sance": 1},
    {"meno": "AWP | Dragon Lore", "sance": 0.2},
    {"meno":"M4A4 | Temukau","sance":1},
    {"meno":"AK-47 | Head Shot","sance":1},
    {"meno":"P2000 | Wicked Sick","sance":1},
    {"meno":"AWP | Duality","sance":1},
    {"meno":"UMP-45 | Wild Child","sance":1},
    {"meno":"P90 | Neoqueen","sance":1},
    {"meno":"M4A1-S | Emphorosaur-S","sance":1},
    {"meno":"MAC-10 | Sakkaku","sance":1},
    {"meno":"R8 Revolver | Banana Cannon","sance":1},
    {"meno":"MP5-SD | Liquidation","sance":1},
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
