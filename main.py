import tkinter as tk
from random import randint
import os

class DiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("app")
        self.history_file = "dice_history.txt"
        self.counts_file = "dice_counts.txt"
        self.roll_counts = {i: 0 for i in range(1, 7)}

        # Felhasználói felület elemek
        self.label = tk.Label(root, text="Dobókocka eredmény: ", font=("Arial", 16))
        self.label.pack(pady=10)

        self.result_label = tk.Label(root, text="?", font=("Arial", 36))
        self.result_label.pack(pady=10)

        self.roll_button = tk.Button(root, text="Dobás", command=self.roll_dice, font=("Arial", 14))
        self.roll_button.pack(pady=10)

        self.history_label = tk.Label(root, text="Előző dobások:", font=("Arial", 14))
        self.history_label.pack(pady=10)

        self.history_text = tk.Text(root, height=10, width=30, state="disabled")
        self.history_text.pack(pady=10)

        self.counts_label = tk.Label(root, text="Gyakoriság:", font=("Arial", 14))
        self.counts_label.pack(pady=10)

        self.counts_text = tk.Text(root, height=6, width=30, state="disabled")
        self.counts_text.pack(pady=10)

        self.clear_button = tk.Button(root, text="Előzmények törlése", command=self.clear_history, font=("Arial", 12))
        self.clear_button.pack(pady=10)

        # Előző dobások és gyakoriság betöltése
        self.load_history()
        self.load_counts()

    def roll_dice(self):
        result = randint(1, 6)
        self.result_label.config(text=str(result))
        self.save_roll(result)
        self.update_history_display(result)
        self.update_counts(result)

    def save_roll(self, result):
        with open(self.history_file, "a") as file:
            file.write(f"{result}\n")

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as file:
                history = file.readlines()
                for line in history:
                    number = int(line.strip())
                    self.update_history_display(number)

    def update_history_display(self, result):
        self.history_text.config(state="normal")
        self.history_text.insert("end", f"{result}\n")
        self.history_text.config(state="disabled")

    def update_counts(self, result):
        self.roll_counts[result] += 1
        self.save_counts()
        self.update_counts_display()

    def save_counts(self):
        with open(self.counts_file, "w") as file:
            for num, count in self.roll_counts.items():
                file.write(f"{num}: {count}\n")

    def load_counts(self):
        if os.path.exists(self.counts_file):
            with open(self.counts_file, "r") as file:
                for line in file:
                    num, count = line.strip().split(": ")
                    self.roll_counts[int(num)] = int(count)
            self.update_counts_display()

    def update_counts_display(self):
        self.counts_text.config(state="normal")
        self.counts_text.delete("1.0", "end")
        for num, count in self.roll_counts.items():
            self.counts_text.insert("end", f"{num}: {count} db\n")
        self.counts_text.config(state="disabled")

    def clear_history(self):
        # Előzmények törlése
        if os.path.exists(self.history_file):
            os.remove(self.history_file)
        self.history_text.config(state="normal")
        self.history_text.delete("1.0", "end")
        self.history_text.config(state="disabled")

        # Gyakoriságok nullázása
        self.roll_counts = {i: 0 for i in range(1, 7)}
        self.update_counts_display()
        if os.path.exists(self.counts_file):
            os.remove(self.counts_file)


if __name__ == "__main__":
    root = tk.Tk()
    app = DiceApp(root)
    root.mainloop()
