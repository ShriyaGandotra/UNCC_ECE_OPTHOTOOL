# AUTHOR: SHRIYA GANDOTRA
# This file  sets up the main window (master), configures its appearance, 
# and calls various functions from different modules (MAIN_COMPONENTS, UPLOAD_FILE, TAB, TAB2) 
# to set up the UI elements like buttons, labels, tabs, and file upload functionality.


# Import required modules from Tkinter and other components of the application
from tkinter import *
import tkinter as tk
from tkinter import ttk
import Components as MAIN_COMPONENTS
import File_Upload as UPLOAD_FILE
import Tabs as TAB
import Tabs2 as TAB2
import Config as CONFIG
import octa_tabs as OCTA_TAB

# Initialize the main application window (master frame)
master = Tk()

# Placeholder for the file name selected by the user
name_borwser = ""

# Initialize data variable, possibly for holding application data
data = ()
 
# Configure the size and background color of the main application window
master.geometry("600x400")
master.configure(bg="white")

# Set the title of the main application window with patient information
master.title("Patient Name: Dummy Person | DOB: 06/15/2002 | ID: 11223344 ")

# Path variables for icons used in the GUI, which are loaded within components
measure_icon = "measurement_button.png"
logo_img = "logo.png"
up_image = "up_button.png"
down_image = "down_button.png"
Table_button = "Table_button.png"
filepath = 'OCTA.png'

# Setup and display of all GUI components 
MAIN_COMPONENTS.start_screen(master)
MAIN_COMPONENTS.opthotool_techlology(master)
MAIN_COMPONENTS.upload(master)
MAIN_COMPONENTS.tools(master)
MAIN_COMPONENTS.layer(master)
MAIN_COMPONENTS.diag_button(master)
MAIN_COMPONENTS.layerDetails(master)
MAIN_COMPONENTS.OCTA_features(master)
MAIN_COMPONENTS.initialize_empty_frames(master)

# # Initalize Enface and Contour Mapping Tab within the application and thier funcationalites
# # frames, num_tabs_list = TAB.initialize_tabs(master)
# frames_octa, tab_names_list_octa = OCTA_TAB.initialize_tabs3(master)

# Setup the scan table for file selection and interaction
table_select = UPLOAD_FILE.selectScanTabel(master,data)

# Create a file upload button which allows users to select and upload files alongside conversions
UPLOAD_FILE.file_upload_btn(master, table_select)

# Display the file name that has been selected or uploaded by the user
UPLOAD_FILE.file_name(master,table_select,name_borwser)

# Initalize skeletonization, perimeter mapping and RAW OCT-B scan Tabs and thier funcationalites
# TAB2.main_application(CONFIG.selected_file_path, master)

# mainloop, runs infinitely
mainloop()



