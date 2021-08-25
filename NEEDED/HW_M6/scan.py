import sys
from pathlib import Path


IMAGES = []
AUDIO = []
VIDEO = []
DOCUMENTS = []
OTHER = []
FOLDERS = []
ARCHIVES = []
UNKNOW = set()
EXTENSIONS = set()

REGISTERED_EXTENSIONS = {
    'JPEG': IMAGES,
    'PNG': IMAGES,
    'JPG': IMAGES,
    'SVG': IMAGES,
    'AVI': VIDEO,
    'MP4': VIDEO,
    'MOV': VIDEO,
    'MKV': VIDEO,
    'DOC': DOCUMENTS,
    'DOCX': DOCUMENTS,
    'TXT': DOCUMENTS,
    'PDF': DOCUMENTS,
    'XLSX': DOCUMENTS,
    'PPTX': DOCUMENTS,
    'MP3': AUDIO,
    'OGG': AUDIO,
    'WAV': AUDIO,
    'AMR': AUDIO,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES,
}


def get_extensions(file_name) -> str:
    return Path(file_name).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('Images', 'Audio', 'Video', 'Documents', 'Archives'):
                FOLDERS.append(item)
                scan(item)
            continue
        extension = get_extensions(item.name)
        new_name = folder / item.name
        if not extension:
            OTHER.append(new_name)
        else:
            try:
                current_container = REGISTERED_EXTENSIONS[extension]
                EXTENSIONS.add(extension)
                current_container.append(new_name)
            except KeyError:
                UNKNOW.add(extension)
                OTHER.append(new_name)


if __name__ == '__main__':
    scan_path = sys.argv[1]

    search_folder = Path(scan_path)
    scan(search_folder)
