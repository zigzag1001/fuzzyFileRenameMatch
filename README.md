# fuzzyFileRenameMatch
fuzzy search matches files from two directories, renames the files in the second to the closest matching ones from the first

![renaming files](https://user-images.githubusercontent.com/72932714/235324454-69c8402c-4229-46ba-91c0-6367209b5761.png)

+ move metadata from first directory to second. (if for example first directory has metadata, but second directory has higher audio quality)

![image](https://user-images.githubusercontent.com/72932714/235324554-809e5ed5-f4ea-44bf-ba20-cd80277d72e0.png)


## Use
Never intended to use again so not user friendly

pip install fuzzywuzzy

Youre going to need to edit the .py files with your directory names

Also probably standardize the filenames through the clean_filename() function to help with fuzzyrenaming

This only cleans the filenames when fuzzy matching and dosent affect anything else
