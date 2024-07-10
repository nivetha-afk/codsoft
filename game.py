import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors")
        self.root.geometry("300x200")

        self.player_score = 0
        self.computer_score = 0

        self.player_score_label = tk.Label(self.root, text="Player Score: 0", font=("Helvetica", 14))
        self.player_score_label.grid(row=0, column=0, padx=10, pady=10)

        self.computer_score_label = tk.Label(self.root, text="Computer Score: 0", font=("Helvetica", 14))
        self.computer_score_label.grid(row=0, column=1, padx=10, pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play("rock"), font=("Helvetica", 14))
        self.rock_button.grid(row=2, column=0, padx=10, pady=10)

        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play("paper"), font=("Helvetica", 14))
        self.paper_button.grid(row=2, column=1, padx=10, pady=10)

        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play("scissors"), font=("Helvetica", 14))
        self.scissors_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def play(self, player_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            result = "Player wins!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.result_label.config(text=f"Player: {player_choice}, Computer: {computer_choice}, {result}")
        self.player_score_label.config(text=f"Player Score: {self.player_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()
