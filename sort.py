import json
import os
import glob
import shutil

# i fucked up the files 5 times
# Input and output folder paths
input_folder = 'input'
output_folder = 'output'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Find input files ending with tml_dance.dtape.ckd in the input folder
input_files = glob.glob(os.path.join(input_folder, '*_tml_dance.dtape.ckd'))

if not input_files:
    print("Error: No input file found.")
    exit()

# Read each input file
for input_file in input_files:
    # Load the JSON data from file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Extract the 'Clips' list from the data
    clips = data.get('Clips', [])

    # Separate PictogramClips and MotionClips
    pictogram_clips = []
    motion_clips = []
    for clip in clips:
        if clip['__class'] == 'PictogramClip':
            pictogram_clips.append(clip)
        elif clip['__class'] == 'MotionClip':
            motion_clips.append(clip)

    # Sort PictogramClips and MotionClips by their StartTime
    sorted_pictogram_clips = sorted(pictogram_clips, key=lambda x: x.get('StartTime', 0))
    sorted_motion_clips = sorted(motion_clips, key=lambda x: x.get('StartTime', 0))

    # Combine sorted clips and MotionPlatformSpecifics
    sorted_data = {
        "__class": data["__class"],
        "Clips": sorted_pictogram_clips + sorted_motion_clips,
        "TapeClock": data["TapeClock"],
        "TapeBarCount": data["TapeBarCount"],
        "FreeResourcesAfterPlay": data["FreeResourcesAfterPlay"],
        "MapName": data["MapName"],
        "SoundwichEvent": data["SoundwichEvent"]
    }

    # Get the map name from the MapName idk
    map_name = data["MapName"]

    # Output file path with the same name as the MapName in the output folder maybe
    output_file = os.path.join(output_folder, f"{map_name}.json")

    # Write the sorted dtapes to the output files
    with open(output_file, 'w') as f:
        json.dump(sorted_data, f, indent=2)

    print(f"Output file '{output_file}' created successfully.")

print("All dtapes are sorted and saved in the output folder.")
