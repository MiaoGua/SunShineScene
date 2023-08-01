import os
import shutil

# The directory that contains your save files
source_directory = os.getcwd()

# The directory where you want to move the 'KoiKatuCharaSun' save files
destination_directory_game2 = os.path.join(source_directory, "SunShine")

# Create the destination directory if it doesn't exist
os.makedirs(destination_directory_game2, exist_ok=True)

# Get a list of all the .png files in the source directory
file_list = [f for f in os.listdir(source_directory) if f.endswith('.png')]

total_files = len(file_list)
for i, filename in enumerate(file_list):
    # Construct the full path to the file
    file_path = os.path.join(source_directory, filename)

    # Open the file in binary mode, read it, and decode
    with open(file_path, 'rb') as f:
        content = f.read().decode('utf-8', errors='ignore')

    # Check if the unique string is in the content
    if 'KoiKatuCharaSun' in content:
        # Move the file to the directory for game 2
        shutil.move(file_path, os.path.join(destination_directory_game2, filename))

    print(f"{i+1}/{total_files}")

print("Complete!")


