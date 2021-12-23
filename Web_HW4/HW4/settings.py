#This is path, where program will be executed
MAIN_PATH = 'B:\\Sorting folder' 

#This is extensions dictionary. 
#Keys are names of folders and values - extension of files in these folders
EXTENSIONS = { 

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
# This is conversion of extension dict into list which looks like: [(key1,[val1,val2,val3]),(key2,[val3,val4,val5])]
# Will be used later in sort_file_thread func
EXT_LIST = list(EXTENSIONS.items())

# print(EXT_LIST)