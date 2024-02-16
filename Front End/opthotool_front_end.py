# Author : Shriya Gandotra
# Last Modified: 2/15/2024
#------------------------------------------- LIBRARIES ---------------------------------------------------#
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from tkinter.filedialog import askopenfilename
from tkinter import font as tkFont
from tkintertable import TableCanvas, TableModel
import os
from tkintertable import TableCanvas, TableModel
import random
from collections import OrderedDict
import oct_Converter as OCT
import math
import cv2
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter.messagebox import showinfo
import threading
import time
from PIL import Image, ImageTk
from tkinter import ttk, Button, Toplevel, Label
from tkinter import ttk, filedialog
from tkinter.ttk import Progressbar
import threading
#------------------------------------------- FIRST PAGE --------------------------------------------------#
# creates a Tk() object
master = Tk()

name_borwser = ""

data = ()
 
# sets the geometry of main 
# window dimensions
master.geometry("600x400")
# Set the window background color
master.configure(bg="white")
master.title("Patient Name: Dummy Person | DOB: 06/15/2002 | ID: 11223344 ")

#Setting window to be fullscreen when you run it
def start_screen(master):
    #getting screen width and height of display
    width= master.winfo_screenwidth() 
    height= master.winfo_screenheight()
    #setting tkinter window size
    master.geometry("%dx%d" % (width, height))

# Creating OPTHOTOOL TECHNOLGY label for 1st page
def opthotool_techlology(master):
    optho_label = Label(master, text ="OPTHOTOOL TECHNOLOGY", width=220, height=2, font = "Karla 10 bold", borderwidth=2, relief="groove")
    optho_label.config(bg= "#4990FB", fg= "white")
    optho_label.pack(pady = 0)

    global logo_img
    # Create an object of tkinter ImageTk
    logo = (Image.open("logo.png"))
    logo1 = logo.resize((35,30))
    logo_img = ImageTk.PhotoImage(logo1)

    # # Create a Label Widget to display the text or Image
    label_logo1 = Label(master, image = logo_img)
    label_logo1.config(bg="#4990FB")
    label_logo1.pack()
    label_logo1.place(x=620,y=2)

# Creating OPTHOTOOL TECHNOLGY label for 2nd page
def opthotool_techlology2(newWindow):
    optho_label = Label(newWindow, text ="OPTHOTOOL TECHNOLOGY", width=100, height=2, font = "Karla 10 bold", borderwidth=2, relief="groove")
    optho_label.config(bg= "#4990FB", fg= "white")
    optho_label.pack(pady = 0)

    global logo_img
    # Create an object of tkinter ImageTk
    logo2 = (Image.open("logo.png"))
    logo3 = logo2.resize((35,30))
    logo_img1 = ImageTk.PhotoImage(logo3)

    # # Create a Label Widget to display the text or Image
    label_logo2 = Label(newWindow, image = logo_img1)
    label_logo2.config(bg="#4990FB")
    label_logo2.pack()
    label_logo2.place(x=620,y=2)

def create_label_with_shadow(master, text, x, y, width):
    shadow_color = "#dddddd"  # Light grey for shadow
    # Create the main label on top of the shadow label
    main_label = Label(master, text=text, anchor="w", width=width, height=2, font="Karla 10 bold")
    main_label.config(bg="#9CE2F8", fg="black")
    main_label.place(x=x, y=y)
 
# Creating upload scan label for 1st page
def upload(master):
    # Create the main frame that will hold both labels
    combined_frame = Frame(master, borderwidth=2, relief="groove", bg="white")
    combined_frame.place(x=85, y=60, width=434, height=341)

    # Place the "Upload Scan" label with shadow in the combined frame
    create_label_with_shadow(combined_frame, "  Upload Scan", 0, 0, 53)

    # Place the "Select Scan" label with shadow in the combined frame
    # Adjust y-coordinate according to the height of the "Upload Scan" label
    create_label_with_shadow(combined_frame, "  Select Scan", 0, 130, 53)  # y is adjusted for placement

    return combined_frame


