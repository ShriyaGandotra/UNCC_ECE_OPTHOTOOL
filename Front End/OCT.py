# AUTHOR: SHRIYA GANDOTRA
# This script provides a function, oct_conversion, that acts as a dispatcher for 
# converting various medical image file formats to a standardized form. It checks the file extension of 
# the provided file path and calls the appropriate function from the oct_Converter module for each specific 
# file type, including 'OCT', 'fds', 'fda', 'img', 'dcm', and 'e2e'. 
# Refer to Backend repo for original function

import oct_Converter as OCT
import os

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