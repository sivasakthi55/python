import os

def rename_file(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"File '{old_name}' renamed to '{new_name}'.")
    else:
        print(f"Error: '{old_name}' does not exist.")

rename_file("data.txt","info.txt")