# Creating retinal scan label for 1st page
def tools(master):
    # Create the main frame that will hold the retina details section
    tools_frame = Frame(master, borderwidth=2, relief="groove", bg="white")
    tools_frame.place(x=85, y=640, width=434, height=107)

    create_label_with_shadow(tools_frame, "  Tools", 0, 0, 53)
   
    ############# DISTANCE TOOL #########
    # Function to calculate the distance
    def calculate_distance():
        global point1, point2
        if point1 and point2:
            distance = math.sqrt(((point2[0] - point1[0]) * width) ** 2 + ((point2[1] - point1[1]) * height) ** 2)
            result_label.config(text=f"Distance: {distance:.2f} mm")

    def set_point(event):
        global point1, point2
        if point1 is None:
            point1 = (event.x, event.y)
        elif point2 is None:
            point2 = (event.x, event.y)
            calculate_distance()
            draw_line()

    # Function to draw a line between the two points
    def draw_line():
        global point1, point2, line
        if line:
            line.destroy()
        x1, y1 = point1
        x2, y2 = point2
        length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        min_x = min(x1, x2)
        min_y = min(y1, y2)
        line = ttk.Label(master, width=int(length), background="red")
        line.place(x=min_x, y=min_y)
        line.config(height=2)

    # Function to toggle measurement mode
    def toggle_measure_mode():
        global measure_mode, point1, point2, line
        measure_mode = not measure_mode
        if measure_mode:
            measure_button.config(relief=tk.SUNKEN, borderwidth=3)
            master.bind("<Button-1>", set_point)
        else: 
            measure_button.config(relief=tk.RAISED, borderwidth=0)
            master.unbind("<Button-1>")
            point1 = None
            point2 = None
            result_label.config(text="Distance: N/A")
            if line:
                line.destroy()

    measure_button = Button(master, text = "Measure Tool", command = toggle_measure_mode)
    measure_button.place(x=95, y=690)
    #Show Distance
    result_label = tk.Label(master, text="Distance: N/A")
    result_label.place(x=95, y=720, width= 80, height= 20)

    return tools_frame

# Creating retinal scan label for 1st page
def layer(master):
    # Create the main frame that will hold the retina details section
    layer_frame = Frame(master, borderwidth=2, relief="groove", bg="white")
    layer_frame.place(x=85, y=435, width=434, height=175)

    # Place the "Retina Details" label with shadow in the retina frame
    create_label_with_shadow(layer_frame, "  Layer Details", 0, 0, 53)

    return layer_frame

# create a diagnose button that will open a new window on button click
def diag_button(master):
    diagnose_btn = Button(master, text ="Diagnose", command = openDiagsoneWindow,borderwidth=0, bg='#4990FB',font="Karla 12 bold", fg='white',padx=20,pady=5)
    diagnose_btn.place(x=245,y=775)


# create a text box where selected file name will display
def display_name(master,name):
    if name == "":
        name = "Dummy_Left_Eye"

    T = Text(master, height = 2, width = 20,font = "Karla 12",relief="flat")
    T.config(bg="white")
    T.place(x=550,y=60)
    T.insert(END,name)

# create a text box where selected file name will display
def display_eye_side(master):
    eye_side = "Left/ODD"

    T = Text(master, height = 2, width = 20,font = "Karla 12",relief="flat")
    T.config(bg="white")
    T.place(x=1330,y=60)
    T.insert(END,eye_side)

# create a text box where selected file name will display
def confidence_score(newWindow):
    confidence_score_master_label = Label(newWindow, anchor="w", width=60, height=15, font = "Karla 10 bold", relief="groove")
    confidence_score_master_label.config(bg= "white", fg= "black")
    confidence_score_master_label.pack(pady = 0)
    confidence_score_master_label.place(x=60,y= 90)
    
    confidence_score_label = Label(newWindow, text ="Confidence Score", anchor="w", width=60, height=2, font = "Karla 10 bold")
    confidence_score_label.config(bg= "#9CE2F8", fg= "black")
    confidence_score_label.pack(pady = 0)
    confidence_score_label.place(x=60,y=90)

def confidence_score_info(newWindow):
    
    diabetic = Text(newWindow, height = 2, width = 20,font = "Karla 12",relief="flat")
    diabetic.place(x=80,y=150)
    diabetic.insert(END,"Diabetic Retinopathy: ")

    prediction = Text(newWindow, height = 2, width = 20,font = "Karla 12",relief="flat",fg="red")
    prediction.place(x=270,y=150)
    prediction.insert(END,"POSITIVE")

    msg = "Based on the scans, chance of damage reversal:"
    reversal_msg = Text(newWindow, height = 2, width = len(msg),font = "Karla 12",relief="flat")
    reversal_msg.place(x=80,y=200)
    reversal_msg.insert(END,msg)

    percent = Text(newWindow, height = 1, width = 4,font = "Karla 30",relief="flat")
    percent.place(x=270,y=250)
    percent.insert(END,"95%")

