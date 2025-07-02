import tkinter as tk
import random

# Initialize scores
player_score = 0
computer_score = 0

def play(user_choice):
    global player_score, computer_score

    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        player_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    result_var.set(f"You chose {user_choice.capitalize()} | "
                   f"Computer chose {computer_choice.capitalize()}\n{result}")

    score_var.set(f"Player: {player_score} | Computer: {computer_score}")

def reset():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    result_var.set("Make your move!")
    score_var.set("Player: 0 | Computer: 0")

def exit_game():
    root.destroy()

# Create window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("500x300")
root.config(bg="#f0f0f0")

# Title label
title = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 20, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Result display
result_var = tk.StringVar()
result_var.set("Make your move!")

result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=5)

# Score display
score_var = tk.StringVar()
score_var.set("Player: 0 | Computer: 0")

score_label = tk.Label(root, textvariable=score_var, font=("Arial", 12, "bold"), bg="#f0f0f0")
score_label.pack(pady=5)

# Buttons frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=12, command=lambda: play('rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=12, command=lambda: play('paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=12, command=lambda: play('scissors'))
scissors_button.grid(row=0, column=2, padx=10)

# Reset and Exit buttons
control_frame = tk.Frame(root, bg="#f0f0f0")
control_frame.pack(pady=10)

reset_button = tk.Button(control_frame, text="Reset", width=10, command=reset, bg="#d9ead3")
reset_button.grid(row=0, column=0, padx=10)

exit_button = tk.Button(control_frame, text="Exit", width=10, command=exit_game, bg="#f4cccc")
exit_button.grid(row=0, column=1, padx=10)

root.mainloop()
