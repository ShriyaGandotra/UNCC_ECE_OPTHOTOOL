# Opthotool Front End  - GUI COMPONENTS
# Author : Shriya Gandotra
# Date updated : 3/28/2024

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from PIL import Image, ImageTk
from tkinter import Label
from tkinter import ttk
import cv2
import numpy as np
import Distance_Tool as DISTANCE_TOOL
import ML_Model as ML_MODEL
import Layer_Measurement as LAYER_MEASUREMENT
from tkinter import messagebox
global logo_img

#Setting window to be fullscreen when you run it
def start_screen(master):
    #getting screen width and height of display
    width= master.winfo_screenwidth() 
    height= master.winfo_screenheight()
    #setting tkinter window size
    master.geometry("%dx%d" % (width, height))

# Creating OPTHOTOOL TECHNOLGY label for 1st page
def opthotool_techlology(master):
    # Load the logo image
    global logo_img

    header_frame = Frame(master, bg="#4990FB")
    header_frame.pack(fill='x', pady=0)

    # Spacer on the left for centering
    left_spacer = Label(header_frame, bg="#4990FB")
    left_spacer.pack(side='left', fill='both', expand=True)

    # Middle section with the label and logo in a nested frame
    middle_frame = Frame(header_frame, bg="#4990FB")
    middle_frame.pack(side='left', expand=False)

    optho_label = Label(middle_frame, text="OPTHOTOOL TECHNOLOGY", font="Karla 10 bold", bg="#4990FB", fg="white")
    optho_label.pack(side='left')

    logo = Image.open("logo.png")
    logo_resized = logo.resize((35, 30))
    logo_img = ImageTk.PhotoImage(logo_resized)

    label_logo1 = Label(middle_frame, image=logo_img, bg="#4990FB")
    label_logo1.pack(side='left', padx=(10, 0))  # Adjust padding as needed

    # Spacer on the right for centering
    right_spacer = Label(header_frame, bg="#4990FB")
    right_spacer.pack(side='left', fill='both', expand=True)


def create_label_with_shadow(master, text, x, y, width):
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
    global measure_icon
    global measure_button

    # Create the main frame that will hold the retina details section
    tools_frame = Frame(master, borderwidth=2, relief="groove", bg="white")
    tools_frame.place(x=85, y=640, width=434, height=107)

    create_label_with_shadow(tools_frame, "  Tools", 0, 0, 53)

    # Measure tool button
    measure_icon = Image.open("measurement_button.png")
    measure_icon = measure_icon.resize((20, 20))
    measure_icon = ImageTk.PhotoImage(measure_icon)

    # measure_button = Button(master, text = "Measure Tool", command = DISTANCE_TOOL.create_distance_calculator)
    measure_button = Button(master, image = measure_icon, command = DISTANCE_TOOL.create_distance_calculator,  state='disabled')
    measure_button.place(x=95, y=690)


    return tools_frame


def enable_measure_button(file_path):
    # You need to add logic to check if the file is uploaded and if its format is OCTA
    # This is a placeholder for the file format checking mechanism
    if file_path.endswith('.OCT'):  # Assuming '.octa' is the file extension for OCTA format
        measure_button['state'] = 'normal'
    else:
        measure_button['state'] = 'disabled'

def enable_diagnose_button(file_path):
    # You need to add logic to check if the file is uploaded and if its format is OCTA
    # This is a placeholder for the file format checking mechanism
    if file_path.endswith('.OCT'):  # Assuming '.octa' is the file extension for OCTA format
        diagnose_btn['state'] = 'normal'
    else:
        diagnose_btn['state'] = 'disabled'

# Creating retinal scan label for 1st page
def layer(master):
    # Create the main frame that will hold the retina details section
    layer_frame = Frame(master, borderwidth=2, relief="groove", bg="white")
    layer_frame.place(x=85, y=435, width=434, height=175)

    # Place the "Retina Details" label with shadow in the retina frame
    create_label_with_shadow(layer_frame, "  Layer Details", 0, 0, 53)

    return layer_frame

