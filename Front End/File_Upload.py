# AUTHOR: SHRIYA GANDOTRA
# Features include:
# - File selection with support for various medical image formats
# - Interactive table displaying file details
# - File processing with Contour, Enface, Perimeter, Skeletonization, and OCT modules (Refer to Backend repo for original functions)
# - Progress bar for conversion and loading operations
# - Multithreading to ensure GUI responsiveness
# - Thread-safe GUI updates during background processing

import tkinter as tk
from tkinter import ttk
from tkinter import *
from datetime import datetime
import os
import threading
import time
from tkinter.filedialog import askopenfilename
import Contour as CONTOUR
import Enface as ENFACE
import Perimeter as PERIMETER
import Skeletonization as SKELETON
import OCT as OCT
import Tabs as TAB
import Tabs2 as TABS2
import Config as CONFIG

selected_file_path = None


# create a text box where selected file name will display
def display_name(master,name):
    if name == "":
        name = "Dummy_Left_Eye"

    T = Text(master, height = 2, width = 20,font = "Karla 12",relief="flat")
    T.configure(bg="white")
    T.place(x=550,y=60)
    T.insert(END,name)

# create a text box where selected file name will display
def display_eye_side(master):
    eye_side = "Left/ODD"

    T = Text(master, height = 2, width = 20,font = "Karla 12",relief="flat")
    T.configure(bg="white")
    T.place(x=1330,y=60)
    T.insert(END,eye_side)

# default file name if no file is chossen
def file_name(master, table_select, name=""):

    print(table_select)
    if name == "":
        name = "No File Chosen"

    # Instead of a Text widget, use a label to display the file name
    file_name_display = tk.Label(master, text=name, font="Karla 10", borderwidth=2, relief="groove")
    file_name_display.place(x=140, y=130, width=200, height=25)

    # If a file was chosen, update the table
    if name != "No File Chosen":
        file_type = os.path.splitext(name)[1].upper().replace(".", "")
        date_time = datetime.now().strftime("%m/%d/%y   %I:%M%p")
        # Append the new file's details to the table  
        table_select.insert("", 0 , values=(name, date_time, file_type))

    return file_name_display

def simulate_file_loading(progress_bar, popup, completion_callback=None):
    """
    Simulate file loading process by updating the progress bar.4
    """
    for i in range(100):
        time.sleep(0.05)  # Simulate time-consuming operation
        progress_bar['value'] += 1
        popup.update_idletasks()
    time.sleep(0.5)  # Hold the completed progress bar for a short time
    if completion_callback:
        completion_callback()

def show_progress_bar(master, completion_callback=None):
    """
    Show a progress bar in a popup window.
    """
    popup = Toplevel(master)
    popup.title("Loading File")
    popup.geometry("300x50+{}+{}".format(master.winfo_x() + 50, master.winfo_y() + 50))

    progress_bar = ttk.Progressbar(popup, orient=tk.HORIZONTAL, length=280, mode='determinate')
    progress_bar.pack(pady=10)

    # Start a thread to simulate file loading and update the progress bar
    threading.Thread(target=simulate_file_loading, args=(progress_bar, popup, completion_callback), daemon=True).start()
    return popup 

def safe_gui_update(master, func, *args, **kwargs):
    """
    Safely update the GUI from a thread by scheduling func to be called in the main loop.
    """
    master.after(0, func, *args, **kwargs)

def update_table_with_file(master, table, file_path):
    name = os.path.basename(file_path)
    file_type = os.path.splitext(name)[1].upper().replace(".", "")
    date_time = datetime.now().strftime("%m/%d/%y %I:%M%p")
    table.insert("", "end", values=(name, date_time, file_type))
    
from tkinter import Tk, Button, Toplevel, ttk, Label, font as tkfont
import AVA as AVA
import octa_tabs as OCTA_TAB
import B_Scan_Tabs as B_SCAN
import Components as MAIN

