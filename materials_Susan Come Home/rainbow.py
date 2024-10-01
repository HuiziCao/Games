

"""
macaron_light_blue = color_rgb(173, 216, 230)  
macaron_red = color_rgb(255, 105, 97)               
macaron_white = color_rgb(255, 250, 240)                  
macaron_black = color_rgb(0, 0, 0)  
macaron_brown = color_rgb(182, 142, 142)  
macaron_green = color_rgb(169, 209, 142)  
macaron_orange = color_rgb(255, 179, 71)    
macaron_pink = color_rgb(255, 182, 193)        
macaron_yellow = color_rgb(255, 255, 133)      
macaron_light_green = color_rgb(144, 238, 144) 
macaron_basket_brown = color_rgb(210, 180, 140)  
macaron_yellow = color_rgb(255, 255, 133)      
macaron_light_yellow = color_rgb(255, 255, 153)  


rainbow_red = color_rgb(255, 105, 97) 
rainbow_orange = color_rgb(255, 179, 71) 
rainbow_yellow = color_rgb(255, 255, 133)         
rainbow_green = color_rgb(139, 198, 139)
rainbow_cyan = color_rgb(135, 206, 235) 
rainbow_blue =color_rgb(153, 212, 247)
rainbow_purple = color_rgb(221, 160, 221)
"""

"""
import tkinter as tk
from tkinter import Canvas

# Creating the main window
root = tk.Tk()
root.title("Rainbow Drawing with Tkinter")

# Setting canvas size
canvas_width = 600
canvas_height = 400

# Creating a canvas
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Rainbow colors as provided
rainbow_colors = [
    "#FF6961",  # Red
    "#FFB347",  # Orange
    "#FFFF85",  # Yellow
    "#8BC68B",  # Green
    "#87CEEB",  # Cyan
    "#99D4F7",  # Blue
    "#DDA0DD"   # Purple
]

# Drawing the rainbow
for i, color in enumerate(rainbow_colors):
    x0 = canvas_width * (0.1 + i * 0.05)
    y0 = canvas_height * (0.8 - i * 0.05)
    x1 = canvas_width * (0.9 - i * 0.05)
    y1 = canvas_height * (0.2 + i * 0.05)
    canvas.create_arc(x0, y0, x1, y1, start=0, extent=180, fill=color, outline=color, width=10)

# Running the tkinter main loop
root.mainloop()
"""

import tkinter as tk

def draw_rainbow_circles(canvas, colors, start_x, start_y, radius):
    """ Draw circles in rainbow colors on the canvas. """
    for color in colors:
        canvas.create_oval(
            start_x - radius, start_y - radius,
            start_x + radius, start_y + radius,
            outline=color, fill=color
        )
        start_x += 2 * radius  # Move to the next position

# Setting up the main window
root = tk.Tk()
root.title("Rainbow Circles with Tkinter")

# Canvas size variables
canvas_width = 800
canvas_height = 200

# Creating the canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()


# Rainbow colors as specified
rainbow_colors = [
    "#FF6961",  # Red
    "#FFB347",  # Orange
    "#ffe338",  # Yellow
    "#8BC68B",  # Green
    "#6fd9cf",  # Cyan
    "#4c78ae",  # Blue
    "#DDA0DD"   # Purple
]

#FF6961",  # Red
#FFB347",  # Orange
    #ffe338",  # Yellow
    #8BC68B",  # Green
    #93D3D3",  # Cyan
    #9AD6F9",  # Blue
    #DDA0DD"   # Purple

# Draw the rainbow circles
draw_rainbow_circles(canvas, rainbow_colors, radius=50, start_x=50, start_y=canvas_height/2)

# Running the Tkinter loop
root.mainloop()
