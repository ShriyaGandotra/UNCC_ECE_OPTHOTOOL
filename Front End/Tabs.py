# AUTHOR: SHRIYA GANDOTRA
# This script is designed to dynamically create and manage tabs within a Tkinter GUI application. 
# It defines two main functions: Enface and Contour Mapping Tab

import tkinter as tk
from tkinter import ttk, Frame
from PIL import Image, ImageTk
import os
import Config as config

def tabs(master, frames, num_tabs_list, selected_file_path, tab_names_list):
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
                        full_path = os.path.join(base_path, "raw_images", "image_0_256.png")
                        image_to_display = full_path
                        
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
                            print(f"Error loading image from {full_path}: {e}")

        # Pack the main tab control
        main_tabControl.pack(expand=1, fill="both")

        # Store the reference to the Notebook widget in the frame for later destruction
        frame.notebook = main_tabControl

def clear_all_tabs(frames):
    """Clear all tabs from each frame provided."""
    for frame in frames:
        if hasattr(frame, 'notebook'):
            frame.notebook.destroy()  # Destroy the notebook widget to clear all its tabs
            delattr(frame, 'notebook')  # Remove the attribute to avoid reference issues

def initialize_tabs(master):
    frame = Frame(master, width=600, height=600)
    frame.pack()
    frame.place(x=550, y=110)

    frame4 = Frame(master, width=600, height=600)
    frame4.pack()
    frame4.place(x=1000, y=470)

    config.frames = [frame, frame4]  # Initialize the list of frames for the tabs if not already done

    config.num_tabs_list = [0, 0]

    selected_file_path = None  # This seems like a placeholder for now

    tab_names_list = [
        ["Enface"],  # Names for tabs in the first frame
        ["Contour Mapping"]  # Names for tabs in the fourth frame
    ]
    
    tabs(master, config.frames, config.num_tabs_list, selected_file_path, tab_names_list)

    return config.frames, config.num_tabs_list
