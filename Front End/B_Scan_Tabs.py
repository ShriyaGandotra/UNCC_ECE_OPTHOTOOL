# AUTHOR: SHRIYA GANDOTRA
# This script is designed to dynamically create and manage tabs within a Tkinter GUI application. 
# It defines two main functions: Enface and Contour Mapping Tab

import tkinter as tk
from tkinter import ttk, Frame
from PIL import Image, ImageTk
import os
import Config as config

# Function to call after file conversion to update the tabs with images
def load_images(master):
    global up_image, down_image

    # Setting up the style for the notebook and tabs
    style = ttk.Style()
    theme_name = style.theme_use('clam')
    style.configure(f"{theme_name}.TNotebook", background='white')
    style.configure(f"{theme_name}.TNotebook.Tab", background='white')
    style.configure(f"{theme_name}.TFrame", background='white')

    image_list = load_images_from_folder("oct_test1/raw_images")  # Adjust the folder path as necessary
    current_image_index = [0]  # Use a list for mutable integer

    # Create the notebook
    notebook = ttk.Notebook(master, width=400, height=300,style=f"{theme_name}.TNotebook")
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

def b_tabs(master, frames, num_tabs_list, selected_file_path, tab_names_list):
    style = ttk.Style()
    theme_name = style.theme_use('clam')
    style.configure(f"{theme_name}.TNotebook", background='white')
    style.configure(f"{theme_name}.TNotebook.Tab", background='white')

    # Configure the background color for the content area of the tabs
    style.configure(f"{theme_name}.TFrame", background='white')

    for i, frame in enumerate(frames):
        # Check if the frame already has a tab control and destroy it
        for widget in frame.winfo_children():
            widget.destroy()

        # Create the main tab control 
        main_tabControl = ttk.Notebook(frame, style=f"{theme_name}.TNotebook")
        main_tabControl.config(width=400, height=300)  # Set the initial size of the notebook

        # Add tabs with names from the tab_names_list
        for j in range(num_tabs_list[i] + 1):  # +1 for the main tab
            tab_name = tab_names_list[i][j] if j < len(tab_names_list[i]) else f"Tab {j + 1}"
            tab = ttk.Frame(main_tabControl)
            main_tabControl.add(tab, text=tab_name)

            if j == 0 and selected_file_path and isinstance(selected_file_path, str) and len(selected_file_path) >= 3:

                if selected_file_path[-3:] == "OCT":
                        print(selected_file_path)
                        base_path = os.path.splitext(selected_file_path)[0]
                        print("error")
                        # full_path = os.path.join(base_path, "raw_images", "image_0_256.png")
                        # image_to_display = full_path
                        
                        if tab_name == "Enface":
                            enface_path = "oct_test1/enface_image/projection.png"  
                            # Call the function with the specified parameters
                            image_to_display = enface_path
                            try:
                                img = Image.open(image_to_display)
                                img_resized = img.resize((400, 300))
                                img_photo = ImageTk.PhotoImage(img_resized)
                                label = tk.Label(tab, image=img_photo)
                                label.image = img_photo  # keep a reference to the image
                                label.pack(padx=10, pady=10)
                            except Exception as e:
                                print(f"Error loading image from {image_to_display}: {e}")
                        
                        if tab_name == "Middle OCT-B":
                            middle_path = "oct_test1/raw_images/image_0_256.png"
                            # middle_index = len(middle_path) // 2
                            # middle_image_path = os.path.join(middle_path, middle_path[middle_index])
                            # Call the function with the specified parameters
                            image_to_display =  middle_path
                            try:
                                img = Image.open(image_to_display)
                                img_resized = img.resize((400, 300))
                                img_photo = ImageTk.PhotoImage(img_resized)
                                label = tk.Label(tab, image=img_photo)
                                label.image = img_photo  # keep a reference to the image
                                label.pack(padx=10, pady=10)
                            except Exception as e:
                                print(f"Error loading image from {image_to_display}: {e}")
                        
                        if tab_name == "Contour Mapping":
                            contour_path = os.path.join(base_path, "contoured_images", "contoured_image.png")
                            image_to_display = contour_path
                        try:
                                img = Image.open(image_to_display)
                                img_resized = img.resize((400, 300))
                                img_photo = ImageTk.PhotoImage(img_resized)
                                label = tk.Label(tab, image=img_photo)
                                label.image = img_photo  # keep a reference to the image
                                label.pack(padx=10, pady=10)
                        except Exception as e:
                            print(f"Error loading image from {image_to_display}: {e}")

                        if tab_name == "RAW OCT-B":
                            load_images(master)
                            

        # Pack the main tab control
        main_tabControl.pack(expand=1, fill="both")

        # Store the reference to the Notebook widget in the frame for later destruction
        frame.notebook = main_tabControl


def initialize_tab_b(master):
    frame = Frame(master, width=600, height=600)
    frame.pack()
    frame.place(x=550, y=110)

    frame2 = Frame(master, width=600, height=600)
    frame2.pack()
    frame2.place(x=1000, y=110)

    frame3 = Frame(master, width=600, height=600)
    frame3.pack()
    frame3.place(x=550, y=470)

    frame4 = Frame(master, width=600, height=600)
    frame4.pack()
    frame4.place(x=1000, y=470)


    config.frames_b = [frame, frame2 , frame3, frame4]  # Initialize the list of frames for the tabs if not already done

    config.num_tabs_list_b = [0, 0, 0, 0]  # Adjusted to match the number of tabs you're adding

    selected_file_path = None  # This seems like a placeholder for now

    tab_names_list_b = [
        ["Enface"],  # Names for tabs in the first frame
        ["Middle OCT-B"], 
        ["RAW OCT-B"], 
        ["Contour Mapping"]  # Names for tabs in the fourth frame
    ]
    
    b_tabs(master, config.frames_b, config.num_tabs_list_b, selected_file_path, tab_names_list_b)

    return config.frames_b, config.num_tabs_list_b