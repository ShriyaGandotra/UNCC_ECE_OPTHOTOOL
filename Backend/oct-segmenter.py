#Libraries
import oct_converter.readers
import os
import glob
from PIL import Image


fp = 'C:\Users\adams\Desktop\OCT\ZhangLabData\CellData\OCT\train\NORMAL'

oct_volume = fp.read_oct_volume()
oct_volume.peek(show_contours=True) # plots a montage of the volume, with layer segmentations is available
oct_volume.save('fds_testing.avi')  # save volume as a movie
oct_volume.save('fds_testing.png')  # save volume as a set of sequential images, fds_testing_[1...N].png
oct_volume.save_projection('projection.png') # save 2D projection

