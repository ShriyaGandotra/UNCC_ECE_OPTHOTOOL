import json
import numpy as np
from oct_converter.image_types import OCTVolumeWithMetaData
from PIL import Image
import io
import tempfile
import os
import os.path as osp

# filepath = "/Users/Shriya Gandotra/Desktop/Senior design/oct_test1.OCT"


# convert .fds files to png
def oct_converter_fds(filepath):
    from oct_converter.readers import FDS
    file = FDS(filepath)
    oct_volumes = (file.read_oct_volume())
    oct_volumes.save("image.png")


# convert .fda files to png
def oct_converter_fda(filepath):
    from oct_converter.readers import FDA
    file = FDA(filepath)
    oct_volumes = (file.read_oct_volume())
    oct_volumes.save("image.png")


# conversion of e2e files into png images
def oct_converter_e2e(filepath):
    from oct_converter.readers import E2E
    file = E2E(filepath)
    oct_volumes = (file.read_oct_volume())

    for volume in oct_volumes:
        volume.save("image.png")


# convert .img files to png
def oct_converter_img(filepath):
    from oct_converter.readers import IMG
    file = IMG(filepath)
    oct_volume = (file.read_oct_volume())
    oct_volume.save("image.png")


# conversion of BOCT(bioptigen) files into png images
def oct_converter_boct(filepath):
    from oct_converter.readers import BOCT
    file = BOCT(filepath)
    oct_volumes = file.read_oct_volume()

    for oct in oct_volumes:
        oct.save("image.png")

# # conversion of POCT(optovue) files into png images
# def oct_converter_poct(filepath):
#     from oct_converter.readers import POCT
#     file = POCT(filepath)
#     oct_volumes = file.read_oct_volume()

#     for volume in oct_volumes:
#         volume.save("image.png")


def oct_converter_poct(filepath):
    from oct_converter.readers import POCT

    # Extract the base file name without extension
    base_name = osp.splitext(osp.basename(filepath))[0]

    # Create a directory named after the file if it doesn't exist
    dir_path = osp.join(osp.dirname(filepath), base_name)
    raw_images_path = osp.join(dir_path, 'raw_images')
    os.makedirs(raw_images_path, exist_ok=True)

    # Read OCT volumes
    file = POCT(filepath)
    oct_volumes = file.read_oct_volume()

    # Save each volume in the raw_images directory
    for i, volume in enumerate(oct_volumes):
        volume.save(osp.join(raw_images_path, f"image_{i}.png"))

# convert .dcm files to png
def oct_converter_dcm(filepath):
    from oct_converter.readers import Dicom
    file = Dicom(filepath)
    oct_volumes = (file.read_oct_volume())
    oct_volumes.save("image.png")

# oct_converter_poct(filepath)


