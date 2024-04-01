# Opthotool Front End  - GUI COMPONENTS
# Author : Shriya Gandotra
# Date updated : 3/28/2024

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from PIL import Image, ImageTk
from tkinter import Label
from tkinter import ttk
import Distance_Tool as DISTANCE_TOOL
import ML_Model as ML_MODEL
import Layer_Measurement as LAYER_MEASUREMENT
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

    # Create the main frame that will hold the retina details section
    tools_frame = Frame(master, borderwidth=2, relief="groove", bg="white")
    tools_frame.place(x=85, y=640, width=434, height=107)

    create_label_with_shadow(tools_frame, "  Tools", 0, 0, 53)

    # Measure tool button
    measure_icon = Image.open("measure_button.png")
    measure_icon = measure_icon.resize((20, 20))
    measure_icon = ImageTk.PhotoImage(measure_icon)

    measure_button = Button(master, text = "Measure Tool", command = DISTANCE_TOOL.create_distance_calculator)
    measure_button = Button(master, image = measure_icon, command = DISTANCE_TOOL.create_distance_calculator)
    measure_button.place(x=95, y=690)


    return tools_frame

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
    confidence_score_master_label = Label(newWindow, anchor="w", width=55, height=15, font = "Karla 10 bold", relief="groove")
    confidence_score_master_label.config(bg= "white", fg= "black")
    confidence_score_master_label.pack(pady = 0)
    confidence_score_master_label.place(x=65,y= 90)
    
    confidence_score_label = Label(newWindow, text ="Confidence Score", anchor="w", width=55, height=2, font = "Karla 10 bold")
    confidence_score_label.config(bg= "#9CE2F8", fg= "black")
    confidence_score_label.pack(pady = 0)
    confidence_score_label.place(x=67,y=92)

def confidence_score_info(newWindow):
    model_prediction = ML_MODEL.MLmodel()

    diabetic = Text(newWindow, height = 2, width = 20,font = "Karla 12",relief="flat")
    diabetic.place(x=80,y=150)
    diabetic.insert(END,"Diabetic Retinopathy: ")

    prediction = Text(newWindow, height = 2, width = 20,font = "Karla 12",relief="flat",fg="Red")
    prediction.place(x=270,y=150)
    prediction.insert(END,model_prediction)

    msg = "Based on the scans, chance of damage reversal:"
    reversal_msg = Text(newWindow, height = 2, width = len(msg),font = "Karla 12",relief="flat")
    reversal_msg.place(x=80,y=200)
    reversal_msg.insert(END,msg)

    percent = Text(newWindow, height = 1, width = 4,font = "Karla 30",relief="flat")
    percent.place(x=270,y=250)
    percent.insert(END,"95%")

# function to open a new window 
# on a button click
def openDiagsoneWindow(master):  
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

    newWindow.resizable(False, False)

    opthotool_techlology2(newWindow)
    confidence_score(newWindow)
    confidence_score_info(newWindow)

# create a diagnose button that will open a new window on button click
def diag_button(master):
    diagnose_btn = Button(master, text ="Diagnose", command = lambda:openDiagsoneWindow(master),borderwidth=0, bg='#4990FB',font="Karla 12 bold", fg='white',padx=20,pady=5)
    diagnose_btn.place(x=245,y=775)

def layerDetails(master):
    style = ttk.Style()
    style.theme_use('clam')
    # Configure the style to have a white background
    style.configure('My.TFrame', background='white')
    style.configure('TLabel', background='white')
    style.configure('TCheckbutton', background='white')
    # style.configure('TCombobox', fieldbackground='white', background='white', selectbackground = 'white' , selectforeground = 'white')
    style.configure('TEntry', fieldbackground='white', background='white')

    style.map('TCombobox',
              fieldbackground=[('readonly', 'white'), ('focus', 'white')],
              background=[('readonly', 'white'), ('focus', 'white')],
              selectbackground=[('readonly', 'white'), ('focus', 'white')],
              selectforeground=[('readonly', 'black')])
    style.configure('TCombobox', fieldbackground='white', background='white')

    
 
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
    from_label.place(x=111, y=485)

    # Create dropdown menus with white background
    from_combo = ttk.Combobox(master, values=layer_names, state="readonly", width=22, background= "white", style='TCombobox')
    from_combo.place(x=180,y=485)

    to_label = ttk.Label(master, text="To: ", font="Karla 10", style='TLabel')
    to_label.pack()
    to_label.place(x=111, y=515)

    to_combo = ttk.Combobox(master, values=layer_names, state="readonly", width=22, background= "white", style='TCombobox')
    to_combo.place(x=180,y=515)

    # Thickness entry moved up next to 'To' combobox
    thickness_label = ttk.Label(master, text="Thickness: ", font="Karla 10", style='TLabel')
    thickness_label.pack()
    thickness_label.place(x=111,y=545)

    thickness_entry = ttk.Entry(master, width=24, style='TEntry')
    thickness_entry.pack()
    thickness_entry.place(x=180,y=545)

    from_combo.current(0)
    to_combo.current(0)

    # Set the initial state of the comboboxes to be blank
    from_combo.set('')
    to_combo.set('')

        # Define the function that gets called when the calculate button is clicked
    def calculate_thickness():
        from_layer = from_combo.get()
        to_layer = to_combo.get()
        
        # Ensure that the selections are valid
        if from_layer and to_layer:
            try:
                # Calculate the total thickness based on selected layers
                total_thickness = LAYER_MEASUREMENT.calculate_thicknesses(
                    filepath="oct_test1/segmented_images/predicted_middle.png",
                    layer1=layer_names.index(from_layer) + 1,
                    layer2=layer_names.index(to_layer) + 1
                )
                thickness_entry.delete(0, tk.END)
                thickness_entry.insert(0, str(total_thickness))
            except ValueError as e:
                tk.messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            tk.messagebox.showwarning("Warning", "Please select both 'From' and 'To' layers.")

   # Set up the Calculate button
    calculate_button = tk.Button(master, width=10, text="Calculate", borderwidth=0, bg='#4990FB',font="Karla 10 bold", fg='white', command= calculate_thickness)
    calculate_button.place(x=150,y=575)


    # Create checkboxes with white background
    check_fovea = ttk.Checkbutton(master, text="Fovea", style='TCheckbutton',)
    check_parafovea = ttk.Checkbutton(master, text="Parafovea", style='TCheckbutton')
    check_perifovea = ttk.Checkbutton(master, text="Perifovea", style='TCheckbutton')

    # Place checkboxes with uniform padding
    check_fovea.place(x=360,y=485)
    check_parafovea.place(x=360, y=515)
    check_perifovea.place(x=360,y=545)