import os
from time import sleep
import random

# CSGO OPENING SIMULATOR

if os.name("windows"):
    os.system("cls")
else:
    os.system("clear")
    
Snipe_AWP = ["AWP": ["Safary Mesh", ]]
Snipe_SSG_08 = ["SSG-08": ["Blood Sport", ]]

FullList = ["Snipe_AWP","Snipe_SSG_08","","","","","","","","","","",""]

print(""":CSGO - Cases : 
      1. Prisma Case
      2. Prisma 2 Case
      3. Fracture Case""")
SelectCaseInput = input("napíšte číslo : ")

vybrany_prvky = [random.choice(sublist) for _, sublist in Snipe_AWP,]

print(f"Vygenerované: {', '.join(vybrany_prvky)}")
