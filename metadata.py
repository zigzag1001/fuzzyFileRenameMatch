import os
from shutil import copyfile
from mutagen.id3 import ID3, APIC

def copy_metadata_and_cover(source_file, target_file, output_directory):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Copy the target file to the output directory if it exists, otherwise copy the source file
    if os.path.exists(target_file):
        output_file = os.path.join(output_directory, os.path.basename(target_file))
        copyfile(target_file, output_file)
    else:
        output_file = os.path.join(output_directory, os.path.basename(source_file))
        copyfile(source_file, output_file)

    # Load the source file's metadata
    source_metadata = ID3(source_file)

    # Load the target file's metadata if it exists, otherwise create a new ID3 object
    if os.path.exists(output_file):
        target_metadata = ID3(output_file)
    else:
        target_metadata = ID3()

    # Copy the metadata from the source file to the target file
    for key in source_metadata.keys():
        if key == 'APIC:':
            # Copy the cover art
            target_metadata[key] = APIC(
                encoding=source_metadata[key].encoding,
                mime=source_metadata[key].mime,
                type=source_metadata[key].type,
                desc=source_metadata[key].desc,
                data=source_metadata[key].data
            )
        else:
            # Copy other metadata
            target_metadata[key] = source_metadata[key]

    # Save the changes to the target file
    target_metadata.save(output_file)

    print("Metadata and cover art copied successfully!")

# Example usage
source_directory = "./yt" # Where the metadata is
target_directory = "./gdrive" # Where the audio quality is
output_directory = "./out" # Combined output + files from source that didnt have a match

# Get the list of MP3 files in the source directory
source_files = [file for file in os.listdir(source_directory) if file.endswith(".mp3")]

for file in source_files:
    # Construct the corresponding target and source file paths
    source_file = os.path.join(source_directory, file)
    target_file = os.path.join(target_directory, file)

    print(f"Source file: {source_file}")
    print(f"Target file: {target_file}")

    # Copy metadata and cover art from the source file to the target file
    copy_metadata_and_cover(source_file, target_file, output_directory)