# Creating OPTHOTOOL TECHNOLGY label for 2nd page
def opthotool_techlology2(newWindow):
    global logo_img

    optho_label = Label(newWindow, text ="OPTHOTOOL TECHNOLOGY", width=100, height=2, font = "Karla 10 bold", borderwidth=2, relief="groove")
    optho_label.config(bg= "#4990FB", fg= "white")
    optho_label.pack(pady = 0)

    logo2 = (Image.open("logo.png"))
    logo3 = logo2.resize((35,30))
    logo_img1 = ImageTk.PhotoImage(logo3)

    # # Create a Label Widget to display the text or Image
    label_logo2 = Label(newWindow, image = logo_img1)
    label_logo2.config(bg="#4990FB")
    label_logo2.pack()
    label_logo2.place(x=620,y=2)

# create a text box where selected file name will display
def confidence_score(newWindow):
    confidence_score_master_label = Label(newWindow, anchor="w", width=54, height=10, font = "Karla 10 bold", relief="groove", borderwidth=2, pady =10)
    confidence_score_master_label.config(bg= "white", fg= "black")
    confidence_score_master_label.pack(pady = 0)
    confidence_score_master_label.place(x=66,y= 90)

    confidence_score_label = Label(confidence_score_master_label, text =" Diagnostic Prediction", anchor="w", width=54, height=2, font = "Karla 10 bold")
    confidence_score_label.config(bg= "#9CE2F8", fg= "black")
    confidence_score_label.pack(pady = 0)
    confidence_score_label.place(x=0,y=0)


def confidence_score_info(newWindow):
    model_prediction = ML_MODEL.MLmodel()

    diabetic = Text(newWindow, height = 2, width = 20,font = "Karla 12",relief="flat")
    diabetic.place(x=150,y=170)
    diabetic.insert(END," Diabetic Retinopathy : ")

    prediction = Text(newWindow, height = 2, width = 15, font = "Karla 12",relief="flat")
    prediction.place(x=330,y=170)
    prediction.insert(END,model_prediction)

    # Change text color based on the prediction
    if model_prediction.lower() == "positive":
        prediction.config(fg="Red")  # Red for positive prediction
    else:
        prediction.config(fg="Green")  # Green for negative prediction

    # msg = "Based on the scans, chance of damage reversal:"
    # reversal_msg = Text(newWindow, height = 2, width = len(msg),font = "Karla 12",relief="flat")
    # reversal_msg.place(x=80,y=200)
    # reversal_msg.insert(END,msg)

    # percent = Text(newWindow, height = 1, width = 4,font = "Karla 30",relief="flat")
    # percent.place(x=270,y=250)
    # percent.insert(END,"95%")

# function to open a new window 
# on a button click
def openDiagsoneWindow(master):  
    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(master)
 
    # sets the title of the
    # Toplevel widget
    # newWindow.title("Patient Name: Dummy Person")
    
    #Set background color
    newWindow.configure(bg="white")
 
    # sets the geometry of toplevel
    newWindow.geometry("600x400")

    newWindow.resizable(False, False)


    opthotool_techlology2(newWindow)
    confidence_score(newWindow)
    confidence_score_info(newWindow)

# create a diagnose button that will open a new window on button click
def diag_button(master):
    global diagnose_btn

    style = ttk.Style()
    style.theme_use('clam')  # Use the 'clam' theme which allows for more style customizations
    style.configure('Diag.TButton', font='Karla 12 bold', background='#4990FB', foreground='white', borderwidth=0)
    style.map('Diag.TButton',
          foreground=[('disabled', 'white')],
          background=[('disabled', '#4990FB')])

    diagnose_btn = ttk.Button(master, text ="Diagnose", style='Diag.TButton', command = lambda:openDiagsoneWindow(master), state='disabled')
    diagnose_btn.place(x=240,y=775,width=150, height=40)

