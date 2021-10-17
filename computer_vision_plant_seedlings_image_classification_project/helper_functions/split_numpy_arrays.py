# -*- coding: utf-8 -*-
"""
Use this to split numpy arrays to github-friendly sizes.
(Need to make this less manual)
"""

import numpy as np
import os
import math

working_directory = 'C:\\Users\\Team Crazer\\Documents\\data_science_practice\\pgp_aiml\\private_pgp_aiml\\introduction_to_computer_vision\\project\\'
file = 'images.npy'
file_location = working_directory + file


# Split file if too big.
file_size = os.stat(file_location).st_size/(1024*1024)
data = np.load(file_location)

if file_size > 100:
    min_splits = math.ceil(file_size / 100)
    print("file needs to be split at least {} times.".format(min_splits))
    # I need to make this step dynamic.  4 worked for this file,
    #  but I need to set it up 
    x1, x2, x3, x4 = np.dsplit(data, 4)
    np.save(working_directory + "images1.npy", x1)
    np.save(working_directory + "images2.npy", x2)
    np.save(working_directory + "images3.npy", x3)
    np.save(working_directory + "images4.npy", x4)
    
else:
    print("file is small enough that no splitting is necessary.")