# -*- coding: utf-8 -*-
"""
Use this to rejoin numpy arrays.
(Need to make this dynamic instead of always 4).
Need to turn this into a function
"""
import numpy as np

working_directory = 'C:\\Users\\Team Crazer\\Documents\\data_science_practice\\pgp_aiml\\private_pgp_aiml\\introduction_to_computer_vision\\project\\'
file_root = 'images'
file_ext = '.npy'

data1 = np.load(working_directory + file_root + '1' + file_ext)
data2 = np.load(working_directory + file_root + '2' + file_ext)
data3 = np.load(working_directory + file_root + '3' + file_ext)
data4 = np.load(working_directory + file_root + '4' + file_ext)

data_rejoined = np.dstack((data1, data2, data3, data4))

# # (Tested this against the original data)
# np.array_equal(data, data_rejoined)

np.save(working_directory + file_root + file_ext, data_rejoined)