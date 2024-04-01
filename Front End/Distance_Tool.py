# Opthotool Front End  - DISTANCE_TOOL
# Author : Shriya Gandotra
# Date updated : 3/28/2024

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import math

# Global reference for the photo image to prevent garbage collection
photo = None

def create_distance_calculator():
    # Local variables for the distance calculator
    IMAGE_DIM = 6000  # 6mm x 6mm assumption
    height = 0  # height per pixel
    width = 0  # width per pixel
    point1 = None
    point2 = None
    point1_oval = None
    point2_oval = None
    line = None
    measure_mode = False
    image_loaded = False
    result_label = None
    distance = 0

    def calc_image_size(pixel_width, pixel_height):
        nonlocal width, height
        width = IMAGE_DIM / pixel_width
        height = IMAGE_DIM / pixel_height

    def calculate_distance():
        nonlocal distance, result_label, line
        if point1 and point2:
            distance = math.sqrt(((point2[0] - point1[0]) * width) ** 2 + ((point2[1] - point1[1]) * height) ** 2)
            x1, y1 = point1
            x2, y2 = point2
            midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
            if result_label is not None:
                result_label.destroy()
            result_label = tk.Label(calculator_window, text=f"{distance:.2f} um")
            result_label.place(x=midpoint[0], y=midpoint[1], anchor="center")
            if line:
                canvas.delete(line)
            line = canvas.create_line(point1[0], point1[1], point2[0], point2[1], fill="red", width=2)

    def set_point(event):
        nonlocal point1, point2, point1_oval, point2_oval
        if image_loaded:
            if point1 is None:
                point1 = (event.x, event.y)
                point1_oval = canvas.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5, outline="red", width=0.5, fill="red")
            elif point2 is None:
                point2 = (event.x, event.y)
                point2_oval = canvas.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5, outline="red", width=0.5, fill="red")
                calculate_distance()

    def toggle_measure_mode():
        nonlocal measure_mode, point1, point2, point1_oval, point2_oval, line
        measure_mode = not measure_mode
        if measure_mode:
            measure_button.config(relief="sunken")
            canvas.bind("<Button-1>", set_point)
        else:
            measure_button.config(relief="raised")
            canvas.unbind("<Button-1>")
            if point1_oval:
                canvas.delete(point1_oval)
            if point2_oval:
                canvas.delete(point2_oval)
            if line:
                canvas.delete(line)
            if result_label:
                result_label.destroy()
            point1 = None
            point2 = None

    def open_image():
        nonlocal image_loaded
        # Provide the path to your image
        file_path = "oct_test1/segmented_images/predicted_middle.png"
        try:
            # global photo
            image = Image.open(file_path)
            image = image.resize((640, 640))
            photo = ImageTk.PhotoImage(image)

            pixel_width, pixel_height = image.size
            calc_image_size(pixel_width, pixel_height)

            canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            canvas.image = photo  # Keep a reference to avoid garbage collection
            canvas.config(scrollregion=canvas.bbox(tk.ALL))

            image_loaded = True
        except Exception as e:
            print(f"Failed to load the image: {e}")

    # Create the new window for the distance calculator
    calculator_window = tk.Toplevel()
    calculator_window.title("Image Distance Calculator")

    calculator_window.resizable(False, False)

    # Create and configure the canvas
    canvas = tk.Canvas(calculator_window, width=640, height=650)  # Adjust size as needed
    canvas.pack(fill="both", expand=True)

    # Create a frame for buttons
    button_frame = ttk.Frame(calculator_window)
    button_frame.pack()

    # Measure tool button
    measure_button = tk.Button(button_frame, text="Meaurement Tool", command=toggle_measure_mode)
    measure_button.place(x = 320, y =610)
    measure_button.grid(row=0, column=1)

    open_image()