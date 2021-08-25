import re


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


def normalize(text):

    text = text.translate(table)
    clean_text = re.sub(r'[^\w\s]', '_', text)
    text = clean_text
    return text
