from concurrent.futures import ThreadPoolExecutor
import os
from time import time

#This is path, where program will be executed
main_path = 'b:\\random folder' 

#This is extensions dictionary. 
#Keys are names of folders and values - extension of files in these folders
extensions = { 

    'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 'h264', 'flv',
              'rm', 'swf', 'vob'],

    'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav', 'tar', 'xml'],

    'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl', 'cda'],

    'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 'tiff'],

    'archive': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb'],

    'text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],

    '3d': ['stl', 'obj', 'fbx', 'dae', '3ds', 'iges', 'step'],

    'presentation': ['pptx', 'ppt', 'pps', 'key', 'odp'],

    'spreadsheet': ['xlsx', 'xls', 'xlsm', 'ods'],

    'font': ['otf', 'ttf', 'fon', 'fnt'],

    'gif': ['gif'],

    'exe': ['exe'],

    'bat': ['bat'],

    'apk': ['apk']
}

# Function to create folders from "extensions" dictionary
# Check on existance of such folder included
def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')

# Function to get subfolders path (of 1st level nesting)
def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()] 

    return subfolder_paths

# Function to recursively check directory for files, diving inside every folder
# Returns list of paths to files
def recurs_get_file_paths(folder_path) -> list: # Функция возвращает пути к файлам в директории. Когда встречает папку , рекурсивно заходит в нее.
    result =[]
    final_result=[]
    for f in os.scandir(folder_path):
        if not f.is_dir():
            result.append(f.path)
        elif f.is_dir:
            result.append(recurs_get_file_paths(f.path))
    # This makes flat list of unflat list
    for r in result: 
        def recurs_single_list(r):
            if type(r) is str:
                final_result.append(r)
            elif type(r) is list:
                for i in r:
                    recurs_single_list(i)
        recurs_single_list(r)

    return final_result 

# This is main func for sorting files
def sort_files(folder_path):
    file_paths = recurs_get_file_paths(folder_path)
    ext_list = list(extensions.items())
    # This is child func to sort_files, made to execute inside tread
    def sort_file_tread(file_path):
        extension = file_path.split('.')[-1] # split extension from file path
        file_name = file_path.split('\\')[-1] # split filename from file path

        for dict_key_int in range(len(ext_list)): # iterate throuth extension dict
            if extension in ext_list[dict_key_int][1]: # check if extension is present in extension dict
                print(f'Moving {file_name} in {ext_list[dict_key_int][0]} folder\n') 
                os.rename(file_path, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}') # by renaming file path, we actualy move it to new folder
# Running treads with sort_file_tread func
    with ThreadPoolExecutor(2) as pool:
        pool.map(sort_file_tread,file_paths)

# Func to remove empty folders
def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)

    for p in subfolder_paths:
        if not os.listdir(p): 
            print('Deleting empty folder:', p.split('\\')[-1], '\n')
            os.rmdir(p) 


if __name__ == "__main__":
    start_time = time()
    create_folders_from_list(main_path, extensions)
    sort_files(main_path)
    remove_empty_folders(main_path)
    finish_time = time()-start_time
    print(finish_time)


