import os
import shutil


#FILE CATEGORIES

File_cat = {
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".pdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
    "Music": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "Code": [".py", ".html", ".css", ".js", ".c", ".java", ".cpp", ".php"]

}

# GETS THE FILES I

def get_target_dir():
    target_dir = input("Enter the full path to the directory: ")
    if not os.path.isdir(target_dir):
        print(f"Error: The path {target_dir} is not valid")
        exit(1) #EXIT IF THE DIRECTORY IS NOT VALID
    return target_dir

    
# GETS THE CATEGORY FOR A FILE BEASED ON EXTENSION

def get_file_cat(fileName):
    file_exst = os.path.splitext(fileName)[1].lower()
    for category, extension in File_cat.items(): #dbT File_cat.items()
        if file_exst in extension:
            return category
    return "Others"
    

# directory = get_target_dir()


def org_folder(path):

    for item in os.listdir(path):
        item_path = os.path.join(path, item)


        # PROCESS ONLY FILES

        if os.path.isfile(item_path):
            # print(f"Found: {item}")
            category = get_file_cat(item)
            dest_folder = os.path.join(path, category)

            # CREATE 'CATEGORY' FOLDER IF DOESN'T EXIST

            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
                print(f"Created folder: {dest_folder}")



            # CREATES NEW FILE PATH AND MOVES THE FILE 

            dest_path = os.path.join(dest_folder, item)
            shutil.move(item_path, dest_path)
            print(f"Moved {item}, to {category} 'Folder'")




# TESTING

# print(get_file_cat("example.jpg"))
# print(get_file_cat("document.pdf"))
# print(get_file_cat("archive.xyz"))


if __name__ == "__main__":
    directory = get_target_dir()
    org_folder(directory)
    print("FILE ORGANIZATION COMPLETE")