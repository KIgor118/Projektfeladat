import os

def dobas_mentes(file_name, result):
    with open(file_name, "a") as file:
        file.write(f"{result}\n")

def dobas_betoltes(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return file.readlines()
    return []

def szamlalo_mentes(file_name, counts):
    with open(file_name, "w") as file:
        for num, count in counts.items():
            file.write(f"{num}: {count}\n")

def szamlalo_betoltes(file_name):
    counts = {i: 0 for i in range(1, 7)}
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                num, count = line.strip().split(": ")
                counts[int(num)] = int(count)
    return counts
