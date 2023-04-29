import os
from fuzzywuzzy import fuzz

# Path to the directories
first_directory = './yt'
second_directory = './gdrive'

# Get the list of files in both directories
first_files = os.listdir(first_directory)
second_files = os.listdir(second_directory)

# Set the similarity threshold for renaming files
similarity_threshold = 70

# Function to remove "Eurobeat Remix" from the filename
def clean_filename(filename):
    # add your own filters
    return filename # Here is what i used - .lower().replace("eurobeat remix", "").replace("turbo - ", "").strip()

# Create sets to store matched and unmatched filenames
matched_files = set()
unmatched_first_files = set(first_files)
unmatched_second_files = set(second_files)

# Iterate over the files in the second directory
for second_file in second_files:
    # Remove "Eurobeat Remix" from the second filename
    second_file_cleaned = clean_filename(second_file)

    # Initialize the best match and its similarity score
    best_match = None
    best_similarity = 0

    # Iterate over the files in the first directory
    for first_file in first_files:
        # Remove "Eurobeat Remix" from the first filename
        first_file_cleaned = clean_filename(first_file)

        # Calculate the similarity score between the two cleaned filenames
        similarity = fuzz.ratio(first_file_cleaned, second_file_cleaned)

        # Update the best match if the current similarity is higher
        if similarity > best_similarity and similarity >= similarity_threshold:
            best_similarity = similarity
            best_match = first_file

    # Rename the file in the second directory if a suitable match was found
    if best_match is not None:
        matched_files.add(best_match)
        unmatched_second_files.remove(second_file)
        unmatched_first_files.discard(best_match)

        old_file_path = os.path.join(second_directory, second_file)
        new_file_path = os.path.join(second_directory, best_match)

        # Check if the new file name already exists
        if os.path.exists(new_file_path):
            print(f'Skipped renaming {second_file} because {best_match} already exists.')
        else:
            os.rename(old_file_path, new_file_path)
            print(f'Renamed {second_file} to {best_match}')
    else:
        print(f'No suitable match found for {second_file}')

# Print unmatched files from the first directory
print("Unmatched files in the first directory:")
for unmatched_file in unmatched_first_files:
    print(unmatched_file)

# Print unmatched files from the second directory
print("Unmatched files in the second directory:")
for unmatched_file in unmatched_second_files:
    print(unmatched_file)