def layerDetails(master):
    global from_combo, to_combo, thickness_entry, check_fovea, check_parafovea, check_perifovea, calculate_button
    global fovea_var, parafovea_var, perifovea_var

    style = ttk.Style()
    style.theme_use('clam')

    # Configure the style to have a white background
    style.configure('My.TFrame', background='white')
    style.configure('TLabel', background='white')
    style.configure('TButton', background='white') # If you have buttons
    style.configure('TCheckbutton', background='white')
    style.configure('TEntry', fieldbackground='white', background='white')
    style.configure('TCombobox', fieldbackground='white', background='white')

    # Apply map configurations for various widget states
    style.map('TLabel', background=[('disabled', 'white'), ('active', 'white')])
    style.map('TButton', background=[('active', 'white'), ('disabled', 'white')]) # If you have buttons
    style.map('TCheckbutton',
              background=[('active', 'white'), ('!disabled', 'white')],
              indicatorcolor=[('selected', 'white'), ('!selected', 'white')],
              focuscolor=[('focus', 'none'), ('!focus', 'none')])
    style.map('TEntry',
              fieldbackground=[('disabled', 'white')])
    style.map('TCombobox',
              fieldbackground=[('readonly', 'white')],
              background=[('readonly', 'white')],
              selectbackground=[('readonly', 'white')],
              selectforeground=[('readonly', 'black')])
    
    layer_names = [
        'Nerve Fiber Layer',
        'GCL + IPL',
        'Inner Nuclear Layer',
        'Outer Plexiform Layer',
        'Outer Nuclear Layer',
        'Ellipsoid Zone',
        'Retinal Pigment Epithelium',
        'Choroid'
    ]

    frame = ttk.Frame(master, padding="10", style='My.TFrame')
    frame.place(x=118, y=485)

    # Create labels with white background
    from_label = ttk.Label(master, text="From: ", font="Karla 10", style='TLabel')
    from_label.pack()
    from_label.place(x=120, y=485)

    # Create dropdown menus with white background
    from_combo = ttk.Combobox(master, values=layer_names, state="disabled", width=22, background= "white", style='TCombobox')
    from_combo.place(x=215,y=485)

    to_label = ttk.Label(master, text="To: ", font="Karla 10", style='TLabel')
    to_label.pack()
    to_label.place(x=120, y=515)

    to_combo = ttk.Combobox(master, values=layer_names, state="disabled", width=22, background= "white", style='TCombobox')
    to_combo.place(x=215,y=515)

    # Thickness entry moved up next to 'To' combobox
    thickness_label = ttk.Label(master, text="Thickness: ", font="Karla 10", style='TLabel')
    thickness_label.pack()
    thickness_label.place(x=120,y=545)

    thickness_entry = ttk.Entry(master, state="disabled", width=24, style='TEntry')
    thickness_entry.pack()
    thickness_entry.place(x=215,y=545)

    from_combo.current(0)
    to_combo.current(0)

    # Set the initial state of the comboboxes to be blank
    from_combo.set('')
    to_combo.set('')

    fovea_var = tk.IntVar()
    parafovea_var = tk.IntVar()
    perifovea_var = tk.IntVar()

    check_fovea = ttk.Checkbutton(master, state='disabled', text=" Fovea", variable=fovea_var, style='TCheckbutton', takefocus=0)
    check_parafovea = ttk.Checkbutton(master, state='disabled', text=" Parafovea", variable=parafovea_var, style='TCheckbutton',takefocus=0)
    check_perifovea = ttk.Checkbutton(master, state='disabled', text=" Perifovea", variable=perifovea_var, style='TCheckbutton',takefocus=0)

    check_fovea.place(x=395, y=485)
    check_parafovea.place(x=395, y=515)
    check_perifovea.place(x=395, y=545)
    
    def split_bscan(bscan_image):
        # Define regions based on image size
        _, width, _ = bscan_image.shape

        perifovea_line = width // 3
        fovea_start = perifovea_line
        fovea_end = 2 * perifovea_line
        parafovea_line = 2 * width // 3

        return perifovea_line, fovea_start, fovea_end, parafovea_line


    def calculate_thickness():
        from_layer = from_combo.get()
        to_layer = to_combo.get()
        is_fovea = fovea_var.get() == 1
        is_parafovea = parafovea_var.get() == 1
        is_perifovea = perifovea_var.get() == 1
        image_path = "oct_test1/segmented_images/predicted_middle.png"
        bscan_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

        _, fovea_start, fovea_end, width = split_bscan(bscan_image)

        # Ensure that the selections are valid
        if from_layer and to_layer:
            try:
                cropped_images = []
                # Handle region combinations first
                if is_fovea and is_parafovea and is_perifovea:
                    cropped_images.append(bscan_image)
                elif not any([is_fovea, is_parafovea, is_perifovea]):
                    cropped_images.append(bscan_image)
                else:
                    if is_fovea and is_parafovea:
                        cropped_images.append(bscan_image[:, fovea_start:, :])
                    elif is_fovea and is_perifovea:
                        cropped_images.append(bscan_image[:, :fovea_end, :])
                    elif is_perifovea and is_parafovea:
                        cropped_images.append(bscan_image[:, :fovea_start, :])
                        cropped_images.append(bscan_image[:, fovea_end:, :])
                    else:
                        if is_fovea:
                            cropped_images.append(bscan_image[:, fovea_start:fovea_end, :])
                        if is_parafovea:
                            cropped_images.append(bscan_image[:, fovea_end:, :])
                        if is_perifovea:
                            cropped_images.append(bscan_image[:, :fovea_start, :])

                # Calculate thickness for each cropped image
                total_thickness = 0
                for cropped_image in cropped_images:
                    layer_thickness = LAYER_MEASUREMENT.calculate_thicknesses(
                        cropped_image,
                        layer1=layer_names.index(from_layer) + 1,
                        layer2=layer_names.index(to_layer) + 1
                    )
                    layer_thickness_value = layer_thickness.split()[0]  # Get the numeric part
                    total_thickness += float(layer_thickness_value)

                # Handle the averaging of thickness if multiple regions are processed
                if len(cropped_images) > 1:
                    average_thickness = total_thickness / len(cropped_images)
                    formatted_thickness = "{:.4f}".format(average_thickness)
                    thickness_entry.delete(0, tk.END)
                    thickness_entry.insert(0, formatted_thickness)
                else:
                    formatted_total_thickness = "{:.4f}".format(total_thickness)
                    thickness_entry.delete(0, tk.END)
                    thickness_entry.insert(0, formatted_total_thickness)

            except ValueError as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "Please select both 'From' and 'To' layers.")

    style = ttk.Style()
    style.theme_use('clam')  # Use the 'clam' theme which allows for more style customizations
    style.configure('Calc.TButton', font='Karla 10 bold', background='#4990FB', foreground='white', borderwidth=0)
    style.map('Calc.TButton',
          foreground=[('disabled', 'white')],
          background=[('disabled', '#4990FB')])
    
   # Set up the Calculate button
    calculate_button = ttk.Button(master, style = 'Calc.TButton', state='disabled', width=10, text="Calculate", takefocus=0, command= calculate_thickness)
    calculate_button.place(x=250,y=575)

