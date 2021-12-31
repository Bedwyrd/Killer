# This is a sample Python script.

# The Github stuff was done as per
# https://medium.com/analytics-vidhya/how-to-share-the-pycharm-project-on-github-de837063c12
# Sudoku:
# https://www.killersudokuonline.com/tips.html
# https://sudoku.com/killer/easy/
# https://www.sudokuwiki.org/killersudoku.htm

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import json
#from tkinter import *
#import tkinter as tk
#from future.moves import tkinter
import TkinterExtensions

# For tkinter
#tkinter.Tcl().eval('info patchlevel')
#tk._test()
#root = Tk()

value1 = input("Please enter length_of_one_square e.g. 3:\n")
value2 = input("Please enter total_length e.g. 9:\n")

length_of_one_square = int(value1)
total_length = int(value2)

choice = input("Enter 1 for create_list.\nEnter 2 for specifying Killer game values.:\n")
choice = int(choice)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def saveListToFile(listname, pathtosave):
    with open(pathtosave, 'a') as f:
        f.write(json.dumps(listname) + "\n")


def openFileToList(pathtosave):
    # Now read the file back into a Python list object
    with open(pathtosave, 'r') as f:
        listname = [json.loads(line) for line in f]
    # print('listname = ', listname)
    return listname


def for_recursive(number_of_loops, range_list, execute_function, current_index=0, iter_list=[]):
    # print('number_of_loops = ', number_of_loops, 'range_list = ', range_list)
    if iter_list == []:
        iter_list = [0] * number_of_loops

    if current_index == number_of_loops - 1:
        for iter_list[current_index] in range_list[current_index]:
            execute_function(iter_list)
    else:
        for iter_list[current_index] in range_list[current_index]:
            for_recursive(number_of_loops, iter_list=iter_list, range_list=range_list, current_index=current_index + 1,
                          execute_function=execute_function)


def do_whatever(index_list):
    # print('index_list[:] = ', index_list[:])
    index_list_after_2 = index_list[2:]
    # res returns true if the elements of the list are in a strictly increasing order
    res = all(i < j for i, j in zip(index_list_after_2, index_list_after_2[1:]))

    if sum(index_list[2:]) == index_list[0] and index_list[1] == len(index_list[2:]) and res:
        # print ('res = ', res)
        temp_list = [length_of_one_square]
        index_list = temp_list + index_list
        # Uncomment following line to append into file sum_no_of_squares_list
        # saveListToFile(index_list, 'sum_no_of_squares_list')
        return print(index_list)


