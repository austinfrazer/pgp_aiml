# -*- coding: utf-8 -*-
"""
Use this to delete large files.
"""
import os

working_directory = 'C:\\Users\\Team Crazer\\Documents\\data_science_practice\\pgp_aiml\\private_pgp_aiml\\introduction_to_computer_vision\\project\\'
file = 'images.npy'
file_location = working_directory + file


# This step checks creates a list of what items need to be deleted.
folder_contents = os.listdir()
files_to_delete = []
for item in folder_contents:
    
    tmp_file_size = os.stat(item).st_size/(1024*1024)
    print(item, "has file size", round(tmp_file_size, 2))
    
    if tmp_file_size > 100:
        print('\t', item, "will need to be deleted")
        files_to_delete.append(item)

# This step deletes files.
for item in files_to_delete:
    os.remove(item)
    print(item, "has been removed.")