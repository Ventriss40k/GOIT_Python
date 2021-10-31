from concurrent.futures import ThreadPoolExecutor
import os
from time import time


main_path = 'b:\\random folder' # название директории для сканирования

# Это список расширений. Ключи будут использоваться для создания папок.
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

# создает папки с именами из списка или словаря. В данном случае - словаря.
def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'): # двойной слеш для экранирования
            os.mkdir(f'{folder_path}\\{folder}')

# получает список путей папок в директории 
def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()] 

    return subfolder_paths

# получает список путей файлов (рекурсивно)
def recurs_get_file_paths(folder_path) -> list: # Функция возвращает пути к файлам в директории. Когда встречает папку , рекурсивно заходит в нее.
    result =[]
    final_result=[]
    for f in os.scandir(folder_path):
        if not f.is_dir():
            result.append(f.path)
        elif f.is_dir:
            result.append(recurs_get_file_paths(f.path))
    for r in result: # делает из вложенных списков 1 список
        def recurs_single_list(r):
            if type(r) is str:
                final_result.append(r)
            elif type(r) is list:
                for i in r:
                    recurs_single_list(i)
        recurs_single_list(r)

    return final_result # возвращает список с путями файлов

def sort_files(folder_path):
    file_paths = recurs_get_file_paths(folder_path)
    ext_list = list(extensions.items())
# для каждого пути файла - сортировка используя несколько потоков
    def sort_file_tread(file_path):
        extension = file_path.split('.')[-1] # отделяем расширение от пути к файлу
        file_name = file_path.split('\\')[-1] # отделяем название файла от пути к файлу

        for dict_key_int in range(len(ext_list)): # проходимся по ключам словаря расширений
            if extension in ext_list[dict_key_int][1]: # если расширение (отделенное от файла) есть в словаре расширений
                print(f'Moving {file_name} in {ext_list[dict_key_int][0]} folder\n') 
                os.rename(file_path, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}') # перемещаем файл по новому пути, используя функцию переименования
    with ThreadPoolExecutor(2) as pool:
        pool.map(sort_file_tread,file_paths)


def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)

    for p in subfolder_paths: # итерируемся по путям папок
        if not os.listdir(p): # находим пустые папки
            print('Deleting empty folder:', p.split('\\')[-1], '\n')
            os.rmdir(p) # удаление папки р 


if __name__ == "__main__":
    start_time = time()
    create_folders_from_list(main_path, extensions)
    sort_files(main_path)
    remove_empty_folders(main_path)
    finish_time = time()-start_time
    print(finish_time)


