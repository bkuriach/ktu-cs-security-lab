# Write a program to list images, pdf in a directory given.
""" 
This program walks through all files and subdirectories in the given directory and checks 
if each file has one of the given extensions. If a file has one of the extensions, it is 
added to the list of matched files. The extensions are checked in a case-insensitive manner 
by converting the filename to lowercase with the lower method.
"""
import os

def list_files(directory, extensions):
    matched_files = []

    # Walk through all files and subdirectories in the given directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file has one of the given extensions
            if file.lower().endswith(tuple(extensions)):
                file_path = os.path.join(root, file)
                matched_files.append(file_path)

    return matched_files

directory = input("Enter a directory: ")
extensions = [".jpg", ".jpeg", ".png", ".gif", ".pdf"]
files = list_files(directory, extensions)

if files:
    print("Files:")
    for file in files:
        print(file)
else:
    print("No files found.")