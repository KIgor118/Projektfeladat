import tkinter as tk
from random import randint
import os
from KI_fajlkezeles import dobas_mentes, dobas_betoltes, szamlalo_mentes, szamlalo_betoltes

class KI_kocka:
    def __init__(self, root):
        self.root = root
        self.root.title("app")
        self.elozmeny = "elozmenyek.txt"
        self.szamlalo = "szamlalo.txt"
        self.dobas_szamlalo = {i: 0 for i in range(1, 7)}

        # Felhasználói felület elemek
        self.label = tk.Label(root, text="Dobás eredménye: ", font=("Arial", 16))
        self.label.pack(pady=10)

        self.result_label = tk.Label(root, text="?", font=("Arial", 36))
        self.result_label.pack(pady=10)

        self.roll_button = tk.Button(root, text="Dobás", command=self.dobas, font=("Arial", 14))
        self.roll_button.pack(pady=10)

        self.history_label = tk.Label(root, text="Előző dobások:", font=("Arial", 14))
        self.history_label.pack(pady=10)

        self.history_text = tk.Text(root, height=10, width=30, state="disabled")
        self.history_text.pack(pady=10)

        self.counts_label = tk.Label(root, text="Gyakoriság:", font=("Arial", 14))
        self.counts_label.pack(pady=10)

        self.counts_text = tk.Text(root, height=6, width=30, state="disabled")
        self.counts_text.pack(pady=10)

        self.clear_button = tk.Button(root, text="Előzmények törlése", command=self.torles, font=("Arial", 12))
        self.clear_button.pack(pady=10)

        # Előző dobások és gyakoriság betöltése
        self.elozmenyek_betoltese()
        self.szamlalo_betoltese()

    def dobas(self):
        result = randint(1, 6)
        self.result_label.config(text=str(result))
        dobas_mentes(self.elozmeny, result)
        self.elozmenyek_frissit(result)
        self.szamlalo_frissit(result)

    def elozmenyek_betoltese(self):
        history = dobas_betoltes(self.elozmeny)
        for line in history:
            self.elozmenyek_frissit(int(line.strip()))

    def elozmenyek_frissit(self, result):
        self.history_text.config(state="normal")
        self.history_text.insert("end", f"{result}\n")
        self.history_text.config(state="disabled")

    def szamlalo_frissit(self, result):
        self.dobas_szamlalo[result] += 1
        szamlalo_mentes(self.szamlalo, self.dobas_szamlalo)
        self.szamlalo_frissit_kiiras()

    def szamlalo_betoltese(self):
        self.dobas_szamlalo = szamlalo_betoltes(self.szamlalo)
        self.szamlalo_frissit_kiiras()

    def szamlalo_frissit_kiiras(self):
        self.counts_text.config(state="normal")
        self.counts_text.delete("1.0", "end")
        for num, count in self.dobas_szamlalo.items():
            self.counts_text.insert("end", f"{num}: {count} db\n")
        self.counts_text.config(state="disabled")

    def torles(self):
        if os.path.exists(self.elozmeny):
            os.remove(self.elozmeny)
        if os.path.exists(self.szamlalo):
            os.remove(self.szamlalo)

        self.history_text.config(state="normal")
        self.history_text.delete("1.0", "end")
        self.history_text.config(state="disabled")

        self.dobas_szamlalo = {i: 0 for i in range(1, 7)}
        self.szamlalo_frissit_kiiras()

if __name__ == "__main__":
    root = tk.Tk()
    app = KI_kocka(root)
    root.mainloop()