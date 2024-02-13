import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
import math
from PIL import Image, ImageTk

# Global variables to store point coordinates and line
IMAGE_DIM = 6  # 6mm x 6mm assumption
height = 0  # height per pixel
width = 0  # width per pixel
point1 = None
point2 = None
point1_oval = None
point2_oval = None
line = None
measure_mode = False
image_loaded = False

def calc_image_size(pixel_width, pixel_height):
    global width, height, IMAGE_DIM

    width = IMAGE_DIM / pixel_width
    height = IMAGE_DIM / pixel_height

# Function to calculate the distance
def calculate_distance():
    global point1, point2, line
    if point1 and point2:
        distance = math.sqrt(((point2[0] - point1[0]) * width) ** 2 + ((point2[1] - point1[1]) * height) ** 2)
        result_label.config(text=f"Distance: {distance:.2f} mm")
        # Draw a line between the two points
        if line:
            canvas.delete(line)
        line = canvas.create_line(point1[0], point1[1], point2[0], point2[1], fill="red", width=2)

# Function to set the selected point
def set_point(event):
    global point1, point2, point1_oval, point2_oval
    if image_loaded:
        if point1 is None:
            point1 = (event.x, event.y)
            point1_oval = canvas.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5, outline="red",
                                              width=0.5, fill="red")
        elif point2 is None:
            point2 = (event.x, event.y)
            point2_oval = canvas.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5, outline="red",
                                              width=0.5, fill="red")
            calculate_distance()

# Function to toggle measurement mode
def toggle_measure_mode():
    global point1, point2, point1_oval, point2_oval, line, measure_mode
    measure_mode = not measure_mode
    if measure_mode:
        measure_button.config(borderwidth=3)
        canvas.bind("<Button-1>", set_point)
    else:
        # reset button and clear the previous points
        measure_button.config(borderwidth=0)
        canvas.unbind("<Button-1>")
        if point1:
            canvas.delete(point1_oval)
        if point2:
            canvas.delete(point2_oval)
        if line:
            canvas.delete(line)
        point1 = None
        point2 = None
        result_label.config(text="Distance: N/A")

# Function to open an image file
def open_image():
    global image_area_pixels, image_loaded
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff")])
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)

        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo
        canvas.config(scrollregion=canvas.bbox(tk.ALL))
        if image:
            pixel_width = image.width
            pixel_height = image.height
            calc_image_size(pixel_width, pixel_height)
            canvas.config(width=pixel_width, height=pixel_height + 20)
            image_loaded = True 

# Create the main window
root = tk.Tk()
root.title("Image Distance Calculator")

# Create and configure the canvas
canvas = tk.Canvas(root, width=358, height=250)
canvas.pack()

# Create a frame for buttons
button_frame = ttk.Frame(root)
button_frame.pack()

# Open Image button
open_button = tk.Button(button_frame, text="Open Image", command=open_image)
open_button.grid(row=0, column=0)

# Measure tool button
measure_icon = Image.open(r"C:\Users\youse\OneDrive\Desktop\School\Senior Spring\VS Code\Senior Design\measure_button.png")
measure_icon = measure_icon.resize((20, 20))
measure_icon = ImageTk.PhotoImage(measure_icon)

# Measure tool button
#measure_button = tk.Button(button_frame, text="Meaurement Tool", command=toggle_measure_mode)
measure_button = tk.Button(button_frame, image=measure_icon, command=toggle_measure_mode)
measure_button.grid(row=0, column=1)

# Show Distance
result_label = tk.Label(button_frame, text="Distance: N/A")
result_label.grid(row=1, column=0)

root.mainloop()
