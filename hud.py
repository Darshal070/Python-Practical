import tkinter as tk
import math

WIDTH = 900
HEIGHT = 700

root = tk.Tk()
root.title("IRON MAN HUD")
root.configure(bg="black")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT,
                   bg="black", highlightthickness=0)
canvas.pack()

angle = 0

def draw_hud():
    global angle

    canvas.delete("all")

    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    # Outer rotating ring
    for i in range(0, 360, 15):
        a = math.radians(i + angle)

        x1 = center_x + math.cos(a) * 220
        y1 = center_y + math.sin(a) * 220

        x2 = center_x + math.cos(a) * 260
        y2 = center_y + math.sin(a) * 260

        canvas.create_line(
            x1, y1, x2, y2,
            fill="#00FFFF",
            width=3
        )

    # Inner circle
    canvas.create_oval(
        center_x - 150,
        center_y - 150,
        center_x + 150,
        center_y + 150,
        outline="#00FFFF",
        width=3
    )

    # Radar sweep
    radar_angle = math.radians(angle * 2)

    radar_x = center_x + math.cos(radar_angle) * 180
    radar_y = center_y + math.sin(radar_angle) * 180

    canvas.create_line(
        center_x,
        center_y,
        radar_x,
        radar_y,
        fill="#00FF88",
        width=4
    )

    # Center glow
    canvas.create_oval(
        center_x - 20,
        center_y - 20,
        center_x + 20,
        center_y + 20,
        fill="#00FFFF",
        outline=""
    )

    # HUD text
    canvas.create_text(
        center_x,
        50,
        text="JARVIS ONLINE",
        fill="white",
        font=("Consolas", 28, "bold")
    )

    canvas.create_text(
        center_x,
        HEIGHT - 40,
        text="TARGETING SYSTEM ACTIVE",
        fill="#00FF88",
        font=("Consolas", 16)
    )

    angle += 2

    root.after(30, draw_hud)

draw_hud()

root.mainloop()