# Define layers
def layer_segmentation(master):

    Layer1 = Text(master, height = 1, width = 20, font = "Karla 10", relief="flat", fg="red")
    Layer1.place(x=1310,y=580)
    Layer1.insert(END,"Outer Nuclear Layer")

    Layer2 =  Text(master, height = 1, width = 20, font = "Karla 10", relief="flat", fg="green")
    Layer2.place(x=1310,y=600)
    Layer2.insert(END,"Ellipsoid Zone")

    Layer3 =  Text(master, height = 1, width = 23, font = "Karla 10", relief="flat", fg="orange")
    Layer3.place(x=1310,y=620)
    Layer3.insert(END,"Retinal Pigment Epithelium")

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

        
        table_select.insert("", "end", values=(name, date_time, file_type))
        #append('', 'end', values=(name, date_time, file_type))

    return file_name_display

def simulate_file_loading(progress_bar, popup, completion_callback=None):
    """
    Simulate file loading process by updating the progress bar.
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

selected_file_path = None

# display file button
def file_upload_btn(master, table_select):
    global selected_file_path

    def oct_conversion_thread(oct_f_path):
        tab_names_list = [
            ["Raw OCT-A"],  # Names for tabs in the first frame
            ["Segmented Map", "Skeletonized Map", "AVA Map"],  # Names for tabs in the second frame
            ["Raw OCT-B"],  # Names for tabs in the third frame
            ["Contour Mapping", "Layer Segmenter"]  # Names for tabs in the fourth frame
        ]
        def run_conversion():
            oct_conversion(oct_f_path)
            name_browser = os.path.basename(oct_f_path)
            file_name(master, table_select, name_browser)
            tabs(master, frames, num_tabs_list, file_name, tab_names_list)
            popup.destroy()  # Close the popup window once conversion is done
            upload_file_btn.config(state="normal")

       # Create a popup window for the progress bar
        popup = Toplevel(master)
        popup.title("Converting OCT File")
        popup.geometry("300x100")  # Adjust the size as needed
        popup.configure(bg='white')  # White background for the popup window

        karla_font = tkfont.Font(family="Karla", size=11)
        popup_label = Label(popup, text="Converting, please wait...", font=karla_font, bg='white', fg='black')
        popup_label.pack(pady=10)

        # Configure the progress bar with custom colors
        style = ttk.Style()
        style.theme_use('default')
        style.configure("custom.Horizontal.TProgressbar", 
                        background='#008dd2', troughcolor='#f9f9f9')
        
        progress = ttk.Progressbar(popup, style="custom.Horizontal.TProgressbar", 
                                   orient="horizontal", mode="indeterminate", length=280)
        progress.pack(pady=10)
        progress.start(10)

        upload_file_btn.config(state="disabled")  # Disable the button while processing
        threading.Thread(target=run_conversion).start()

    def browse():
        global selected_file_path
        tab_names_list = [
            ["Raw OCT-A"],  # Names for tabs in the first frame
            ["Segmented Map", "Skeletonized Map", "AVA Map"],  # Names for tabs in the second frame
            ["Raw OCT-B"],  # Names for tabs in the third frame
            ["Contour Mapping", "Layer Segmenter"]  # Names for tabs in the fourth frame
        ]

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

    progress = ttk.Progressbar(master, orient="horizontal", mode="indeterminate")

    return upload_file_btn

#oct-converter
def oct_conversion(oct_f_path):
    file_type = os.path.splitext(oct_f_path)[1].upper().replace(".", "")

    if file_type == 'OCT':
        OCT.oct_converter_poct(oct_f_path)
    if file_type == 'oct':
        OCT.oct_converter_boct(oct_f_path)
    if file_type == 'fds':
        OCT.oct_converter_fds(oct_f_path)
    if file_type == 'fda':
        OCT.oct_converter_fda(oct_f_path)
    if file_type == 'img':
        OCT.oct_converter_img(oct_f_path)
    if file_type == 'dcm':
        OCT.oct_converter_dcm(oct_f_path)
    if file_type == 'e2e':
        OCT.oct_converter_e2e(oct_f_path)
 
    return

 # function to open a new window 
# on a button click
def openDiagsoneWindow():  
    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(master)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Patient Name: Dummy Person")
    
    #Set background color
    newWindow.configure(bg="white")
 
    # sets the geometry of toplevel
    newWindow.geometry("600x400")

    opthotool_techlology2(newWindow)
    confidence_score(newWindow)
    confidence_score_info(newWindow)

# function for selecting scan and corresponding file tabel
def selectScanTabel(window,table_data):
    frame = ttk.Frame(window, padding="0")
    frame.pack(padx=0, pady=0)
    frame.place(x=86, y=230)

    # Styling the Treeview
    style = ttk.Style()
    style.theme_use("default")

    # Configure the font and background for headings and rows
    style.configure("Treeview", font=("Karla", 10), rowheight=25)
    style.configure("Treeview.Heading", font=("Karla", 10, "bold"), background="#e1e1e1", foreground="black")

    # Configure the Treeview layout
    style.map("Treeview", background=[('alternate', '#f5f5f5')])  # Alternating row colors

    # Configure the scrollbar style
    style.configure("Vertical.TScrollbar", gripcount=0, background="#c1c1c1", darkcolor="#c1c1c1",
                    lightcolor="#c1c1c1", troughcolor="#f0f0f0", bordercolor="#f0f0f0", arrowcolor="black")
    style.map("Vertical.TScrollbar", background=[("active", "#a1a1a1")])

    # Create Treeview widget
    table = ttk.Treeview(frame, columns=("File Name", "Date/Time", "File Type"), show='headings', height=7)
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
        
        # Access individual values assuming a tuple structure (file_name, date_time, file_type)
        file_name, date_time, file_type = item_values
        tab_names_list = [
            ["Raw OCT-A"],  # Names for tabs in the first frame
            ["Segmented Map", "Skeletonized Map", "AVA Map"],  # Names for tabs in the second frame
            ["Raw OCT-B"],  # Names for tabs in the third frame
            ["Contour Mapping", "Layer Segmenter"]  # Names for tabs in the fourth frame
        ]
        tabs(master, frames, num_tabs_list, file_name, tab_names_list)
        file_name = file_name.split(".")[0]
        
        display_name(master,file_name)
    
    # Bind the nested function to the treeview's selection event
    table.bind('<<TreeviewSelect>>', on_row_selected)


    # Configuring column widths and headers
    table.column("File Name", width=150, anchor="w")
    table.column("Date/Time", width=150, anchor="w")
    table.column("File Type", width=113, anchor="w")

    table.heading("File Name",anchor="w", text="File Name")
    table.heading("Date/Time",anchor="w", text="Date/Time")
    table.heading("File Type", anchor="w", text="File Type")

    # Apply tags for alternating row colors
    style.configure('evenrow', background="#f5f5f5")
    style.configure('oddrow', background="#ffffff")

    return table 


# function for displaying retinal details
def retinaDetailsTabel(window2):
    frame = ttk.Frame(window2, padding="0")
    frame.pack(padx=0, pady=0)
    frame.place(x=86, y=466)

    # Styling the Treeview
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", font=("Karla", 10))
    style.configure("Treeview.Heading", font=("Karla bold", 10), background= "gray79", foreground="black", padding=(0, 4, 0, 4))
    style.layout('Vertical.TScrollbar', [
        ('Vertical.Scrollbar.trough', {'children':
            [('Vertical.Scrollbar.uparrow', {'side': 'top', 'sticky': ''}),
            ('Vertical.Scrollbar.downarrow', {'side': 'bottom', 'sticky': ''}),
            ('Vertical.Scrollbar.thumb', {'expand': 'true', 'sticky': 'nswe'})
            ], 'sticky': 'ns'
        })
    ])

    style.configure("Vertical.TScrollbar", background="gray79", darkcolor="gray", lightcolor="gray", troughcolor="white", bordercolor="white", arrowcolor="black")
    style.map("Vertical.TScrollbar", background=[("active", "gray"), ("!disabled", "gray79")], 
          gripcount=[("active", 10), ("!disabled", 0)])
    
# Style the arrows (optional)
    style.configure('Vertical.Scrollbar.uparrow', width=15, relief='flat')
    style.configure('Vertical.Scrollbar.downarrow', width=15, relief='flat')
    style.configure("Vertical.TScrollbar", width=5) 
    style.configure("Vertical.Scrollbar.thumb", width=5)  
    style.configure("Vertical.Scrollbar.trough", width=5) 
    style.configure("Treeview.Item", padding=(0, 10, 0, 10))

    table = ttk.Treeview(frame, columns=("Feature", "Measurement"), show='headings', height=13)
    table.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")

    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=table.yview, style="Vertical.TScrollbar")
    scrollbar.grid(row=1, column=1, sticky="ns")

    table.configure(yscrollcommand=scrollbar.set)

    # Sample data
    data = [
        ("Macular Vessel Density", "X Unit"),
        ("TBD_FEATURE 1", "X Unit"),
        ("TBD_FEATURE 2", "X Unit"),
        ("TBD_FEATURE 3", "X Unit"),
        ("TBD_FEATURE 4", "X Unit"),
        ("TBD_FEATURE 5", "X Unit"),
        ("TBD_FEATURE 6", "X Unit"),
        ("TBD_FEATURE 7", "X Unit"),
        ("TBD_FEATURE 8", "X Unit"),
        ("TBD_FEATURE 9", "X Unit"),
        ("TBD_FEATURE 10", "X Unit"),
        ("TBD_FEATURE 11", "X Unit"),
        ("TBD_FEATURE 12", "X Unit"),
        ("TBD_FEATURE 13", "X Unit"),
        ("TBD_FEATURE 14", "X Unit"),
    ]

    # Populate data into the table
    for feature, measurement in data:
        table.insert("", "end", values=(feature, measurement))

    # Configuring column widths
    table.column("Feature", width=207)
    table.column("Measurement", width=207)

    # Configuring header texts
    table.heading("Feature", anchor="w", text=" Feature")
    table.heading("Measurement", anchor="w", text=" Measurement")

def layerDetails(master):
    style = ttk.Style()
    # Configure the style to have a white background
    style.configure('My.TFrame', background='white')
    style.configure('TLabel', background='white')
    style.configure('TCombobox', fieldbackground='white', background='white')
    style.configure('TEntry', fieldbackground='white', background='white')
    style.configure('TCheckbutton', background='white')

    frame = ttk.Frame(master, padding="10", style='My.TFrame')
    frame.place(x=118, y=485)

    # Create labels with white background
    from_label = ttk.Label(frame, text="From:", font="Karla 10", style='TLabel')
    to_label = ttk.Label(frame, text="To:", font="Karla 10", style='TLabel')
    thickness_label = ttk.Label(frame, text="Thickness:", font="Karla 10", style='TLabel')

    # Place labels with uniform padding
    from_label.grid(row=0, column=0, sticky='W', padx=10, pady=5)
    to_label.grid(row=1, column=0, sticky='W', padx=10, pady=5)
    thickness_label.grid(row=2, column=0, sticky='W', padx=10, pady=5)

    # Create dropdown menus with white background
    from_combo = ttk.Combobox(frame, values=["LAYER 1", "LAYER 2", "LAYER 3"], state="readonly", width=15, style='TCombobox')
    to_combo = ttk.Combobox(frame, values=["LAYER 1", "LAYER 2", "LAYER 3"], state="readonly", width=15, style='TCombobox')

    # Place dropdown menus with uniform padding
    from_combo.grid(row=0, column=1, padx=10, pady=5, sticky='EW')
    to_combo.grid(row=1, column=1, padx=10, pady=5, sticky='EW')

    # Create thickness entry with white background
    thickness_entry = ttk.Entry(frame, width=18, style='TEntry')
    thickness_entry.grid(row=2, column=1, padx=10, pady=5, sticky='EW')

    # Create checkboxes with white background
    check_fovea = ttk.Checkbutton(frame, text="Fovea", style='TCheckbutton')
    check_parafovea = ttk.Checkbutton(frame, text="Parafovea", style='TCheckbutton')
    check_perifovea = ttk.Checkbutton(frame, text="Perifovea", style='TCheckbutton')

    # Place checkboxes with uniform padding
    check_fovea.grid(row=0, column=2, padx=25, pady=5, sticky='W')
    check_parafovea.grid(row=1, column=2, padx=25, pady=5, sticky='W')
    check_perifovea.grid(row=2, column=2, padx=25, pady=5, sticky='W')

    # Adjust frame column configurations for alignment
    frame.columnconfigure(1, weight=1)  # Allows the column with comboboxes to expand

def display_image_on_tab(image_path, tab_frame):
    # Load the image
    img = Image.open(image_path)
    img_resized = img.resize((400, 300))  # Resize the image to fit the tab
    img_photo = ImageTk.PhotoImage(img_resized)

    # Display the image in a label within the tab frame
    label = tk.Label(tab_frame, image=img_photo)
    label.image = img_photo  # Keep a reference to the image
    label.pack(padx=10, pady=10)

def initialize_tabs():
    frames = [frame, frame2, frame3, frame4]  # List of frames for the tabs
    num_tabs_list = [0, 2, 0, 1]  # Initially, no sub-tabs
    selected_file_path = None  # No file selected initially
    tab_names_list = [
    ["Raw OCT-A"],  # Names for tabs in the first frame
    ["Segmented Map", "Skeletonized Map", "AVA Map"],  # Names for tabs in the second frame
    ["Raw OCT-B"],  # Names for tabs in the third frame
    ["Contour Mapping", "Layer Segmenter"]  # Names for tabs in the fourth frame
    ]
    tabs(master, frames, num_tabs_list, selected_file_path, tab_names_list)

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

            # Add the image to the main tab if it's the first tab and selected_file_path is provided
            if j == 0 and selected_file_path and isinstance(selected_file_path, str) and len(selected_file_path) >= 3:
                #Add code to add image to the tab, as per the specific file type handling and requirements
                if selected_file_path[-3:] == "png":
                    try:
                        print(selected_file_path)
                        img = Image.open(selected_file_path)
                        img_resized = img.resize((400, 300))
                        img_photo = ImageTk.PhotoImage(img_resized)
                        label = tk.Label(tab, image=img_photo)
                        label.image = img_photo  # keep a reference to the image
                        label.pack(padx=10, pady=10)
                    except Exception as e:
                        print(f"Error loading image from {selected_file_path}: {e}")
                if selected_file_path[-3:] == "OCT":
                        print(selected_file_path)
                        base_path = os.path.splitext(selected_file_path)[0]
                        full_path = os.path.join(base_path, "raw_images", "image_0_256.png")
                        image_to_display = full_path
                        if tab_name == "Contour Mapping":
                            contour_mapping(full_path)
                            contour_path = os.path.join(base_path, "ContouredImages", "contoured_image.png")
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
     
########## CONTOUR MAPPING #########
def contour_mapping(filepath):
    # Read the B-scan image
    b_scan = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(b_scan, (9, 9), 1)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, 30, 70)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original grayscale image
    result_image = cv2.cvtColor(b_scan, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(result_image, contours, -1, (0, 255, 0), 1)

    # Save the image with contours
    output_folder = os.path.join("/Users/Shriya Gandotra/Desktop/Senior design/oct_test1", 'ContouredImages')
    os.makedirs(output_folder, exist_ok=True)

    output_filepath = os.path.join(output_folder, 'contoured_image.png')
    cv2.imwrite(output_filepath, result_image)

#---------------- Image 1 -----------------------#
frame = Frame(master, width=600, height=600)
frame.pack()
frame.place(x=550,y=110)

#---------------- Image 2 -----------------------#
frame2 = Frame(master, width=600, height=600)
frame2.pack()
frame2.place(x=1000,y=110)

#---------------- Image 3 -----------------------#
frame3 = Frame(master, width=600, height=600)
frame3.pack()
frame3.place(x=550,y=470)

#---------------- Image 4 -----------------------#
frame4 = Frame(master, width=600, height=600)
frame4.pack()
frame4.place(x=1000,y=470)


logo_img = "logo.png"

start_screen(master)
opthotool_techlology(master)
upload(master)
tools(master)
diag_button(master)
display_eye_side(master)
table_select = selectScanTabel(master,data)
file_upload_btn(master, table_select)
file_name(master,table_select,name_borwser)
initialize_tabs()
frames = [frame, frame2,frame3, frame4]  # Create a list of frames for the tabs
num_tabs_list = [0, 2, 0, 1]  # Example number of sub-tabs for each main tab
tabs(master, frames, num_tabs_list)

# mainloop, runs infinitely
mainloop()









