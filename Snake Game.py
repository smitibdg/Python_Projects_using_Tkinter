import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk, ImageFilter

class SnakeGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake Game")
        self.display_image()

    def display_image(self):
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.snake_image = Image.open("snake_image.jpg")
        self.snake_image = self.snake_image.resize((800, 600))
        self.snake_image = ImageTk.PhotoImage(self.snake_image)
        self.canvas.create_image(0, 0, image=self.snake_image, anchor="nw")
        self.root.after(3000, self.remove_image)

    def remove_image(self):
        self.canvas.delete("all")
        self.snake_image1 = Image.open("snake_image1.jpg")
        self.snake_image1 = self.snake_image1.resize((800, 600))
        self.snake_image1 = ImageTk.PhotoImage(self.snake_image1)
        self.canvas.create_image(0, 0, image=self.snake_image1, anchor="nw")
        self.root.after(1000, self.welcome_message)

    def welcome_message(self):
        self.canvas.create_text(400, 200, text="Hello, welcome to the game of Snake!", font=("Candara", 24))
        self.canvas.create_text(400, 250, text="Are you ready to play?", font=("Candara", 18))
        self.button_frame = tk.Frame(self.root, bg="limegreen", highlightbackground="forestgreen", highlightthickness=5)
        self.button_frame.place(x=340, y=280)
        self.play_button = tk.Button(self.button_frame, text="Play", command=self.start_game, bg="green", fg="white", relief=tk.RAISED, borderwidth=5)
        self.play_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.root.destroy, bg="red", fg="white", relief=tk.RAISED, borderwidth=5)
        self.exit_button.pack(side=tk.LEFT, padx=10, pady=10)

    def start_game(self):
        self.button_frame.destroy()
        self.canvas.delete("all")
        self.canvas.config(bg="black")
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.apple = (400, 300)
        self.direction = 'RIGHT'
        self.score = 0
        self.draw_snake()
        self.draw_apple()
        self.draw_score()
        self.root.bind("<Key>", self.key_press)
        self.update()

    def draw_snake(self):
        self.canvas.delete("snake")
        for i, pos in enumerate(self.snake):
            if i == 0:
                self.canvas.create_oval(pos[0], pos[1], pos[0] + 20, pos[1] + 20, fill="green", tag="snake")
            else:
                self.canvas.create_oval(pos[0], pos[1], pos[0] + 20, pos[1] + 20, fill="lightgreen", tag="snake")

    def draw_apple(self):
        self.canvas.delete("apple")
        self.canvas.create_oval(self.apple[0], self.apple[1], self.apple[0] + 20, self.apple[1] + 20, fill="red", tag="apple")

    def draw_score(self):
        self.canvas.delete("score")
        self.canvas.create_text(750, 20, text="Score: " + str(self.score), font=("Candara", 16), tag="score", fill="white")

    def update(self):
        head = self.snake[-1]
        if self.direction == 'UP':
            new_head = (head[0], head[1] - 20)
        elif self.direction == 'DOWN':
            new_head = (head[0], head[1] + 20)
        elif self.direction == 'LEFT':
            new_head = (head[0] - 20, head[1])
        elif self.direction == 'RIGHT':
            new_head = (head[0] + 20, head[1])

        if new_head[0] < 0:
            new_head = (800 - 20, new_head[1])
        elif new_head[0] > 800 - 20:
            new_head = (0, new_head[1])
        if new_head[1] < 0:
            new_head = (new_head[0], 600 - 20)
        elif new_head[1] > 600 - 20:
            new_head = (new_head[0], 0)

        if new_head in self.snake[:-1]:
            self.game_over()
            return

        if new_head == self.apple:
            self.apple = (random.randint(0, 39) * 20, random.randint(0, 29) * 20)
            self.score += 1
        else:
            self.snake.pop(0)

        self.snake.append(new_head)
        self.draw_snake()
        self.draw_apple()
        self.draw_score()
        self.root.after(100, self.update)

    def game_over(self):
        self.canvas.delete("all")
        self.snake_image1 = Image.open("snake_image1.jpg")
        self.snake_image1 = self.snake_image1.resize((800, 600))
        self.snake_image1 = ImageTk.PhotoImage(self.snake_image1)
        self.canvas.create_image(0, 0, image=self.snake_image1, anchor="nw")
        self.canvas.image = self.snake_image1
        self.canvas.create_text(400, 200, text="Game Over! You Lost!", font=("Candara", 24))
        self.canvas.create_text(400, 250, text="Your final score is: " + str(self.score), font=("Candara", 18))
        self.button_frame = tk.Frame(self.root, bg="limegreen", highlightbackground="forestgreen", highlightthickness=5)
        self.button_frame.place(x=325, y=280)
        self.play_again_button = tk.Button(self.button_frame, text="Play Again", command=self.play_again, bg="green", fg="white", relief=tk.RAISED, borderwidth=5)
        self.play_again_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.root.destroy, bg="red", fg="white", relief=tk.RAISED, borderwidth=5)
        self.exit_button.pack(side=tk.LEFT, padx=10, pady=10)
    
    def play_again(self):
        self.play_again_button.destroy()
        self.exit_button.destroy()
        self.start_game()

    def key_press(self, event):
        if event.keysym == 'Up' and self.direction != 'DOWN':
            self.direction = 'UP'
        elif event.keysym == 'Down' and self.direction != 'UP':
            self.direction = 'DOWN'
        elif event.keysym == 'Left' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif event.keysym == 'Right' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
