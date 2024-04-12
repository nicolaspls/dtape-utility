import os
import shutil

# Read moves from moves.txt
with open('moves.txt', 'r') as file:
    moves = file.read().splitlines()

# Prompt the user to input the folder path
input_folder = input("Enter the path to your cache folder: ")
print(f"Input folder path: {input_folder}")

# Construct the path to the output folder
output_folder = os.path.join(os.path.dirname(__file__), "moves")
print(f"Output folder: {output_folder}")

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print("Output folder created.")

# Function to copy msm files
def copy_msm_files(source_dir, destination_dir):
    for file in os.listdir(source_dir):
        if file.endswith(".msm") and file[:-4] in moves:
            shutil.copy(os.path.join(source_dir, file), destination_dir)
            print(f"File {file} copied to output folder.")

# Construct the path to the moves directory
maps_dir = os.path.join(input_folder, "world/maps")

# Traverse through world/maps subdirectories
for root, dirs, files in os.walk(maps_dir):
    for directory in dirs:
        wiiu_dir = os.path.join(maps_dir, directory, "timeline/moves/wiiu")
        if os.path.exists(wiiu_dir):
            print(f"Checking wiiu directory: {wiiu_dir}")
            copy_msm_files(wiiu_dir, output_folder)

print("Moves collected and saved to the 'moves' folder.")
