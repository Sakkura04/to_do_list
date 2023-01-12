from todolist.data.entrences import entrance_dict
from todolist.data.entrences import param_list
from datetime import date
from datetime import datetime
import sqlite3
import json
import os


def yes_or_no():
    d='t'
    while d != 'y' and d != 'n':
        d = input('enter y(yes) ot n(not)').lower()
        if (d == 'y'):
            return True
        if (d == 'n'):
            return False


def print_menu():
    print('Створити новий запис -1\nЗнайти справу та переглянути її деталі -2')
    print('Знайти та помітити справу, як виконану -3\nЗнайти справу та змінити її пріоритет -4\nЗайти та видалити справу -5')
    print('Переглянути дісні справи за їх додавання -6')
    print('Переглянути дісні справи за пріоритетом -7\nПереглянути всі невиконані справи -8')
    print('Переглянути виконані справи -9\nПереглянути прострочені справи -10')
    print('Переглянути статистику -11')
    print('Очистити екран -12\nвийти -13')


def from_json():
    cwd = os.getcwd()
    file_path = os.path.join(cwd, 'data', 'save.json')
    try:
        file1 = open(file_path, 'r')
    except FileNotFoundError:
        print('the list is empty')
    else:
        entrance_dict = json.load(file1)


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')
    # print out some text


def check_type(type, text):
    obj = type(input(text))
    while not isinstance (obj, type):
        obj = input(text)
    return obj

def print_from_sq():
    con = sqlite3.connect('Tasks.db')
    cur = con.cursor()

    for value in cur.execute('''SELECT * FROM tasks'''):
        index = 0
        for ind in value:
            if index == 0:
                print('id:', ind, '  title:', end=' ')
            elif index == 2:
                print('description: ', ind, '\npriority: ', end=' ')
            elif index == 4:
                print('finish date: ', date.fromtimestamp(ind), ' is', end = ' ')
            elif ind == 0:
                print('Undone')
            elif ind == 1:
                print('Done')
            else:
                print(ind)
            index += 1

def from_sq():
    con = sqlite3.connect('Tasks.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS tasks(ind BIGINT, title TEXT, description TEXT, 
                                               priority BIGINT, date BIGINT , done BIGINT) """)
    con.commit()

    index = 0
    for value in cur.execute('''SELECT * FROM tasks'''):
        entrance_dict.append({})
        for count, values in enumerate(value):
            if count == 4:
                entrance_dict[index][param_list[count]] = date.fromtimestamp(values)
            else:
                entrance_dict[index][param_list[count]] = values
        index += 1


def to_sq(index):
    con = sqlite3.connect('Tasks.db')
    cur = con.cursor()
    dat = entrance_dict[index]['date']
    my_datetime = datetime(dat.year, dat.month, dat.day)
    dat = datetime.timestamp(my_datetime)
    print(type(dat), '  ', dat)
    cur.execute(f"INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?)", (index, entrance_dict[index]['title'],
                                     entrance_dict[index]['description'], entrance_dict[index]['priority'],
                                     dat, entrance_dict[index]['done']))
    con.commit()


def set_sq(index, param, value):
    con = sqlite3.connect('Tasks.db')
    cur = con.cursor()
    cur.execute(f"UPDATE tasks SET {param} = {value} WHERE ind = '{index}' ")
    con.commit()

def del_sq(index):
    con = sqlite3.connect('Tasks.db')
    cur = con.cursor()
    cur.execute(f"DELETE tasks WHERE ind = '{index}' ")
    con.commit()