### Author: Carolus ###


import tkinter as tk
from tkinter import messagebox
import random

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Set the dimensions of the window
window.geometry("200x150")

# Set the background color of the window
window.configure(bg='light blue')

# Create the game logic
def game(player_choice):
    # List of possible computer choices
    choices = ['rock', 'paper', 'scissors']
    # Choose a random choice for the computer
    computer_choice = random.choice(choices)

    # Determine the winner
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif player_choice == 'rock' and computer_choice == 'scissors':
        result = "You win!"
    elif player_choice == 'paper' and computer_choice == 'rock':
        result = "You win!"
    elif player_choice == 'scissors' and computer_choice == 'paper':
        result = "You win!"
    else:
        result = "You lose!"

    # Show the result in a message box
    messagebox.showinfo("Result", result)

# Create the buttons for each choice
button_rock = tk.Button(window, text="Rock", command=lambda: game('rock'), bg='light green')
button_paper = tk.Button(window, text="Paper", command=lambda: game('paper'), bg='light pink')
button_scissors = tk.Button(window, text="Scissors", command=lambda: game('scissors'), bg='light yellow')

# Place the buttons on the window
button_rock.pack()
button_paper.pack()
button_scissors.pack()

# Run the main loop
window.mainloop()
