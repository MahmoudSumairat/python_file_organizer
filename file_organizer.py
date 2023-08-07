import os

files_list = os.listdir('./files')
folders = [];

# to get the language of the file by splitting the filename and getting the first element
def get_file_lang(filename):
    return filename.split('-')[0]

# to loop through the files and push the language of the file to the folders array if it doesn't exist
def populate_folders():
    for filename in files_list:
        file_lang = get_file_lang(filename)
        if file_lang not in folders:
            folders.append(file_lang)

# to create the language folders based on the folders array
def create_folders():
    for folder in folders:
        os.mkdir('./files/' + folder)


# to move the files to the language folders and categorize them
def move_files_lang_folders():
    for filename in files_list:
        file_lang = get_file_lang(filename)
        os.rename('./files/' + filename, './files/' + file_lang + '/' + filename)



# run the organizer in action
populate_folders()
create_folders()
move_files_lang_folders()