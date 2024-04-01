# AUTHOR: SHRIYA GANDOTRA
# This script is designed to dynamically create and manage tabs within a Tkinter GUI application. 
# It defines three main functions: Skeletonized mapping, Periemter Mapping and RAW OCT- B Sacn tabs

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter import ttk, Button, Toplevel, Label

def main_application(selected_file_path, master):
    # Define the function to create empty tabs
    def create_empty_tab(notebook, tab_text):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=tab_text)
        return frame

    # Define the function to update tabs with images
    def update_tab_with_image(frame, image_path):
        image = Image.open(image_path)
        img_resized = image.resize((400, 300))
        photo = ImageTk.PhotoImage(img_resized)
        label = Label(frame, image=photo)
        label.image = photo  # keep a reference!
        label.pack(padx=10, pady=10)

    # Function to call after file conversion to update the tabs with images
    def load_images(selected_file_path):
        global up_image, down_image

        if selected_file_path[-3:] == "OCT":
            print(selected_file_path)
            base_path = os.path.splitext(selected_file_path)[0]

            ## Create and add tabs with images based on the file type
            skeleton_image_path = os.path.join(base_path, "skeletonized_image/skeleton.png")
            perimeter_image_path = os.path.join(base_path, "perimeter_image/perimeter.png")

            # Updating tabs with images
            update_tab_with_image(skeleton_tab, skeleton_image_path)
            update_tab_with_image(perimeter_tab, perimeter_image_path)

            if raw_oct_b_tab:
                image_list = load_images_from_folder("oct_test1/raw_images")  # Adjust the folder path as necessary
                current_image_index = [0]  # Use a list for mutable integer

                # Create the notebook
                notebook = ttk.Notebook(master, width=400, height=300, style=f"{theme_name}.TNotebook")
                notebook.pack(expand=True, fill='both')
                notebook.place(x=550,y=470)

                # Create a frame for the Raw OCT-B tab
                raw_oct_b_frame = ttk.Frame(notebook)
                notebook.add(raw_oct_b_frame, text="Raw OCT-B")

                # Unified navigation command
                def update_image_index(direction):
                    current_image_index[0] = navigate_images(direction, image_list, current_image_index[0], image_label, image_number_label)

                image_frame = tk.Frame(raw_oct_b_frame)
                image_frame.grid(row=0, column=0, padx=10, pady=10)

                button_frame = tk.Frame(raw_oct_b_frame)
                button_frame.grid(row=0, column=1, padx=10, pady=10)

                image_label = tk.Label(image_frame, bg = '#dcdad5')
                image_label.pack()

                image_number_label = tk.Label(image_frame, text="0/0", anchor="se", bg = '#dcdad5')
                image_number_label.pack(side="bottom", fill="x")


                up1 = (Image.open("up_button.png"))
                up = up1.resize((25,20))

                down1 = (Image.open("down_button.png"))
                down = down1.resize((25,20))

                # Assume you have 'up_button.png' and 'down_button.png' in the current directory
                up_image = ImageTk.PhotoImage(up)
                down_image = ImageTk.PhotoImage(down)

                up_button = tk.Button(button_frame, image=up_image, command=lambda: update_image_index("previous"))
                up_button.pack(side="top", padx=0, pady=0)

                down_button = tk.Button(button_frame, image=down_image, command=lambda: update_image_index("next"))
                down_button.pack(side="top", padx=0, pady=0)
                
                show_image(image_label, image_list, current_image_index[0], image_number_label)

    def load_images_from_folder(folder_path):
        image_list = []
        for filename in os.listdir(folder_path):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                image_list.append(os.path.join(folder_path, filename))
        return image_list

    def update_image_number(image_number_label, current_image_index, total_images):
        image_number_label.config(text=f"{current_image_index + 1}/{total_images}")

    def show_image(image_label, image_list, current_image_index, image_number_label):
        if image_list:
            image_path = image_list[current_image_index]
            image = Image.open(image_path)
            image = image.resize((320, 260))
            photo = ImageTk.PhotoImage(image)
            image_label.config(image=photo)
            image_label.image = photo  # Keep a reference!
            update_image_number(image_number_label, current_image_index, len(image_list))

    def navigate_images(direction, image_list, current_image_index, image_label, image_number_label):
            if direction == "next":
                new_index = (current_image_index + 1) % len(image_list)
            else:  # Assuming direction == "previous"
                new_index = (current_image_index - 1) % len(image_list)
            show_image(image_label, image_list, new_index, image_number_label)
            return new_index
    
    # Setting up the style for the notebook and tabs
    style = ttk.Style()
    theme_name = style.theme_use('clam')
    style.configure(f"{theme_name}.TNotebook", background='white')
    style.configure(f"{theme_name}.TNotebook.Tab", background='white')
    style.configure(f"{theme_name}.TFrame", background='white')

    # Create the Notebook widget for skeletonized and perimeter images and position it
    notebook = ttk.Notebook(master, width=400, height=300, style=f"{theme_name}.TNotebook")
    notebook.pack(expand=True, fill="both")
    notebook.place(x=1000, y=110)  # Adjust the positioning as needed

    # Create the Notebook widget for raw OCT-B images and position it
    raw_notebook = ttk.Notebook(master, width=400, height=300, style=f"{theme_name}.TNotebook")
    raw_notebook.pack(expand=True, fill="both")
    raw_notebook.place(x=550, y=470)  # Adjust the positioning as needed


    # Create empty tabs
    skeleton_tab = create_empty_tab(notebook, "Skeletonized Map")
    perimeter_tab = create_empty_tab(notebook, "Perimeter Map")
    raw_oct_b_tab = create_empty_tab(raw_notebook, "Raw OCT-B")

    # Check if the file path is not None and is a string
    if selected_file_path and isinstance(selected_file_path, str):
        load_images(selected_file_path)
    else:
        print("No file selected or invalid file path")

