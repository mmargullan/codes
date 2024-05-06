import os
import shutil

#C:\Users\begzh\Downloads my downloads folder 

def create_sub(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path


def clean_folder(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split('.')[-1].lower()
            if file_extension:
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_sub(folder_path, subfolder_name)
                file_path = os.path.join(folder_path, filename)
                new_location = os.path.join(subfolder_name, filename)
                if not os.path.exists(new_location):
                    shutil.move(file_path, subfolder_path)
                else:
                    print("Skipped")


folder_path = r'C:\Users\begzh\Downloads'
if os.path.isdir(folder_path):
    clean_folder(folder_path)
    print("Cleaning complete")
else:
    print("Wrong folder path")