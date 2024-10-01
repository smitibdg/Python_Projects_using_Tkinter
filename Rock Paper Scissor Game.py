import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

# Initialize scores and rounds
player_score = 0
computer_score = 0
rounds = 5
current_round = 0

# Function to play the game and display results
def play_game(player_choice):
    global player_score, computer_score, current_round
    
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You won this round!"
        player_score += 1
    else:
        result = "Computer wins this round!"
        computer_score += 1
    
    current_round += 1

    if current_round < rounds:
        result_label.config(text=f"Round {current_round}/{rounds}\nYour choice: {player_choice}\nComputer's choice: {computer_choice}\n{result}",
                            bg="gold1", font='Candara', fg="black")
    else:
        # Show final result and hide game buttons
        final_result = determine_final_winner()
        result_label.config(text=f"Final Score:\nYou: {player_score}\nComputer: {computer_score}\n{final_result}", bg="gold1", font='Candara', fg="black")
        hide_game_buttons()

# Function to determine the final winner
def determine_final_winner():
    if player_score > computer_score:
        return "Congratulations, You win the game!"
    elif computer_score > player_score:
        return "Computer wins the game!"
    else:
        return "It's a tie game!"

# Function to start the game
def start_game():
    global player_score, computer_score, current_round
    player_score = 0
    computer_score = 0
    current_round = 0
    
    welcome_label.pack_forget()  # Hide the welcome message
    start_button.pack_forget()   # Hide the start button
    exit_button.pack_forget()    # Hide the exit button
    show_game_buttons()          # Show the game buttons

# Function to exit the game
def exit_game():
    root.destroy()

# Function to show game buttons after the welcome message
def show_game_buttons():
    title_label.pack(pady=10)
    rock_button.pack(pady=10)
    paper_button.pack(pady=10)
    scissors_button.pack(pady=10)
    result_label.pack(pady=10)

# Function to hide game buttons after 5 rounds
def hide_game_buttons():
    rock_button.pack_forget()
    paper_button.pack_forget()
    scissors_button.pack_forget()

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissor")
root.geometry("700x500")
root.configure(bg='white')

# Load the background image
background_image = Image.open("RPS_image.jpg")
background_image = background_image.resize((1500, 1500), Image.LANCZOS)  # Resize the image to fit the window
bg_image = ImageTk.PhotoImage(background_image)

# Create a label for the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Place the background label in the window


# Welcome message and Start button
welcome_label = tk.Label(root, text="Hello, Smiti!\nWelcome to Rock Paper Scissors Game\nThere are 5 Rounds in this Game\nAre you ready to play?",
                         font=('Candara', 16, 'bold'), bg='plum', fg='white')
welcome_label.pack(pady=40)

start_button = tk.Button(root, text="Play", font=('Candara', 12), bg='#4CAF50', fg='white', width=10, command=start_game)
start_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", font=('Candara', 12), bg='#FF6347', fg='white', width=10, command=exit_game)
exit_button.pack(pady=10)

# Game title label (initially hidden)
title_label = tk.Label(root, text="Rock Paper Scissor Game", font=('Candara', 14, 'bold'), bg='DarkOrchid2', fg='white')

# Game buttons (initially hidden)
rock_button = tk.Button(root, text="Rock", font='Candara', width=10, bg="hotpink1", command=lambda: play_game('Rock'))
paper_button = tk.Button(root, text="Paper", font='Candara', width=10, bg="skyblue1", command=lambda: play_game('Paper'))
scissors_button = tk.Button(root, text="Scissors", font='Candara', width=10, bg="greenyellow", command=lambda: play_game('Scissors'))

# Result label (initially hidden)
result_label = tk.Label(root, text="", font=('Candara', 12), bg='white')

# Start the Tkinter main loop
root.mainloop()