#display file button
def file_upload_btn(master, table_select):
    global selected_file_path

    def oct_conversion_thread(oct_f_path):
        tab_names_list = [
            ["Enface"],  # Names for tabs in the first frame # Names for tabs in the second frame  # Names for tabs in the third frame
            ["Contour Mapping"]  # Names for tabs in the fourth frame
        ]
        tab_names_list_octa = [
        ["Raw OCT-A"],  # Names for tabs in the first frame
        ["AVA Map"], 
        ["Skeletonized Map"], 
        ["Perimeter Map"]  # Names for tabs in the fourth frame
        ]
        
        tab_names_list_b = [
        ["Enface"],  # Names for tabs in the first frame
        ["Middle OCT-B"], 
        ["RAW OCT-B"], 
        ["Contour Mapping"]  # Names for tabs in the fourth frame
    ]
    
        def run_conversion():
            global av_map_path, a_map_path, v_map_path
            OCTA_TAB.empty_frame(master)

            name_browser = os.path.basename(oct_f_path)
            file_name(master, table_select, name_browser)

            if oct_f_path[-3:] == "OCT":
                B_SCAN.initialize_tab_b(master)
                # OCT-CONVERSION
                OCT.oct_conversion(oct_f_path)
                # ENFACE
                ENFACE.enface_conversion()
                # SEGMENTER + CONTOUR 
                CONTOUR.contour_conversion()
                #TAB.tabs(master, CONFIG.frames, CONFIG.num_tabs_list, file_name, tab_names_list)
                B_SCAN.b_tabs(master, CONFIG.frames_b, CONFIG.num_tabs_list_b, selected_file_path, tab_names_list_b)
                MAIN.enable_measure_button(oct_f_path)
                MAIN.enable_octa_button(selected_file_path)
                MAIN.enable_widgets(selected_file_path)
                MAIN.enable_diagnose_button(selected_file_path)
                # TABS2.main_application(selected_file_path, master)

            if oct_f_path[-3:] == "png":
                print("in png loop")
                OCTA_TAB.initialize_tabs_2(master)
                print("initalized tabs 2")
                # SKELETONIZATION
                octa_path = 'OCTA.png'
                SKELETON.skeletonize_image(octa_path)
                # PERIMETER
                PERIMETER.perimeter_image(octa_path)
                # AVA
                ava_model = 'AVA_model_3.hdf5'
                av_map_path, a_map_path, v_map_path = AVA.AVA_save(octa_path, ava_model)
                OCTA_TAB.octa_tabs(master, CONFIG.frames_octa, CONFIG.num_tabs_list_octa, file_name, tab_names_list_octa)
                MAIN.enable_measure_button(oct_f_path)
                MAIN.enable_octa_button(selected_file_path)
                MAIN.enable_widgets(selected_file_path)
                MAIN.enable_diagnose_button(selected_file_path)
            
            # load_images(selected_file_path)
            popup.destroy()  # Close the popup window once conversion is done
            upload_file_btn.configure(state="normal")


            if oct_f_path[-3:] == "OCT":
                B_SCAN.initialize_tab_b(master)
                #TAB.tabs(master, CONFIG.frames, CONFIG.num_tabs_list, file_name, tab_names_list)
                B_SCAN.b_tabs(master, CONFIG.frames_b, CONFIG.num_tabs_list_b, selected_file_path, tab_names_list_b)
                MAIN.enable_measure_button(oct_f_path)
                MAIN.enable_octa_button(selected_file_path)
                MAIN.enable_widgets(selected_file_path)
                MAIN.enable_diagnose_button(selected_file_path)
                # TABS2.main_application(selected_file_path, master)

            if oct_f_path[-3:] == "png":   
                OCTA_TAB.initialize_tabs_2(master)
                OCTA_TAB.octa_tabs(master, CONFIG.frames_octa, CONFIG.num_tabs_list_octa, file_name, tab_names_list_octa)
                MAIN.enable_measure_button(oct_f_path)
                MAIN.enable_octa_button(selected_file_path)
                MAIN.enable_widgets(selected_file_path)

       # Create a popup window for the progress bar
        popup = Toplevel(master)
        popup.title("Converting OCT File")
        popup.geometry("300x100")  # Adjust the size as needed
        popup.configure(bg='white')  # White background for the popup window

        karla_font = tkfont.Font(family="Karla", size=11)
        popup_label = Label(popup, text="Converting, please wait...", font=karla_font, bg='white', fg='black')
        popup_label.pack(pady=10)

        # CONFIGure the progress bar with custom colors
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("custom.Horizontal.TProgressbar", 
                        background='#008dd2', troughcolor='#f9f9f9')
        
        progress = ttk.Progressbar(popup, style="custom.Horizontal.TProgressbar", 
                                   orient="horizontal", mode="indeterminate", length=280)
        progress.pack(pady=10)
        progress.start(10)

        upload_file_btn.configure(state="disabled")  # Disable the button while processing
        threading.Thread(target=run_conversion).start()

    def browse():
        global selected_file_path

        f_path = askopenfilename(initialdir="/", title="Select File", filetypes = (
        ("PNG files", "*.png"),
        ("OCT files", "*.oct"),    # Assuming .oct is the extension for OCT files
        ("FDS files", "*.fds"),    # Assuming .fds is the extension for FDS files
        ("FDA files", "*.fda"),    # Assuming .fda is the extension for FDA files
        ("Image files", "*.img"),  # Assuming .img is the extension for IMG files
        ("DICOM files", "*.dcm"),  # Assuming .dcm is the extension for DICOM files
        ("E2E files", "*.e2e"),    # Assuming .e2e is the extension for E2E files
        ("All Files", "*.*")))
        
        if f_path:  # If a file was selected
            # selected_file_path = os.path.splitext(f_path)[0]  # Update the global variable
            selected_file_path = f_path
            oct_conversion_thread(f_path)
    
    upload_file_btn = Button(master, text="Choose File", command=browse, borderwidth=2, bg='gray', font="Karla 10", fg='black')
    upload_file_btn.place(x=340, y=129, width=100, height=25)

    return upload_file_btn

