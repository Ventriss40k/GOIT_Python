from concurrent.futures import ThreadPoolExecutor
import os
from time import time
from settings import MAIN_PATH, EXTENSIONS, EXT_LIST

# Function to create folders from "EXTENSIONS" dictionary
# Check on existence of such folder included
def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')


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


# This func is for sorting files. Made to be used inside threads
def sort_file_thread(file_path):
    extension = file_path.split('.')[-1] # split extension from file path
    file_name = file_path.split('\\')[-1] # split filename from file path

    for ext_list_num in range(len(EXT_LIST)): # iterate throuth extension list
        if extension in EXT_LIST[ext_list_num][1]: # check if extension is present in extension list
            print(f'Moving {file_name} in {EXT_LIST[ext_list_num][0]} folder\n') 
            os.rename(file_path, f'{MAIN_PATH}\\{EXT_LIST[ext_list_num][0]}\\{file_name}') # by renaming file path, we actualy move it to new folder
# example of ext_list_num:
# ('data', ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav', 'tar', 'xml'),
# ext_list_num[0] is filetype ( audio, text, 3d etc.)
# ext_list_num[1] is extension (txt, sql, bin, png etc)


# Func to run dedicated sort_file_thread func inside threads
def run_file_sorting_threads():
    file_paths = recurs_get_file_paths(MAIN_PATH)
    # Running treads with sort_file_thread func
    with ThreadPoolExecutor(2) as pool:
        pool.map(sort_file_thread, file_paths)


# Function to get subfolders path (of 1st level nesting)
def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()] 
    return subfolder_paths

# Func to remove empty folders
def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)

    for p in subfolder_paths:
        if not os.listdir(p): 
            print('Deleting empty folder:', p.split('\\')[-1], '\n')
            os.rmdir(p) 


if __name__ == "__main__":
    start_time = time()
    create_folders_from_list(MAIN_PATH, EXTENSIONS)
    run_file_sorting_threads()
    remove_empty_folders(MAIN_PATH)
    finish_time = time()-start_time
    print(finish_time)