def initialize_empty_frames(master):

    # Setting up the style for the notebook and tabs
    style = ttk.Style()
    theme_name = style.theme_use('clam')
    style.configure(f"{theme_name}.TNotebook", background='white')
    style.configure(f"{theme_name}.TNotebook.Tab", background='white')
    style.configure(f"{theme_name}.TFrame", background='white')

    # Define the dimensions and positions for the frames
    frame_specs = [
        {'width': 400, 'height': 300, 'x': 550, 'y': 110},
        {'width': 400, 'height': 300, 'x': 1000, 'y': 110},
        {'width': 400, 'height': 300, 'x': 550, 'y': 470},
        {'width': 400, 'height': 300, 'x': 1000, 'y': 470},
    ]

    frames = []
    for specs in frame_specs:
        frame = tk.Frame(master, width=specs['width'], height=specs['height'], borderwidth=2, relief='groove')
        # Place the frame at the specified x and y coordinates
        frame.place(x=specs['x'], y=specs['y'])
        frames.append(frame)

    return frames

import BVT_VPI_BVD as OCTA_FEATURES
import AVA as AVA

filepath = 'OCTA.png'
a_path = 'oct_test1/AVA/a_map.png'
v_path = 'oct_test1/AVA/v_map.png'

BVD , VPI, BVT = OCTA_FEATURES.OCTA_Features(filepath)
A_PID , V_PID, AV_PIDR = AVA.AVA_features(a_path, v_path)

