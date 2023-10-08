import json


filepath = ""

#conversion of e2e files into png images
def oct_converter_e2e(filepath):
    from oct_converter.readers import E2E
    
    file = E2E(filepath)
    oct_volumes = (file.read_oct_volume())
    
    for volume in oct_volumes:
        oct_volumes.peek(show_contours=True)
        volume.save("image.png")
        
#conversion of BOCT(bioptigen) files into png images
def oct_converter_oct(filepath):
    from oct_converter.readers import BOCT
    
    file = BOCT(filepath)
    oct_volumes = file.read_oct_volume()
    
    for oct in oct_volumes:
        oct_volumes.peek(show_contours=True)
        oct.save("image.png")
        
#conversion of POCT(optovue) files into png images
def oct_converter_oct(filepath):
    from oct_converter.readers import POCT
    
    file = POCT(filepath)
    oct_volumes = file.read_oct_volume()
    
    for volume in oct_volumes:
        oct_volumes.peek(show_contours=True)
        volume.save("image.png")
