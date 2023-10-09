#------------------------------------------- LIBRARIES ---------------------------------------------------#
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
import os

#------------------------------------------- FIRST PAGE --------------------------------------------------#
# creates a Tk() object
master = Tk()

name_borwser = ""
 
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

# Creating OPTHOTOOL TECHNOLGY label for 2nd page
def opthotool_techlology2(newWindow):
    optho_label = Label(newWindow, text ="OPTHOTOOL TECHNOLOGY", width=100, height=2, font = "Karla 10 bold", borderwidth=2, relief="groove")
    optho_label.config(bg= "#4990FB", fg= "white")
    optho_label.pack(pady = 0)

# Creating TOOLS label for 1st page
def tools(master):
    tools_label = Label(master, text ="TOOLS", anchor="w", width=180, height=2, font = "Karla 8 bold")
    tools_label.config(bg= "#9CE2F8", fg= "black")
    tools_label.pack(pady = 0)

# Creating upload scan label for 1st page
def upload(master):
    upload_master_label = Label(master, anchor="w", width=40, height=20, font = "Karla 10 bold", borderwidth=1, relief="groove")
    upload_master_label.config(bg= "white", fg= "black")
    upload_master_label.pack(pady = 0)
    upload_master_label.place(x=85,y=100)

    # Creating upload label
    upload_label = Label(master, text ="Upload Scan", anchor="w", width=40, height=2, font = "Karla 10 bold", borderwidth=0.5, relief="solid")
    upload_label.config(bg= "#9CE2F8", fg= "black")
    upload_label.pack(pady = 0)
    upload_label.place(x=85,y=100)

# Creating select scan label for 1st page
def select(master):
    select_label = Label(master, text ="Select Scan", anchor="w", width=40, height=2, font = "Karla 10 bold", borderwidth=0.5, relief="solid")
    select_label.config(bg= "#9CE2F8", fg= "black")
    select_label.pack(pady = 0)
    select_label.place(x=85,y=230)

# Creating retinal scan label for 1st page
def retina(master):
    retina_master_label = Label(master, anchor="w", width=40, height=20, font = "Karla 10 bold", borderwidth=0.5, relief="groove")
    retina_master_label.config(bg= "white", fg= "black")
    retina_master_label.pack(pady = 0)
    retina_master_label.place(x=85,y=450)

    retina_label = Label(master, text ="Retina Details", anchor="w", width=40, height=2, font = "Karla 10 bold", borderwidth=0.5, relief="solid")
    retina_label.config(bg= "#9CE2F8", fg= "black")
    retina_label.pack(pady = 0)
    retina_label.place(x=85,y=450)

# create a diagnose button that will open a new window on button click
def diag_button(master):
    diagnose_btn = Button(master, text ="Daignose", command = openDiagsoneWindow,borderwidth=0, bg='#4990FB',font="Karla 12 bold", fg='white',padx=20,pady=5)
    # diagnose_btn.bind("<Enter>", func=lambda e: diagnose_btn.config(background='white'))
    # diagnose_btn.bind("<Leave>", func=lambda e: diagnose_btn.config(background='#4990FB'))
    diagnose_btn.place(x=180,y=795)
    #diagnose_btn.pack(pady = 10)

# create a text box where selected file name will display
def display_name(master):
    name = "Dummy_Left_Eye"

    T = Text(master, height = 2, width = 20,font = "Karla 12",relief="flat")
    T.place(x=450,y=100)
    T.insert(END,name)

# create a text box where selected file name will display
def display_eye_side(master):
    eye_side = "Left/ODD"

    T = Text(master, height = 2, width = 20,font = "Karla 12",relief="flat")
    T.place(x=1230,y=100)
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
def file_name(master,name):
    if name is "":
        name = "No File Chosen"

    file_n = Text(master, height = 1, width = len(name)+10, font = "Karla 10",borderwidth=2, relief="groove",spacing1=5)
    file_n.place(x=110,y=165)
    file_n.insert(END,name)

    return file_n
 
# display file button
def file_upload_btn(master):
    upload_file_btn = Button(master, text ="Choose File", command = browse,borderwidth=0, bg='gray',font="Karla 10", fg='black',border=1)
    upload_file_btn.place(x=283,y=165)


# function to open file explorer to browse files
def browse():
   f_path = askopenfilename(initialdir="/",title="Select File", filetypes=(("PNG files","*.png*"),("All Files","*.*")))
   name_borwser = os.path.split(f_path)[1]
   file_n = Text(master, height = 1, width = 20, font = "Karla 10",spacing1=5)
   file_n.place(x=110,y=165)
   file_n.insert(END,name_borwser)
 
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


#----------------------------- Image 1 ----------------------------------#
frame = Frame(master, width=600, height=400)
frame.pack()
frame.place(x=450,y=150)

# Create an object of tkinter ImageTk
img = (Image.open("test_image1.png"))
new_img = img.resize((400,300))
new_img = ImageTk.PhotoImage(new_img)

# Create a Label Widget to display the text or Image
label = Label(frame, image = new_img)
label.pack()

#-------------------------- Image 2 -------------------------------------#
frame2 = Frame(master, width=600, height=400)
frame2.pack()
frame2.place(x=900,y=150)

# Create an object of tkinter ImageTk
img2 = (Image.open("test_image2.png"))
new_img2 = img2.resize((400,300))
new_img2 = ImageTk.PhotoImage(new_img2)

# Create a Label Widget to display the text or Image
label2 = Label(frame2, image = new_img2)
label2.pack()

#--------------------------- Image 3 ------------------------------------#
frame3 = Frame(master, width=600, height=400)
frame3.pack()
frame3.place(x=450,y=470)

# Create an object of tkinter ImageTk
img3 = (Image.open("test_image3.png"))
new_img3 = img3.resize((400,300))
new_img3 = ImageTk.PhotoImage(new_img3)

# Create a Label Widget to display the text or Image
label3 = Label(frame3, image = new_img3)
label3.pack()

#-------------------------- Image 4 -------------------------------------#
frame4 = Frame(master, width=600, height=400)
frame4.pack()
frame4.place(x=900,y=470)

# Create an object of tkinter ImageTk
img4 = (Image.open("test_image4.png"))
new_img4 = img4.resize((400,300))
new_img4 = ImageTk.PhotoImage(new_img4)

# Create a Label Widget to display the text or Image
label4 = Label(frame4, image = new_img4)
label4.pack()

start_screen(master)
opthotool_techlology(master)
tools(master)
upload(master)
select(master)
retina(master)
diag_button(master)
display_name(master)
display_eye_side(master)
layer_segmentation(master)
file_name(master,name_borwser)
file_upload_btn(master)

# mainloop, runs infinitely
mainloop()









