'''Write a program that takes the name of a file as a command-line argument, and
creates a backup copy of that file. The backup should contain an exact copy of the
contents of the original and should, obviously, have a different nam
Hint: By now, you should be getting the idea that there is a built-in way to do the
heavy lifting here! Take a look at the "Brief Tour of the Standard Library" in the doc'''

import sys
import shutil

def create_backup(file_name):
    try:
        backup_name = file_name.split('.')[0] + "_backup." + file_name.split('.')[1]
        
        shutil.copy(file_name, backup_name)
        print(f"Backup created successfully! Backup file: {backup_name}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_name>")
    else:
        file_name = sys.argv[1]
        create_backup(file_name)
