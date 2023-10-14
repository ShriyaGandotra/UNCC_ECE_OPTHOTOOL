import json

filepath = ""

#convert .fds files to png
def oct_converter_fds(filepath):
    from oct_converter.readers import FDS
    file = FDS(filepath)
    oct_volumes = (file.read_oct_volume())
    oct_volumes.save("image.png")

#convert .fda files to png
def oct_converter_fda(filepath):
    from oct_converter.readers import FDA
    file = FDA(filepath)
    oct_volumes = (file.read_oct_volume())
    oct_volumes.save("image.png")

#conversion of e2e files into png images
def oct_converter_e2e(filepath):
    from oct_converter.readers import E2E
    file = E2E(filepath)
    oct_volumes = (file.read_oct_volume())
    
    for volume in oct_volumes:
        oct_volumes.peek(show_contours=True)
        volume.save("image.png")

#convert .img files to png
def oct_converter_img(filepath):
    from oct_converter.readers import IMG
    file = IMG(filepath)
    oct_volume = (file.read_oct_volume())
    oct_volume.save("image.png")

#conversion of BOCT(bioptigen) files into png images
def oct_converter_boct(filepath):
    from oct_converter.readers import BOCT
    file = BOCT(filepath)
    oct_volumes = file.read_oct_volume()
    
    for oct in oct_volumes:
        oct_volumes.peek(show_contours=True)
        oct.save("image.png")
        
#conversion of POCT(optovue) files into png images
def oct_converter_poct(filepath):
    from oct_converter.readers import POCT
    file = POCT(filepath)
    oct_volumes = file.read_oct_volume()
    
    for volume in oct_volumes:
        oct_volumes.peek(show_contours=True)
        volume.save("image.png")

#convert .dcm files to png
def oct_converter_dcm(filepath):
    from oct_converter.readers import Dicom
    file = Dicom(filepath)
    oct_volumes = (file.read_oct_volume())
    oct_volumes.save("image.png")