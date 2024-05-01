# Opthotool Front End  - DISTANCE_TOOL
# Author : Shriya Gandotra
# Date updated : 3/28/2024

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import math
import Components as MAIN

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
            line = canvas.create_line(point1[0], point1[1], point2[0], point2[1], fill="black", width=2)

    def set_point(event):
        nonlocal point1, point2, point1_oval, point2_oval
        if image_loaded:
            if point1 is None:
                point1 = (event.x, event.y)
                point1_oval = canvas.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5, outline="black", width=0.5, fill="black")
            elif point2 is None:
                point2 = (event.x, event.y)
                point2_oval = canvas.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5, outline="black", width=0.5, fill="black")
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
    calculator_window.configure(bg="white")
    calculator_window.geometry("700x750")

    optho_label = tk.Label(calculator_window, text ="OPTHOTOOL TECHNOLOGY", width=200, height=2, font = "Karla 10 bold", borderwidth=2, relief="groove")
    optho_label.config(bg= "#4990FB", fg= "white")
    optho_label.pack(pady = 0)

    calculator_window.resizable(False, False)

    frame = ttk.Frame(calculator_window)
    frame.pack()

    # Create and configure the canvas
    canvas = tk.Canvas(frame, width=640, height=640)  
    canvas.place(y = 40)
    canvas.pack(fill="both", expand=True)


    # Measure tool button
    measure_button = tk.Button(calculator_window, text="Meaurement Tool", command=toggle_measure_mode, borderwidth=0, bg='#4990FB',font="Karla 10 bold", fg='white', padx= 5 , pady = 5)
    measure_button.place(x = 290, y = 700)

    open_image()
