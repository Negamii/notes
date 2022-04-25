from datetime import datetime
import json


class style:
    RESET = '\033[0m'
    BRIGHT = '\033[1m'
    DIM = '\033[2m'
    ITALICS = '\033[3m'
    LINED = '\033[4m'


def start():
    print('1.Добавить заметку', '2.Удалить заметку',
          '3.Редактировать заметки', '4.Просмотреть заметки', '5.Поиск', '6.Выход', sep='\n')
    temp = int(input('Введите цифру: '))
    match temp:
        case 1:
            return add_notes()
        case 2:
            return del_notes()
        case 3:
            return edit_notes()
        case 4:
            return view_notes()
        case 5:
            return search()
    return 0


def add_notes():
    note = file_read()
    text_name = input('Название: ')
    text = input('Текст: ')
    print('Изменить стиль?', '1.Да', '2.Нет', sep='\n')
    if int(input()) == 1:
        text_name, text = edit_font(text_name, text)
    j_note = {
        'name': text_name,
        'txt': text,
        'date': time_notes()
    }
    note.append(j_note)
    file_write(note)
    return start()


def del_notes():
    list_notes = file_read()
    print_notes(list_notes)
    temp = int(input('Выберите заметку: '))
    if temp > len(list_notes):
        print('Такой заметки не существует\n')
        return del_notes()
    del list_notes[temp - 1]
    print_notes(list_notes)
    file_write(list_notes)
    return start()


def view_notes():
    list_notes = file_read()
    print_notes(list_notes)
    return start()


def edit_notes():
    list_notes = file_read()
    print_notes(list_notes)
    print('Выберите заметку:')
    try:
        temp = int(input())
        print('Название:', list_notes[temp - 1]['name'])
        print('Текст:', list_notes[temp - 1]['txt'])
    except:
        print('Такой заметки не существует\n')
        return edit_notes()
    print('1.Изменить название', '2.Изменить текст', '3.Изменить название и текст', '4.Изменить стиль текста',
          '5.Выйти', sep='\n')
    edit = int(input('Введите цифру: '))
    match edit:
        case 1:
            print('Введите новое название:')
            list_notes[temp - 1]['name'] = input()
            list_notes[temp - 1]['date'] = time_notes()
        case 2:
            print('Введите новый текст:')
            list_notes[temp - 1]['txt'] = input()
            list_notes[temp - 1]['date'] = time_notes()
        case 3:
            print('Введите новое название:')
            list_notes[temp - 1]['name'] = input()
            print('Введите новый текст:')
            list_notes[temp - 1]['txt'] = input()
            list_notes[temp - 1]['date'] = time_notes()
        case 4:
            list_notes[temp - 1]['name'], list_notes[temp - 1]['txt'] = edit_font(
                list_notes[temp - 1]['name'], list_notes[temp - 1]['txt']
            )
            list_notes[temp - 1]['date'] = time_notes()
    file_write(list_notes)
    return start()


def file_read():
    with open('txt_notes.json') as f:
        return json.load(f)


def file_write(notes):
    with open('txt_notes.json', 'w') as wr:
        json.dump(notes, wr, indent=4)


def print_notes(notes):
    print(
        *[str(i + 1) + '.' + notes[i]["name"] + '\n' + notes[i]["txt"] + '\n' + notes[i]["date"]
          + '\n' for i in range(len(notes))], sep='\n'
    )


def time_notes():
    return datetime.today().strftime("Изменено %d/%m/%Y в %H:%M")


def edit_font(name_note, text_note):
    print('1.Изменить стиль названия', '2.Изменить стиль текста', '3.Изменить стиль названия и текста',
          '4.Ничего не изменять', sep='\n')
    temp_font = int(input('Введите цифру: '))
    match temp_font:
        case 1:
            name_note = text_style(name_note)
        case 2:
            text_note = text_style(text_note)
        case 3:
            name_note = text_style(name_note)
            text_note = text_style(text_note)
    return name_note, text_note


def text_style(txt):
    style_txt = style()
    print('1.Изменить стиль на курсив', '2.Изменить стиль на жирный', '3.Изменить стиль на блеклый',
          '4.Изменить стиль на подчеркнутый', '5.Изменить стиль на стандартный', sep='\n')
    number = int(input('Введите цифру: '))
    match number:
        case 1:
            txt = style_txt.ITALICS + txt + style_txt.RESET
        case 2:
            txt = style_txt.BRIGHT + txt + style_txt.RESET
        case 3:
            txt = style_txt.DIM + txt + style_txt.RESET
        case 4:
            txt = style_txt.LINED + txt + style_txt.RESET
        case 5:
            txt = del_style(txt)
    return txt


def del_style(t):
    style_txt = style()
    t = t.replace(style_txt.LINED, '')
    t = t.replace(style_txt.DIM, '')
    t = t.replace(style_txt.BRIGHT, '')
    t = t.replace(style_txt.ITALICS, '')
    return t


def search():
    list_notes = file_read()
    word_note = input('Введите слово: ')
    print('Найдено:')
    for now in range(len(list_notes)):
        if word_note in list_notes[now]['name'] or word_note in list_notes[now]["txt"]:
            print(str(now + 1) + '.' + list_notes[now]["name"], list_notes[now]["txt"], list_notes[now]["date"],
                  sep='\n')
    print()
    return start()


start()