def create_list(length_of_one_square):
    last_number = length_of_one_square ** 2
    total_in_one_square = 0
    for x in range(1, last_number + 1):
        print('x = ', x)
        total_in_one_square = total_in_one_square + x
        print('total_in_one_square = ', total_in_one_square)

    # total_in_shape, no_of_squares
    number_of_loops_lv = 3
    for_recursive(range_list=[range(sum(range(1, number_of_loops_lv - 1)),
                                    sum(range(last_number + 3 - number_of_loops_lv, last_number + 1)) + 1),
                              range(number_of_loops_lv - 2, number_of_loops_lv - 1),
                              range(1, last_number + 1)],
                  execute_function=do_whatever, number_of_loops=number_of_loops_lv)
    number_of_loops_lv = 4

    for_recursive(range_list=[range(sum(range(1, number_of_loops_lv - 1)),
                                    sum(range(last_number + 3 - number_of_loops_lv, last_number + 1)) + 1),
                              range(number_of_loops_lv - 2, number_of_loops_lv - 1),
                              range(1, last_number),
                              range(1, last_number + 1)], execute_function=do_whatever,
                  number_of_loops=number_of_loops_lv)
    number_of_loops_lv = 5

    for_recursive(range_list=[range(sum(range(1, number_of_loops_lv - 1)),
                                    sum(range(last_number + 3 - number_of_loops_lv, last_number + 1)) + 1),
                              range(number_of_loops_lv - 2, number_of_loops_lv - 1),
                              range(1, last_number - 1),
                              range(1, last_number),
                              range(1, last_number + 1)], execute_function=do_whatever,
                  number_of_loops=number_of_loops_lv)
    number_of_loops_lv = 6

    for_recursive(range_list=[range(sum(range(1, number_of_loops_lv - 1)),
                                    sum(range(last_number + 3 - number_of_loops_lv, last_number + 1)) + 1),
                              range(number_of_loops_lv - 2, number_of_loops_lv - 1),
                              range(1, last_number - 2),
                              range(1, last_number - 1),
                              range(1, last_number),
                              range(1, last_number + 1)], execute_function=do_whatever,
                  number_of_loops=number_of_loops_lv)
    number_of_loops_lv = 7

    for_recursive(range_list=[range(sum(range(1, number_of_loops_lv - 1)),
                                    sum(range(last_number + 3 - number_of_loops_lv, last_number + 1)) + 1),
                              range(number_of_loops_lv - 2, number_of_loops_lv - 1),
                              range(1, last_number - 3),
                              range(1, last_number - 2),
                              range(1, last_number - 1),
                              range(1, last_number),
                              range(1, last_number + 1)], execute_function=do_whatever,
                  number_of_loops=number_of_loops_lv)
    number_of_loops_lv = 8

    for_recursive(range_list=[range(sum(range(1, number_of_loops_lv - 1)),
                                    sum(range(last_number + 3 - number_of_loops_lv, last_number + 1)) + 1),
                              range(number_of_loops_lv - 2, number_of_loops_lv - 1),
                              range(1, last_number - 4),
                              range(1, last_number - 3),
                              range(1, last_number - 2),
                              range(1, last_number - 1),
                              range(1, last_number),
                              range(1, last_number + 1)], execute_function=do_whatever,
                  number_of_loops=number_of_loops_lv)
    number_of_loops_lv = 9

    for_recursive(range_list=[range(sum(range(1, number_of_loops_lv - 1)),
                                    sum(range(last_number + 3 - number_of_loops_lv, last_number + 1)) + 1),
                              range(number_of_loops_lv - 2, number_of_loops_lv - 1),
                              range(1, last_number - 5),
                              range(1, last_number - 4),
                              range(1, last_number - 3),
                              range(1, last_number - 2),
                              range(1, last_number - 1),
                              range(1, last_number),
                              range(1, last_number + 1)], execute_function=do_whatever,
                  number_of_loops=number_of_loops_lv)
    number_of_loops_lv = 10

    for_recursive(range_list=[range(sum(range(1, number_of_loops_lv - 1)),
                                    sum(range(last_number + 3 - number_of_loops_lv, last_number + 1)) + 1),
                              range(number_of_loops_lv - 2, number_of_loops_lv - 1),
                              range(1, last_number - 6),
                              range(1, last_number - 5),
                              range(1, last_number - 4),
                              range(1, last_number - 3),
                              range(1, last_number - 2),
                              range(1, last_number - 1),
                              range(1, last_number),
                              range(1, last_number + 1)], execute_function=do_whatever,
                  number_of_loops=number_of_loops_lv)
    number_of_loops_lv = 11

    for_recursive(range_list=[range(sum(range(1, number_of_loops_lv - 1)),
                                    sum(range(last_number + 3 - number_of_loops_lv, last_number + 1)) + 1),
                              range(number_of_loops_lv - 2, number_of_loops_lv - 1),
                              range(1, last_number - 7),
                              range(1, last_number - 6),
                              range(1, last_number - 5),
                              range(1, last_number - 4),
                              range(1, last_number - 3),
                              range(1, last_number - 2),
                              range(1, last_number - 1),
                              range(1, last_number),
                              range(1, last_number + 1)], execute_function=do_whatever,
                  number_of_loops=number_of_loops_lv)


def pop_game(length_of_one_square, total_length):
    # saveListToFile(index_list, 'sum_no_of_squares_list')
    index_list_f = openFileToList('sum_no_of_squares_list')
    print('index_list_f = ', index_list_f)
    l_f_length_of_one_square = [x for x in index_list_f if x[0] == length_of_one_square]
    print('l_f_length_of_one_square = ', l_f_length_of_one_square)
    l_f_caged = openFileToList('caged')
    print('l_f_caged = ', l_f_caged)
    # To initialise all possibilities of the individual squares
    l_possibilities = []
    for x in l_f_caged:
        for y in l_f_length_of_one_square:
            if y[1] == x[3] and y[2] == x[4]:
                l_possibilities.append(x + y[3:])
    print('l_possibilities = ', l_possibilities)
    #tkinter grids
    myLabel00 = Label(root, text="00 grid")
    myLabel01 = Label(root, text="01 grid")
    myLabel10 = Label(root, text="10 grid")
    myLabel00.grid(row=0, column=0)
    myLabel01.grid(row=0, column=1)
    myLabel10.grid(row=1, column=0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if choice == 1:
        print(
            f'You entered length_of_one_square = {length_of_one_square} and total_length = {total_length} for create_list')
        create_list(length_of_one_square)
    elif choice == 2:
        print(
            f'You entered length_of_one_square = {length_of_one_square} and total_length = {total_length} for Killer values')
        pop_game(length_of_one_square, total_length)
    else:
        print("Wrong Choice, terminating the program.")

# print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
