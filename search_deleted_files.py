import os

def search_deleted_files(directory, files_to_check):
    deleted_files = []

    for file in files_to_check:
        file_path = os.path.join(directory, file)

        # If the file does not exist, add it to the list of deleted files
        if not os.path.exists(file_path):
            deleted_files.append(file_path)

    return deleted_files

directory = "."
files_to_check = ["test.txt"]
deleted_files = search_deleted_files(directory, files_to_check)

if deleted_files:
    print("Deleted files:")
    for file in deleted_files:
        print(file)
else:
    print("No deleted files found.")