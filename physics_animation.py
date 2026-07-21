import tkinter as tk
import random
import math

WIDTH = 900
HEIGHT = 600
GRAVITY = 0.25
FRICTION = 0.98

root = tk.Tk()
root.title("✨ Fun Bouncing Ball Simulator")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

balls = []

colors = [
    "#ff4d4d", "#4dff88", "#4dd2ff",
    "#ffd24d", "#ff66ff", "#ffffff"
]

class Ball:
    def __init__(self, x, y):
        self.radius = random.randint(10, 25)
        self.x = x
        self.y = y

        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(4, 10)

        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed

        self.color = random.choice(colors)

        self.trail = []

    def update(self):
        self.dy += GRAVITY

        self.x += self.dx
        self.y += self.dy

        # Bounce walls
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.dx *= -FRICTION

        if self.y + self.radius >= HEIGHT:
            self.y = HEIGHT - self.radius
            self.dy *= -0.85

        # Save trail
        self.trail.append((self.x, self.y))

        if len(self.trail) > 15:
            self.trail.pop(0)

    def draw(self):
        # Draw trail
        for i, (tx, ty) in enumerate(self.trail):
            alpha = i / len(self.trail)
            size = self.radius * alpha

            canvas.create_oval(
                tx - size,
                ty - size,
                tx + size,
                ty + size,
                fill=self.color,
                outline=""
            )

        # Draw ball
        canvas.create_oval(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
            fill=self.color,
            outline="white",
            width=2
        )

def animate():
    canvas.delete("all")

    for ball in balls:
        ball.update()
        ball.draw()

    canvas.create_text(
        150,
        30,
        text="Click Anywhere to Spawn Balls 🎉",
        fill="white",
        font=("Arial", 18, "bold")
    )

    root.after(16, animate)

def create_ball(event):
    for _ in range(3):
        balls.append(Ball(event.x, event.y))

canvas.bind("<Button-1>", create_ball)

animate()
root.mainloop()
