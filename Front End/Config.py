# config.py
frames = None
frames_octa = None
frames_b = None
num_tabs_list = None
num_tabs_list_octa = None
num_tabs_list_b = None
selected_file_path = None
# Initialize with default tabs or set to None if you prefer to initialize elsewhere
tab_names_list = [
    ["Enface"],
    ["Contour Mapping"]
]
tab_names_list_octa = [
    ["Raw OCT-A"],  # Names for tabs in the first frame
    ["AVA Map"], 
    ["Skeletonized Map"], 
    ["Perimeter Map"]  # Names for tabs in the fourth frame
]
images = []