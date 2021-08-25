import os
import shutil
import re
import sys


def moove(path):
    extension = (['.avi', '.mp4', '.mov', '.mkv'],
                 ['.svg', '.jpeg', '.png', '.jpg'],
                 ['.doc', '.docx', '.txt', '.pdf', '.xls'],
                 ['.mp3', '.ogg', '.wav', '.wma'],
                 ['.zip', '.gz', '.tar']
                 )

    for i in os.listdir(path):
        ignore_dir = ('Video', 'Images',  'Documents', 'Music', 'Archives')

        if os.path.isdir(path + '/' + i):
            if i not in ignore_dir:
                moove(path + '/' + i)
            else:
                continue

        elif os.path.isfile(path + '/' + i):
            file = os.path.basename(i)
            file_name = normalize(os.path.splitext(file)[0])
            file_end = os.path.splitext(file)[1]

            if file_end.lower() in extension[0]:
                os.replace(str(path) + '\\' + i,
                           f'D:\\Python\\Test\\trash\\Video\\{file_name+file_end}')
            elif file_end.lower() in extension[1]:
                os.replace(str(path) + '\\' + i,
                           f'D:\\Python\\Test\\trash\\Images\\{file_name+file_end}')
            elif file_end.lower() in extension[2]:
                os.replace(str(path) + '\\' + i,
                           f'D:\\Python\\Test\\trash\\Documents\\{file_name+file_end}')
            elif file_end.lower() in extension[3]:
                os.replace(str(path) + '\\' + i,
                           f'D:\\Python\\Test\\trash\\Music\\{file_name+file_end}')
            elif file_end.lower() in extension[4]:
                shutil.unpack_archive(str(path) + '\\' + i,
                                      f'D:\\Python\\Test\\trash\\Archives\\{file_name}')
                os.remove(str(path) + '\\' + i)


def normalize(text):

    table = {ord('а'): 'a', ord('б'): 'b', ord(
        'в'): 'v', ord('г'): 'h', ord('ґ'): 'g',
        ord('д'): 'd', ord('е'): 'e', ord('є'): 'ie',
        ord('ж'): 'zh', ord('з'): 'z', ord('и'): 'y',
        ord('і'): 'i', ord('ї'): 'i', ord('й'): 'i',
        ord('к'): 'k', ord('л'): 'l', ord('м'): 'm',
        ord('н'): 'n', ord('о'): 'o', ord('п'): 'p',
        ord('р'): 'r', ord('с'): 's', ord('т'): 't',
        ord('у'): 'u', ord('ф'): 'f', ord('х'): 'kh',
        ord('ц'): 'ts', ord('ч'): 'ch', ord('ш'): 'sh',
        ord('щ'): 'shch', ord('ю'): 'iu', ord('я'): 'ia',
        ord('А'): 'A', ord('Б'): 'B', ord(
        'В'): 'V', ord('Г'): 'H', ord('Ґ'): 'G',
        ord('Д'): 'D', ord('Е'): 'E', ord('Є'): 'Ye',
        ord('Ж'): 'Zh', ord('З'): 'Z', ord('И'): 'Y',
        ord('І'): 'I', ord('Ї'): 'Yi', ord('Й'): 'Y',
        ord('К'): 'K', ord('Л'): 'L', ord('М'): 'M',
        ord('Н'): 'N', ord('О'): 'O', ord('П'): 'P',
        ord('Р'): 'R', ord('С'): 'S', ord('Т'): 'T',
        ord('У'): 'U', ord('Ф'): 'F', ord('Х'): 'Kh',
        ord('Ц'): 'Ts', ord('Ч'): 'Ch', ord('Ш'): 'Sh',
        ord('Щ'): 'Shch', ord('Ю'): 'Yu', ord('Я'): 'Ya',
        ord('ь'): '', ord('’'): ''}

    text = text.translate(table)
    clean_text = re.sub(r'[^\w]', '_', text)
    text = clean_text
    return text


def main():
    path = sys.argv[1]
    print(f"Start in {path}")

    moove(path)


if __name__ == '__main__':

    main()
