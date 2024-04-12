# file created by nic
import os
import json

def extract_moves_and_pictos(input_data):
    moves = set()
    pictos = set()
    for clip in input_data["Clips"]:
        if "__class" in clip:
            if clip["__class"] == "MotionClip" and "ClassifierPath" in clip:
                classifier_path = clip["ClassifierPath"]
                _, filename = os.path.split(classifier_path)
                if filename.endswith(".msm"):
                    moves.add(filename[:-4])  # Removing the .msm extension
            elif clip["__class"] == "PictogramClip" and "PictoPath" in clip:
                picto_path = clip["PictoPath"]
                _, filename = os.path.split(picto_path)
                if filename.endswith(".png"):
                    pictos.add(filename[:-4])  # Removing the .png extension
    return moves, pictos

def list_moves(moves):
    unique_moves = set(moves)
    output_filename = "moves.txt"
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = os.path.join(output_dir, output_filename)
    with open(output_path, "w") as f:
        for move in unique_moves:
            f.write(move + "\n")

def list_pictos(pictos):
    unique_pictos = set(pictos)
    output_filename = "pictos.txt"
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = os.path.join(output_dir, output_filename)
    with open(output_path, "w") as f:
        for picto in unique_pictos:
            f.write(picto + "\n")

def main():
    print("Welcome to Moves and Pictos Lister by Nic")

    # Find input files ending with tml_dance.dtape.ckd in the input folder
    input_folder = "input"
    input_files = [f for f in os.listdir(input_folder) if f.endswith("tml_dance.dtape.ckd")]

    # Process each input file
    for input_file in input_files:
        with open(os.path.join(input_folder, input_file)) as f:
            data = json.load(f)

        # Extract moves and pictos based on user's choice
        moves, pictos = extract_moves_and_pictos(data)

        # Ask user what they want to list
        print("What would you like to do?")
        print("1. List moves")
        print("2. List pictos")
        option = input("Enter the number of your choice: ")

        if option == "1":
            list_moves(moves)
        elif option == "2":
            list_pictos(pictos)
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
# file created by nic