def octa_features_window(master):
    octa_window = Toplevel(master)
    octa_window.title("OCTA Features")
    octa_window.configure(bg="white")
    octa_window.geometry("600x550")
    octa_window.resizable(False, False)

    # Frame for the table
    table_frame = tk.Frame(octa_window, bg="white", relief="groove")
    table_frame.pack(pady=20)
    table_frame.place(x=65, y=110, width=470, height=470)

    # Data as seen in the image
    data = [
        (" OCTA Features", " Values"),
        (" Vessel Perimeter Index  (VPI)             ", " " + str(VPI)),
        (" Blood Vessel Tortuosity (BVT)             ", " " + str(BVT)),
        (" Blood Vascular Density (BVD)              ", " " + str(BVD)),
        (" Artery Perfusion Intensity Density (A_PID)", " " + str(A_PID)),
        (" Vein Perfusion Intensity Density (V_PID)  ", " " + str(V_PID)),
        (" Artery Vein PID Ratio (AV_PID)            ", " " + str(AV_PIDR))
    ]

    # Create the headers and rows of the table inside the table frame
    for i, (feature, value) in enumerate(data):
        bg_color = '#9CE2F8' if i == 0 else 'white'  # Header has a different color
        fg_color = 'black' if i == 0 else 'black'

        feature_label = tk.Label(table_frame, text=feature, width=30, height= 3, anchor='w', bg=bg_color, fg=fg_color, borderwidth=1, relief="solid")
        feature_label.grid(row=i, column=0, sticky='ew')

        value_label = tk.Label(table_frame, text=value, width=20, height= 3, anchor='w', bg=bg_color, fg=fg_color, borderwidth=1, relief="solid")
        value_label.grid(row=i, column=1, sticky='ew')

    # Allow the columns to stretch to fill the space
    table_frame.grid_columnconfigure(0, weight=1)
    table_frame.grid_columnconfigure(1, weight=1)

    opthotool_techlology2(octa_window)

def OCTA_features(master):
    global Table_button
    global octa_button
  
    Table_button = Image.open("Table_button.png")
    Table_button = Table_button.resize((20, 20))
    Table_button = ImageTk.PhotoImage(Table_button)

    octa_button = Button(master, image = Table_button, command = lambda: octa_features_window(master), state = 'disabled')
    octa_button.place(x=150, y=690)

def enable_octa_button(file_path):
    # You need to add logic to check if the file is uploaded and if its format is OCTA
    # This is a placeholder for the file format checking mechanism
    if file_path.endswith('.png'):  # Assuming '.octa' is the file extension for OCTA format
        octa_button['state'] = 'normal'
    else:
        octa_button['state'] = 'disabled'

def enable_widgets(file_path):
    # Check if the selected file has an .OCT extension and enable or disable widgets accordingly
    if file_path.lower().endswith('.oct'):
        # Enable widgets for .OCT files
        from_combo['state'] = 'readonly'
        to_combo['state'] = 'readonly'
        thickness_entry['state'] = 'normal'
        check_fovea['state'] = 'normal'
        check_parafovea['state'] = 'normal'
        check_perifovea['state'] = 'normal'
        calculate_button['state'] = 'normal'

        # Reset the widgets to default values or clear them
        from_combo.set('')  # Clear the selection or set default value
        to_combo.set('')    # Clear the selection or set default value
        thickness_entry.delete(0, tk.END)
        thickness_entry.insert(0, '')  # Clear the entry or set default value
        fovea_var.set(0)  # Uncheck the checkbox
        parafovea_var.set(0)  # Uncheck the checkbox
        perifovea_var.set(0)  # Uncheck the checkbox

    else:
        # Disable widgets for non-.OCT files
        from_combo['state'] = 'disabled'
        to_combo['state'] = 'disabled'
        thickness_entry['state'] = 'disabled'
        check_fovea['state'] = 'disabled'
        check_parafovea['state'] = 'disabled'
        check_perifovea['state'] = 'disabled'
        calculate_button['state'] = 'disabled'

        # Reset the widgets to default values or clear them
        from_combo.set('')  # Clear the selection or set default value
        to_combo.set('')    # Clear the selection or set default value
        thickness_entry.delete(0, tk.END)
        thickness_entry.insert(0, '')  # Clear the entry or set default value
        fovea_var.set(0)  # Uncheck the checkbox
        parafovea_var.set(0)  # Uncheck the checkbox
        perifovea_var.set(0)  # Uncheck the checkbox
    

