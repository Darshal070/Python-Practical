import tkinter as tk
import random
import math

WIDTH = 1000
HEIGHT = 700

root = tk.Tk()
root.title("🌌 Black Hole Simulator")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT,
                   bg="black", highlightthickness=0)
canvas.pack()

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

particles = []

class Particle:
    def __init__(self):
        self.angle = random.uniform(0, math.pi * 2)
        self.distance = random.randint(80, 350)

        self.speed = random.uniform(0.01, 0.05)

        self.size = random.randint(2, 5)

        self.color = random.choice([
            "#00FFFF",
            "#FF00FF",
            "#00FF88",
            "#FFFFFF",
            "#FFD700"
        ])

    def update(self):
        self.angle += self.speed

        # Spiral inward slowly
        self.distance -= 0.1

        if self.distance < 20:
            self.distance = random.randint(250, 350)

        self.x = CENTER_X + math.cos(self.angle) * self.distance
        self.y = CENTER_Y + math.sin(self.angle) * self.distance

    def draw(self):
        glow = self.size * 2

        # Glow
        canvas.create_oval(
            self.x - glow,
            self.y - glow,
            self.x + glow,
            self.y + glow,
            fill=self.color,
            outline=""
        )

        # Core particle
        canvas.create_oval(
            self.x - self.size,
            self.y - self.size,
            self.x + self.size,
            self.y + self.size,
            fill="white",
            outline=""
        )

# Create particles
for _ in range(250):
    particles.append(Particle())

def animate():
    canvas.delete("all")

    # Black hole glow
    for i in range(8):
        size = 60 + i * 15

        color = f"#{20+i*10:02x}00{40+i*20:02x}"

        canvas.create_oval(
            CENTER_X - size,
            CENTER_Y - size,
            CENTER_X + size,
            CENTER_Y + size,
            outline=color,
            width=3
        )

    # Black hole center
    canvas.create_oval(
        CENTER_X - 40,
        CENTER_Y - 40,
        CENTER_X + 40,
        CENTER_Y + 40,
        fill="black",
        outline="#00FFFF",
        width=3
    )

    # Draw particles
    for p in particles:
        p.update()
        p.draw()

    # Title
    canvas.create_text(
        WIDTH//2,
        40,
        text="BLACK HOLE SIMULATION",
        fill="white",
        font=("Consolas", 24, "bold")
    )

    root.after(16, animate)

animate()

root.mainloop()
