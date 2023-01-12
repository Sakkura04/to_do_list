from todolist.data.entrences import entrance_dict
from todolist.helpers.help import *
from datetime import date
import sqlite3

def create_str1():
    id1 = len(entrance_dict) + 1
    date1 = 1
    priority1 = -1

    title1 = input('enter title')
    description1 = input('enter description ')
    while not isinstance (priority1, (int)) or priority1 < 0:
        try:
            priority1 = int(input('enter priority '))
        except:
            print('try one more time')

    while not isinstance (date1, date):
        try:
            date1 = input('enter valid data in the format YYYY-MM-DD')
            date1 = date.fromisoformat(date1)
        except:
            print('try one more time')
    entrance_dict.append ({'title' : title1,'description' : description1,
                           'priority' : priority1,'date' : date1,
                           'done' : False})

def search_by(task):
    flag2 = 0
    search_str = input('enter name or part of it: ')
    for index in range(len(entrance_dict)):
        if(search_str in entrance_dict[index]['title']):
            if(task=='check'):
                print(entrance_dict[index])

            if(task=='done'):
                print(entrance_dict[index])
                print('Make this done?: ')
                flag=yes_or_no()
                if flag == True:
                    entrance_dict[index]['done'] = True
                    set_sq(index, 'done', True)

            if(task=='priority'):
                print(entrance_dict[index])
                print('Change priority of it?: ')
                flag=yes_or_no()
                if flag == True:
                    pr = int(input('enter priority: '))
                    entrance_dict[index]['priority'] = pr
                    set_sq(index, 'priority', pr)

            if(task=='delete'):
                print(entrance_dict[index])
                print('Delete it?: ')
                flag=yes_or_no()
                if flag == True:
                    entrance_dict.pop(index)
                    del_sq(index)
            flag2=1
    if flag2 == 0:
        print('Nothing alike:(')


def check(dict = entrance_dict):
    for index in range(0, len(dict)):
        print(dict[index]['title'])


def check_sorted():
    dicts = sorted(entrance_dict, key = lambda x : x.get('priority'))
    check(dicts)


def check_if_done(task):
    flag = 0
    for index in range(len(entrance_dict)):
        if(entrance_dict[index]['done'] == task):
            print(entrance_dict[index]['title'])
            flag = 1
    if flag == 0:
        print('Nothing alike:(')

def check_late():
    today = date.today()
    flag = 0
    for index in range(len(entrance_dict)):
        if(entrance_dict[index]['date'] < today):
            print(entrance_dict[index]['title'])
            flag = 1
    if flag == 0:
        print('Nothing alike:(')


def statistics():
    task_done = 0
    task_n_done = 0
    miss_task = 0
    today = date.today()
    amount = len(entrance_dict)
    for index in range(len(entrance_dict)):
        if(entrance_dict[index]['done']==True):
            task_done += 1
        else:
            task_n_done += 1

        if (entrance_dict[index]['date'] < today):
            miss_task += 1
    print('Amount of tasks', amount, '\nFinished: ', task_done, '\nUnfinished: ', task_n_done, '\nOverdue: ', miss_task)









