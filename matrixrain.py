import tkinter as tk
import random

# Window setup
WIDTH = 1000
HEIGHT = 600

root = tk.Tk()
root.title("💻 Matrix Rain")
root.configure(bg="black")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT,
                   bg="black", highlightthickness=0)
canvas.pack()

# Characters used in rain
chars = "DARSHAL"

font_size = 20
columns = WIDTH // font_size

drops = [random.randint(-HEIGHT, 0) for _ in range(columns)]

def draw_matrix():
    canvas.delete("all")

    for i in range(columns):
        x = i * font_size
        y = drops[i]

        char = random.choice(chars)

        # Bright green text
        canvas.create_text(
            x,
            y,
            text=char,
            fill="#00FF00",
            font=("Consolas", font_size, "bold")
        )

        # Randomly reset drop
        if y > HEIGHT and random.random() > 0.975:
            drops[i] = random.randint(-200, 0)

        drops[i] += font_size

    # Title
    canvas.create_text(
        WIDTH // 2,
        30,
        text="MATRIX TERMINAL",
        fill="white",
        font=("Consolas", 24, "bold")
    )

    root.after(50, draw_matrix)

draw_matrix()

root.mainloop()
