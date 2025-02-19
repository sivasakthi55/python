import os

# 1. Create and Write to a File
def create_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File '{filename}' created and written successfully.")

# 2. Read File
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist.")

# 3. Append to File
def append_to_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write(content)
        print(f"Content appended to '{filename}'.")
    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist.")

# 4. Read File Line by Line
def read_file_by_line(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist.")

# 5. Check if File Exists
def file_exists(filename):
    exists = os.path.exists(filename)
    print(f"File '{filename}' exists: {exists}")
    return exists

# 6. Delete a File
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    else:
        print(f"Error: '{filename}' does not exist.")

# 7. Get File Information
def file_info(filename):
    if os.path.exists(filename):
        info = os.stat(filename)
        print(f"File Information for '{filename}':")
        print(f"  Size: {info.st_size} bytes")
        print(f"  Created: {info.st_ctime}")
        print(f"  Modified: {info.st_mtime}")
    else:
        print(f"Error: '{filename}' does not exist.")

# 8. Copy File Content
def copy_file_content(source, destination):
    try:
        with open(source, 'r') as src, open(destination, 'w') as dest:
            dest.write(src.read())
        print(f"Content copied from '{source}' to '{destination}'.")
    except FileNotFoundError:
        print(f"Error: '{source}' or '{destination}' does not exist.")

# 9. Rename a File
def rename_file(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"File '{old_name}' renamed to '{new_name}'.")
    else:
        print(f"Error: '{old_name}' does not exist.")


# File names
file1 = "example.txt"
file2 = "copy_example.txt"

# Operations
create_file(file1, "This is a test file.\n")
read_file(file1)
append_to_file(file1, "Adding a new line.\n")
read_file(file1)
read_file_by_line(file1)
file_info(file1)
copy_file_content(file1, file2)
file_exists(file2)
rename_file(file2, "renamed_example.txt")
delete_file(file1)
delete_file("renamed_example.txt")
