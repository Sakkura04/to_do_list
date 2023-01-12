from source.create import *
# from data.entrences import entrance_dict
from helpers.help import *
import json
import os

if __name__ == '__main__':
    from_sq()
    # print_from_sq()
    print_menu()
    while True:
        menu = check_type(int, 'choose your function(saw the menu - 0): ')
        if menu == 0:
             print_menu()
        elif menu == 1:
            create_str1()
            to_sq(len(entrance_dict)-1)
        elif menu == 2:
            search_by('check')
        elif menu == 3:
            search_by('done')
        elif menu == 4:
            search_by('priority')
        elif menu == 5:
            search_by('delete')
        elif menu == 6:
            check()
        elif menu == 7:
            check_sorted()
        elif menu == 8:
            check_if_done(False)
        elif menu == 9:
            check_if_done(True)
        elif menu == 10:
            check_late()
        elif menu == 11:
            statistics()
        elif menu == 12:
            screen_clear()
        elif menu == 13:
            print('Chao pitches')
            exit()
