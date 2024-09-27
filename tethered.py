import os
import shutil

# Path to the DCIM folder on the iPhone (replace with the actual path)
iphone_dcim_path = "/Volumes/Apple iPhone/DCIM"

# Destination folder on your computer
destination_folder = "/path/to/destination/folder"

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Iterate over files in the DCIM folder
for filename in os.listdir(iphone_dcim_path):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        source_path = os.path.join(iphone_dcim_path, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.copy2(source_path, destination_path)
        print(f"Copied {filename} to {destination_folder}")