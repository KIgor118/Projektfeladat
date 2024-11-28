import os

def dobas_mentes(fajl, eredmeny):
    with open(fajl, "a") as file:
        file.write(f"{eredmeny}\n")

def dobas_betoltes(fajl):
    if os.path.exists(fajl):
        with open(fajl, "r") as file:
            return file.readlines()
    return []

def szamlalo_mentes(fajl, gyak):
    with open(fajl, "w") as file:
        for szam, db in gyak.items():
            file.write(f"{szam}: {db}\n")

def szamlalo_betoltes(fajl):
    gyak = {i: 0 for i in range(1, 7)}
    if os.path.exists(fajl):
        with open(fajl, "r") as file:
            for line in file:
                szam, db = line.strip().split(": ")
                gyak[int(szam)] = int(db)
    return gyak
