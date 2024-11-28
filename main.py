import tkinter as tk
from random import randint
from KI_fajlkezeles import *

class KI_kocka:
    def __init__(self, root):
        self.root = root
        self.root.title("app")
        self.elozmeny = "elozmenyek.txt"
        self.szamlalo = "szamlalo.txt"
        self.dobas_szamlalo = {i: 0 for i in range(1, 7)}


        self.label = tk.Label(root, text="Dobás eredménye: ", font=("Arial", 16))
        self.label.pack(pady=10)

        self.eredmeny = tk.Label(root, text="?", font=("Arial", 36))
        self.eredmeny.pack(pady=10)

        self.dobas = tk.Button(root, text="Dobás", command=self.dobas, font=("Arial", 14))
        self.dobas.pack(pady=10)

        self.elozo = tk.Label(root, text="Előző dobások:", font=("Arial", 14))
        self.elozo.pack(pady=10)

        self.elozmenyek = tk.Text(root, height=10, width=30, state="disabled")
        self.elozmenyek.pack(pady=10)

        self.gyakorisag = tk.Label(root, text="Gyakoriság:", font=("Arial", 14))
        self.gyakorisag.pack(pady=10)

        self.szamlalo_doboz = tk.Text(root, height=6, width=30, state="disabled")
        self.szamlalo_doboz.pack(pady=10)

        self.eloz_torles = tk.Button(root, text="Előzmények törlése", command=self.torles, font=("Arial", 12))
        self.eloz_torles.pack(pady=10)


        self.elozmenyek_betoltese()
        self.szamlalo_betoltese()

    def dobas(self):
        eredmeny = randint(1, 6)
        self.eredmeny.config(text=str(eredmeny))
        dobas_mentes(self.elozmeny, eredmeny)
        self.elozmenyek_frissit(eredmeny)
        self.szamlalo_frissit(eredmeny)

    def elozmenyek_betoltese(self):
        elozmenyek = dobas_betoltes(self.elozmeny)
        for line in elozmenyek:
            self.elozmenyek_frissit(int(line.strip()))

    def elozmenyek_frissit(self, eredmeny):
        self.elozmenyek.config(state="normal")
        self.elozmenyek.insert("end", f"{eredmeny}\n")
        self.elozmenyek.config(state="disabled")

    def szamlalo_frissit(self, eredmeny):
        self.dobas_szamlalo[eredmeny] += 1
        szamlalo_mentes(self.szamlalo, self.dobas_szamlalo)
        self.szamlalo_frissit_kiiras()

    def szamlalo_betoltese(self):
        self.dobas_szamlalo = szamlalo_betoltes(self.szamlalo)
        self.szamlalo_frissit_kiiras()

    def szamlalo_frissit_kiiras(self):
        self.szamlalo_doboz.config(state="normal")
        self.szamlalo_doboz.delete("1.0", "end")
        for num, count in self.dobas_szamlalo.items():
            self.szamlalo_doboz.insert("end", f"{num}: {count} db\n")
        self.szamlalo_doboz.config(state="disabled")

    def torles(self):
        if os.path.exists(self.elozmeny):
            os.remove(self.elozmeny)
        if os.path.exists(self.szamlalo):
            os.remove(self.szamlalo)

        self.elozmenyek.config(state="normal")
        self.elozmenyek.delete("1.0", "end")
        self.elozmenyek.config(state="disabled")

        self.dobas_szamlalo = {i: 0 for i in range(1, 7)}
        self.szamlalo_frissit_kiiras()

if __name__ == "__main__":
    root = tk.Tk()
    app = KI_kocka(root)
    root.mainloop()