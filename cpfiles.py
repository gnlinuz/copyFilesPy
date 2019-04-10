"""
    This is a utility that copy files from source to destination
    (and creates the destination directory if does not exists)
    only if the source date-time attributes are different than the destination,
    otherwise if source and destination date-time is the same no files are copied.
    Created 10/04/2019
    Editor: George Nikolaidis
"""

import os
import shutil
import time

SOURCE_PATH = "c:\\tmp"
DESTINATION_PATH = "e:\\temp"
DEST_DIC = {}

def copy_files(s_files, s_path, d_path):
    """
    Function that takes arguments a list of directory files
    the source path and the destination path, and copy files
    from source to destination without change the file attributes.
    """
    for f_name in s_files:
        f_file_name = os.path.join(s_path, f_name)
        if os.path.isfile(f_file_name):
            shutil.copy2(f_file_name, d_path)
            print('.', end='')


# check if folder exists, if not create it
if not os.path.exists(DESTINATION_PATH):
    os.makedirs(DESTINATION_PATH)
else:
    print("Directory exists...no need to create it")

# get directory listing
SRC_FILES = os.listdir(SOURCE_PATH)
DEST_FILES = os.listdir(DESTINATION_PATH)

# if directory listing is empty copy all the files without any check
if DEST_FILES == []:
    print("Directory empty, copy all files...from source to destination.")
    copy_files(SRC_FILES, SOURCE_PATH, DESTINATION_PATH)
else:
    # create a dictonary of the destination files as keys and values date-time stamp of each file
    for dest_file_name in DEST_FILES:
        full_dest_file_name = os.path.join(DESTINATION_PATH, dest_file_name)
        stamp_dest = time.ctime(os.path.getmtime(full_dest_file_name))
        DEST_DIC[dest_file_name] = stamp_dest
    for file_name in SRC_FILES:
        full_file_name = os.path.join(SOURCE_PATH, file_name)
        STAMP_SRC = time.ctime(os.path.getmtime(full_file_name))
        # get date-time stamp of source files and compare it with the destination
        if STAMP_SRC == DEST_DIC.get(file_name):
            print('.', end='')
        else:
            # means that source date-time stamp is different that destination so copy the file
            if os.path.isfile(full_file_name):
                shutil.copy2(full_file_name, DESTINATION_PATH)
                print("copying file {}".format(full_file_name))
