import tkinter as tk
from tkinter import ttk, Frame
from PIL import Image, ImageTk
import os
import Config as config

def octa_tabs(master, frames_octa, num_tabs_list, selected_file_path, tab_names_list):
    style = ttk.Style()
    theme_name = style.theme_use('clam')
    style.configure(f"{theme_name}.TNotebook", background='white')
    style.configure(f"{theme_name}.TNotebook.Tab", background='white')

    # Configure the background color for the content area of the tabs
    style.configure(f"{theme_name}.TFrame", background='white')

    for i, frames in enumerate(frames_octa):
        # Check if the frame already has a tab control and destroy it
        for widget in frames.winfo_children():
            widget.destroy()

        # Create the main tab control 
        main_tabControl = ttk.Notebook(frames, style=f"{theme_name}.TNotebook")
        main_tabControl.config(width=400, height=300)  # Set the initial size of the notebook

        # Add tabs with names from the tab_names_list
        for j in range(num_tabs_list[i] + 1):  # +1 for the main tab
            tab_name = tab_names_list[i][j] if j < len(tab_names_list[i]) else f"Tab {j + 1}"
            tab = ttk.Frame(main_tabControl)
            main_tabControl.add(tab, text=tab_name)

            if j == 0 and selected_file_path and isinstance(selected_file_path, str) and len(selected_file_path) >= 3:

                #Add code to add image to the tab, as per the specific file type handling and requirements
                if selected_file_path[-3:] == "png":
                        print(selected_file_path)
                        base_path = os.path.splitext(selected_file_path)[0]
                        full_path = os.path.join(base_path, "raw_images", "image_0_256.png")
                        image_to_display = full_path
                        
                        if tab_name == "Raw OCT-A":
                            rawOCTA_path = "OCTA.png"  
                            # Call the function with the specified parameters
                            image_to_display = rawOCTA_path
                            try:
                                img = Image.open(image_to_display)
                                img_resized = img.resize((400, 300))
                                img_photo = ImageTk.PhotoImage(img_resized)
                                label = tk.Label(tab, image=img_photo)
                                label.image = img_photo  # keep a reference to the image
                                label.pack(padx=10, pady=10)
                            except Exception as e:
                                print(f"Error loading image from {image_to_display}: {e}")
                        
                        if tab_name == "AVA Map":
                            ava_path = "oct_test1/AVA/av_map.png" 
                            image_to_display = ava_path
                        try:
                                img = Image.open(image_to_display)
                                img_resized = img.resize((400, 300))
                                img_photo = ImageTk.PhotoImage(img_resized)
                                label = tk.Label(tab, image=img_photo)
                                label.image = img_photo  # keep a reference to the image
                                label.pack(padx=10, pady=10)
                        except Exception as e:
                            print(f"Error loading image from {full_path}: {e}")

                        if tab_name == "Skeletonized Map":
                            skeleton_path = "oct_test1/skeletonized_image/skeleton.png"  
                            # Call the function with the specified parameters
                            image_to_display = skeleton_path
                            try:
                                img = Image.open(image_to_display)
                                img_resized = img.resize((400, 300))
                                img_photo = ImageTk.PhotoImage(img_resized)
                                label = tk.Label(tab, image=img_photo)
                                label.image = img_photo  # keep a reference to the image
                                label.pack(padx=10, pady=10)
                            except Exception as e:
                                print(f"Error loading image from {image_to_display}: {e}")

                        if tab_name == "Perimeter Map":
                            perimeter_path = "oct_test1/perimeter_image/perimeter.png"  
                            # Call the function with the specified parameters
                            image_to_display = perimeter_path
                            try:
                                img = Image.open(image_to_display)
                                img_resized = img.resize((400, 300))
                                img_photo = ImageTk.PhotoImage(img_resized)
                                label = tk.Label(tab, image=img_photo)
                                label.image = img_photo  # keep a reference to the image
                                label.pack(padx=10, pady=10)
                            except Exception as e:
                                print(f"Error loading image from {image_to_display}: {e}")

        # Pack the main tab control
        main_tabControl.pack(expand=1, fill="both")

        # Store the reference to the Notebook widget in the frame for later destruction
        frames.notebook = main_tabControl

def clear_all_tabs(frames):
    """Clear all tabs from each frame provided."""
    for frame in frames:
        if hasattr(frame, 'notebook'):
            frame.notebook.destroy()  # Destroy the notebook widget to clear all its tabs
            delattr(frame, 'notebook')  # Remove the attribute to avoid reference issues

def initialize_tabs_2(master):
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


    config.frames_octa = [frame, frame2 , frame3, frame4]  # Initialize the list of frames for the tabs if not already done

    config.num_tabs_list_octa = [0, 0, 0, 0]  # Adjusted to match the number of tabs you're adding

    selected_file_path = None  # This seems like a placeholder for now

    tab_names_list_octa = [
        ["Raw OCT-A"],  # Names for tabs in the first frame
        ["AVA Map"], 
        ["Skeletonized Map"], 
        ["Perimeter Map"]  # Names for tabs in the fourth frame
    ]
    
    octa_tabs(master, config.frames_octa, config.num_tabs_list_octa, selected_file_path, tab_names_list_octa)

    return config.frames_octa, config.num_tabs_list_octa

def empty_frame(master):

    def destroy_middle():
        middle_frame.destroy()

    # Middle section with the label and logo in a nested frame
    middle_frame = Frame(master, bg="#4990FB")
    middle_frame.pack(side='left', expand=False)
    middle_frame.place(x = 150, y = 200)

    label = tk.Label(middle_frame, text="Images processing...", font="Karla 10 bold", bg="#4990FB", fg="white")
    label.pack(expand=True, fill=tk.BOTH)

    master.after(500, destroy_middle)

