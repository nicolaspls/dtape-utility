import os
import shutil

# Read pictos from pictos.txt
with open('pictos.txt', 'r') as file:
    pictos = file.read().splitlines()

# Prompt the user to input the folder path
input_folder = input("Enter the path to your cache folder: ")
print(f"Input folder path: {input_folder}")

# Construct the path to the output folder
output_folder = os.path.join(os.path.dirname(__file__), "pictos")
print(f"Output folder: {output_folder}")

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print("Output folder created.")

# Function to copy png files
def copy_png_files(source_dir, destination_dir):
    for file in os.listdir(source_dir):
        if file.endswith(".png.ckd") and file[:-8] in pictos:
            shutil.copy(os.path.join(source_dir, file), destination_dir)
            print(f"File {file} copied to output folder.")

# Construct the path to the itf_cooked directory
itf_cooked_dir = os.path.join(input_folder, "cache/itf_cooked")

# Traverse through itf_cooked subdirectories
for root, dirs, files in os.walk(itf_cooked_dir):
    for directory in dirs:
        maps_dir = os.path.join(itf_cooked_dir, directory, "world/maps")
        if os.path.exists(maps_dir):
            # Traverse through world/maps subdirectories
            for root, dirs, files in os.walk(maps_dir):
                for directory in dirs:
                    pictos_dir = os.path.join(maps_dir, directory, "timeline/pictos")
                    if os.path.exists(pictos_dir):
                        print(f"Checking pictos directory: {pictos_dir}")
                        copy_png_files(pictos_dir, output_folder)

print("Pictos collected and saved to the 'pictos' folder.")
