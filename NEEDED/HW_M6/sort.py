from pathlib import Path
import scan
from Normalize import normalize
import shutil
import sys


def moov_image(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(target_folder / new_name)


def moov_audio(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(target_folder / new_name)


def moov_video(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(target_folder / new_name)


def moov_documents(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(target_folder / new_name)


def moov_other(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(target_folder / new_name)


def moov_archive(file, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, ''))
    archive_folder = target_folder / new_name
    archive_folder.mkdir(exist_ok=True)
    try:
        shutil.unpack_archive(str(file.resolve()),
                              str(archive_folder.resolve()))
    except shutil.ReadError:
        archive_folder.rmdir()
        return
    file.unlink()


def deleate_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        pass


def main(folder):
    folder = Path('D:\Python\Test\\trash')
    scan.scan(folder)

    for file in scan.IMAGES:
        moov_image(file, folder, 'Images')

    for file in scan.AUDIO:
        moov_audio(file, folder, 'Audio')

    for file in scan.VIDEO:
        moov_video(file, folder, 'Video')

    for file in scan.DOCUMENTS:
        moov_documents(file, folder, 'Documents')

    for file in scan.OTHER:
        moov_other(file, folder, 'Other')

    for file in scan.ARCHIVES:
        moov_archive(file, folder, 'Archives')

    for f in scan.FOLDERS:
        deleate_folder(f)


if __name__ == '__main__':
    scan_path = sys.argv[1]
    sort_folder = Path(scan_path)
    main(sort_folder.resolve())
