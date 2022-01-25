from pathlib import Path
import asyncio
import aiopath
from settings import MAIN_PATH, EXTENSIONS, FOLDERS_LIST


# Coroutine to create folders from list in given directory
async def create_folders(folders_list,main_path):
    for i in folders_list:
       await aiopath.AsyncPath(f'{main_path}\{i}').mkdir(exist_ok=True) #exist_ok = True  means, if such folder exists, no exception occurs


# Function to recursively get filenames from our directory
# (find folder - go inside it, search here, repeat)
# * I find no way to make it asyncronous, and there is no point in this
def get_file_names(main_path):
    p = Path(main_path).glob('**/*')     # glob(**/*) allows recursive search
    file_paths = [x for x in p if x.is_file()]
    return file_paths # [WindowsPath('B:/Sorting folder/lection 8.zip'),...]


async def sort_file(file_path,main_path):
        # separate filename
    file_name =  aiopath.AsyncPath(file_path).name # f_app_expense.sql
        # separate extension
    file_ext =  aiopath.AsyncPath(file_path).suffix[1:] #.sql ; [1:] = sql
    for ext  in EXTENSIONS.items():
        # Check extension in EXTENSIONS.items[1]
        if file_ext in ext[1]:
            print(f'{file_ext} in {ext[0]}')
        # If found - move to folder EXTENSIONS.items[0]
            new_file_path = aiopath.AsyncPath(f'{main_path}\{ext[0]}\{file_name}')
            file_path.rename(new_file_path)


async def delete_empty_folders(main_path):
    p = Path(main_path).glob('**/*')     # glob(**/*) allows recursive search
    all_folders = [x for x in p if x.is_dir() ]
    del_folders = []
    for path in all_folders:
        if next(path.iterdir(),None) == None: # in this way we find out, is folder empty
            print(f'{path} is empty, deleting')
            del_folders.append(path)
    for path in del_folders:
        path.rmdir()


async def main(folders_list,main_path):
    await create_folders(folders_list,main_path)
    file_names = get_file_names(main_path)
    for file in file_names:
        await sort_file(file,main_path )
    await delete_empty_folders(main_path)

asyncio.run(main(FOLDERS_LIST,MAIN_PATH))