# function for selecting scan and corresponding file tabel
def selectScanTabel(master,table_data):
    frame_height = 180

    frame = ttk.Frame(master, padding="0", height=frame_height)
    frame.pack(padx=0, pady=0)
    frame.place(x=86, y=231)

    # Styling the Treeview
    style = ttk.Style()
    style.theme_use('clam')

    # CONFIGure the font and background for headings and rows
    style.configure("Treeview", font=("Karla", 10), rowheight=23)
    style.configure("Treeview.Heading", font=("Karla", 10), background="#e1e1e1", foreground="black")

    # CONFIGure the Treeview layout
    # style.map("Treeview", background=[('alternate', '#f5f5f5')])
    style.map('Treeview', 
              background=[('selected', '#e1e1e1')],  # light grey background for selected row
              foreground=[('selected', 'black')]) 

    # CONFIGure the scrollbar style
    style.configure("Vertical.TScrollbar", gripcount=0, background="#c1c1c1", darkcolor="#c1c1c1",
                    lightcolor="#c1c1c1", troughcolor="#f0f0f0", bordercolor="#f0f0f0", arrowcolor="black")
    style.map("Vertical.TScrollbar", background=[("active", "#a1a1a1")])

    # Create Treeview widget
    table = ttk.Treeview(frame, columns=("File Name", "Date/Time", "File Type"), show='headings', height=6)
    table.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")

    # Create Scrollbar widget
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=table.yview, style="Vertical.TScrollbar")
    scrollbar.grid(row=1, column=1, sticky="ns")

    # Link scrollbar to the treeview
    table.configure(yscrollcommand=scrollbar.set)

    # Populate data into the table
    for i, (file_name, date_time, file_type) in enumerate(table_data):
        table.insert("", "end", values=(file_name, date_time, file_type), tags=('evenrow' if i % 2 == 0 else 'oddrow',))

    def on_row_selected(event):
        # Get the Treeview widget
        tree = event.widget
        
        # Get the selected item ID
        selected_item = tree.selection()[0]
        
        # Retrieve the item's values
        item_values = tree.item(selected_item, 'values')

        print(selected_file_path)
        print(item_values)

        # Access individual values assuming a tuple structure (file_name, date_time, file_type)
        file_name, date_time, file_type = item_values

        tab_names_list = [
            ["Enface"],  # Names for tabs in the first frame  # Names for tabs in the second frame
            ["Contour Mapping"]  # Names for tabs in the fourth frame
        ]

        tab_names_list_octa = [
        ["Raw OCT-A"],  # Names for tabs in the first frame
        ["AVA Map"], 
        ["Skeletonized Map"], 
        ["Perimeter Map"]  # Names for tabs in the fourth frame
        ]
        
        tab_names_list_b = [
        ["Enface"],  # Names for tabs in the first frame
        ["Middle OCT-B"], 
        ["RAW OCT-B"], 
        ["Contour Mapping"]  # Names for tabs in the fourth frame
        ]
    
        # Check file extension directly from file_type or parse from file_name
        if file_name.lower().endswith(".oct"):
            B_SCAN.initialize_tab_b(master)
            B_SCAN.b_tabs(master, CONFIG.frames_b, CONFIG.num_tabs_list_b, file_name, tab_names_list_b)
        elif file_name.lower().endswith(".png"):
            OCTA_TAB.initialize_tabs_2(master)
            OCTA_TAB.octa_tabs(master, CONFIG.frames_octa, CONFIG.num_tabs_list_octa, file_name, tab_names_list_octa)

        # Updating UI elements based on selected file
        MAIN.enable_measure_button(file_name)
        MAIN.enable_octa_button(file_name)
        MAIN.enable_diagnose_button(file_name)
        MAIN.enable_widgets(file_name)
        display_name(master, file_name.split(".")[0])
                
    # Bind the nested function to the treeview's selection event
    table.bind('<<TreeviewSelect>>', on_row_selected)

    table.column("File Name", width=137, anchor="w", stretch=False)
    table.column("Date/Time", width=138, anchor="w", stretch=False)
    table.column("File Type", width=139, anchor="w", stretch=False)

    table.heading("File Name", anchor="w", text=" File Name")
    table.heading("Date/Time", anchor="w", text=" Date/Time")
    table.heading("File Type", anchor="w", text=" File Type")

    # Apply tags for alternating row colors
    style.configure('evenrow', background="#f5f5f5")
    style.configure('oddrow', background="#ffffff")

    return table 