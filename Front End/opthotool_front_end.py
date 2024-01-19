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
def retina(master):
    # Create the main frame that will hold the retina details section
    retina_frame = Frame(master, borderwidth=2, relief="groove", bg="white")
    retina_frame.place(x=85, y=430, width=434, height=327)

    # Place the "Retina Details" label with shadow in the retina frame
    create_label_with_shadow(retina_frame, "  Retina Details", 0, 0, 53)

    return retina_frame

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

 #oct-converter
def oct_conversion(name_browser):
    file_type = os.path.splitext(name_browser)[1].upper().replace(".", "")
    
    if file_type == '.oct'
        oct_converter_poct(name_browser)
    if file_type == '.OCT'
        oct_converter_boct(name_browser)
    if file_type == '.fds'
        oct_converter_fds(name_browser)
    if file_type == '.fda'
        oct_converter_fda(name_browser)
    if file_type == '.img'
        oct_converter_img(name_browser)
    if file_type == '.dcm'
        oct_converter_dcm(name_browser)
    if file_type == '.e2e'
        oct_converter_e2e(name_browser)
 
    return
 
# display file button
def file_upload_btn(master, table_select):
    def browse():
        f_path = askopenfilename(initialdir="/", title="Select File", filetypes=(("PNG files", "*.png*"), ("All Files", "*.*")))
        if f_path:  # If a file was selected
            name_browser = os.path.basename(f_path)
            file_name(master, table_select, name_browser)
            
    
    upload_file_btn = Button(master, text="Choose File", command=browse, borderwidth=2, bg='gray', font="Karla 10", fg='black')
    upload_file_btn.place(x=340, y=129, width=100, height=25)

    return upload_file_btn


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

def tabs(master, frames, num_tabs_list):
    style = ttk.Style()
    theme_name = style.theme_use('clam')
    style.configure(f"{theme_name}.TNotebook", background='white')
    style.configure(f"{theme_name}.TNotebook.Tab", background='white')

    for i, frame in enumerate(frames):
        # Main tab control
        main_tabControl = ttk.Notebook(frame)
        main_tabControl.config(width=400, height=300)  # Set the initial size of the notebook

        # Main tab
        main_tab = ttk.Frame(main_tabControl)
        main_tabControl.add(main_tab, text=f"Tab 1")

        # Add the image to the main tab
        image_files = ["test_image1.png", "test_image2.png", "test_image3.png", "test_image4.png"]
        try:
            img = Image.open(image_files[i])
            img_resized = img.resize((400, 300))
            img_photo = ImageTk.PhotoImage(img_resized)
            label = tk.Label(main_tab, image=img_photo)
            label.image = img_photo  # keep a reference to the image
            label.pack(padx=10, pady=10)
        except Exception as e:
            print(f"Error loading image {image_files[i]}: {e}")


        # Add sub-tabs as specified by num_tabs_list
        for j in range(num_tabs_list[i]):
            sub_tab = ttk.Frame(main_tabControl)
            main_tabControl.add(sub_tab, text=f"Tab {j + 2}")

        # Pack the main tab control
        main_tabControl.pack(expand=1, fill="both")
     
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
retina(master)
diag_button(master)
display_eye_side(master)
table_select = selectScanTabel(master,data)
file_upload_btn(master, table_select)
file_name(master,table_select,name_borwser)
retinaDetailsTabel(master)
frames = [frame, frame2,frame3, frame4]  # Create a list of frames for the tabs
num_tabs_list = [0, 2, 0, 1]  # Example number of sub-tabs for each main tab
tabs(master, frames, num_tabs_list)

# mainloop, runs infinitely
mainloop()









