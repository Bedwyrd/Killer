# This is a sample Python script.

# The Github stuff was done as per
# https://medium.com/analytics-vidhya/how-to-share-the-pycharm-project-on-github-de837063c12
# Sudoku:
# https://www.killersudokuonline.com/tips.html
# https://sudoku.com/killer/easy/
# https://www.sudokuwiki.org/killersudoku.htm

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys
#print('sys.path1 = ', sys.path)
import json
from tkinter import *
import copy
#from iteration_utilities import deepflatten
#import more_itertools

# For tkinter
#tkinter.Tcl().eval('info patchlevel')
#tk._test()

value1 = input("Please enter length_of_one_square e.g. 3:\n")
value2 = input("Please enter total_length e.g. 9:\n")

length_of_one_square = int(value1)
total_length = int(value2)

choice = input("Enter 1 for create_list.\nEnter 2 for specifying Killer game values.:\n")
choice = int(choice)

l_possibilities_latest = []

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
                              range(1, last_number + 1)], execute_function=do_whatever,
                  number_of_loops=number_of_loops_lv)
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

def display_grid(l_possibilities):
    root = Tk()
    #tkinter grids
    prev_record = [-99, -99]
    cum_record = ''
    for n_grid in l_possibilities:
        # print('n_grid = ', n_grid)
        # print('prev_record[0] = ', prev_record[0])
        # print('prev_record[1] = ', prev_record[1])
        if n_grid[0] == prev_record[0] and n_grid[1] == prev_record[1]:
            cum_record = str(cum_record) + '\n' + str(n_grid)
            myLabel = Label(root, text=cum_record)
            print('cum_record = ', cum_record)
        else:
            cum_record = str(n_grid)
            myLabel = Label(root, text=cum_record)
            print('cum_record = ', cum_record)

        myLabel.grid(row=n_grid[0], column=n_grid[1])
        prev_record = n_grid
    root.mainloop()

def cage_no_records(cage_no_squares, l_possibilities):
    l_temp_cage_no_squares = []
    for l_possibility in l_possibilities:
        if l_possibility[2] == cage_no_squares:
            l_temp_cage_no_squares.append(l_possibility)
    return l_temp_cage_no_squares

def cage_fully_in_nonet(cage_no_squares, l_possibilities):
    #l_temp_cage_no_squares = [sub_list[2] for sub_list in l_possibilities]
    l_temp_cage_no_squares = cage_no_records(cage_no_squares, l_possibilities)
    print('l_temp_cage_no_squares = ', l_temp_cage_no_squares)
    l_temp_nonet_no = [(sub_list[0]//length_of_one_square, sub_list[1]//length_of_one_square) for sub_list in l_temp_cage_no_squares]
    print('l_temp_nonet_no = ', l_temp_nonet_no)
    a_set = set(l_temp_nonet_no)
    if len(a_set) > 1:
        print('False')
        return False
    else:
        print('True')
        return True

def one_row_for_all_cage_squares(cage_no_squares, l_possibilities):
    l_temp_cage_no_squares = cage_no_records(cage_no_squares, l_possibilities)
    l_temp_square_nos = [(sub_list[0], sub_list[1]) for sub_list in l_temp_cage_no_squares]
    print('l_temp_square_nos = ', l_temp_square_nos)
    a_set = set(l_temp_square_nos)
    print('a_set = ', a_set)
    if len(a_set) == len(l_temp_square_nos):
        print('True')
        return True
    else:
        print('False')
        return False

def delete_all_values_excluding_cage_in_nonet(cage_no_squares, l_possibilities):
    l_temp_cage_no_squares = cage_no_records(cage_no_squares, l_possibilities)
    l_all_nos_in_cage = [tuple(sub_list[5:]) for sub_list in l_temp_cage_no_squares]
    print('l_all_nos_in_cage = ', l_all_nos_in_cage)
    s_all_nos_in_cage = set(l_all_nos_in_cage)
    print('s_all_nos_in_cage = ', s_all_nos_in_cage)
    #l_all_nos_in_cage_de_dup = list(s_all_nos_in_cage)
    l_all_nos_in_cage_de_dup = [list(x) for x in s_all_nos_in_cage]
    #list(deepflatten(l_all_nos_in_cage_de_dup))
    #list(more_itertools.flatten(l_all_nos_in_cage_de_dup))
    #sum(l_all_nos_in_cage_de_dup, [])
    #l_all_nos_in_cage_de_dup = tuple(l_all_nos_in_cage_de_dup)
    #l_all_nos_in_cage_de_dup = [tuple(x) for x in l_all_nos_in_cage_de_dup]
    #l_all_nos_in_cage_de_dup = [1, 3]
    #list(zip(*l_all_nos_in_cage_de_dup)[0])
    #[y for x in l_all_nos_in_cage_de_dup for y in x]
    l_all_nos_in_cage_de_dup = [*l_all_nos_in_cage_de_dup[0]]
    print('*l_all_nos_in_cage_de_dup = ', *l_all_nos_in_cage_de_dup)
    print('l_all_nos_in_cage_de_dup = ', l_all_nos_in_cage_de_dup)
    l_temp_nonet_no = [(sub_list[0]//length_of_one_square, sub_list[1]//length_of_one_square) for sub_list in l_temp_cage_no_squares]
    print('l_temp_nonet_no = ', l_temp_nonet_no)
    #l_temp_nonet_no = l_temp_cage_no_squares_2[0]//length_of_one_square #, l_temp_cage_no_squares_2[0]//length_of_one_square
    a_set = set(l_temp_nonet_no)
    l_a_set = list(a_set)
    print('l_a_set = ', l_a_set)
    print('l_a_set[0][0] = ', l_a_set[0][0])
    print('l_a_set[0][1] = ', l_a_set[0][1])
    start_row = l_a_set[0][0] * length_of_one_square
    end_row = int(l_a_set[0][0]+1)*length_of_one_square-1
    start_column = l_a_set[0][1]*length_of_one_square
    end_column = int(l_a_set[0][1]+1)*length_of_one_square-1
    print('start_row = ', start_row)
    print('end_row = ', end_row)
    print('start_column = ', start_column)
    print('end_column = ', end_column)
    l_temp_squares_in_nonet = []
    for l_nonet_squares in l_possibilities:
        if l_nonet_squares[0] >= start_row and l_nonet_squares[0] <= end_row and l_nonet_squares[1] >= start_column and l_nonet_squares[1] <= end_column:
            l_temp_squares_in_nonet.append(l_nonet_squares)
    print('l_temp_squares_in_nonet = ', l_temp_squares_in_nonet)
    t_temp_squares_in_nonet = [tuple(x) for x in l_temp_squares_in_nonet]
    print('t_temp_squares_in_nonet = ', t_temp_squares_in_nonet)
    s_temp_squares_in_nonet = set(t_temp_squares_in_nonet)
    t_temp_cage_no_squares = [tuple(x) for x in l_temp_cage_no_squares]
    s_temp_cage_no_squares = set(t_temp_cage_no_squares)
    print('s_temp_cage_no_squares = ', s_temp_cage_no_squares)
    s_temp_squares_in_nonet_minus_cage = s_temp_squares_in_nonet - s_temp_cage_no_squares
    #l_temp_squares_in_nonet_minus_cage = list(s_temp_squares_in_nonet_minus_cage)
    l_temp_squares_in_nonet_minus_cage = [list(x) for x in s_temp_squares_in_nonet_minus_cage]
    print('l_temp_squares_in_nonet_minus_cage = ', l_temp_squares_in_nonet_minus_cage)
    l_possibilities_latest = copy.deepcopy(l_possibilities)
    for x_number in l_all_nos_in_cage_de_dup:
        print('x_number1 = ', x_number)
        for x_possibility_latest in l_possibilities_latest:
            for x_temp_squares_in_nonet_minus_cage in l_temp_squares_in_nonet_minus_cage:
                if x_temp_squares_in_nonet_minus_cage[:] == x_possibility_latest[:]:
                    #x_possibility_latest[5:].remove(x_number)
                    try:
                        print('x_possibility_latest[5:] = ', x_possibility_latest[5:])
                        print('x_possibility_latest.index(x_number, 5) = ', x_possibility_latest.index(x_number, 5))
                        #x_possibility_latest[5:].index(x_number)
                        del x_possibility_latest[x_possibility_latest.index(x_number, 5)]
                        #x_possibility_latest.remove(x_number)
                        print('x_temp_squares_in_nonet_minus_cage1 = ', x_temp_squares_in_nonet_minus_cage,
                              'x_possibility_latest = ', x_possibility_latest)
                    except:
                        print('x_number = ', x_number)
                        print('x_temp_squares_in_nonet_minus_cage2 = ', x_temp_squares_in_nonet_minus_cage,
                              'x_possibility_latest2 = ', x_possibility_latest)
                        pass

    print('l_possibility_latest = ', l_possibilities_latest)

    #my_string = [[89, 111, 117, 32], [104, 97, 118, 101, 32], [109, 97, 100, 101, 32], [109, 121, 32], [115, 111, 117, 108, 46]]
    #for outer_ndx, out in enumerate(my_string):
    #    for inner_ndx, inner in enumerate(out):
    #        if inner < 65:
    #            my_string[outer_ndx][inner_ndx] = None
    #my_string
    #[[89, 111, 117, None], [104, 97, 118, 101, None], [109, 97, 100, 101, None], [109, 121, None], [115, 111, 117, 108, None]]

    #l_possibilities_new = [print('x[0:5] = ', x[0:5]) for x in l_possibilities if x[0:5] in l_temp_squares_in_nonet_minus_cage[0:5]]
    # Following is meant to be intersection code
    #l_possibilities_new = [[x for x in sublist if x in l_temp_squares_in_nonet_minus_cage] for sublist in l_possibilities]
    #l_possibilities_new = [list(filter(lambda x: x in l_possibilities, sublist)) for sublist in l_temp_squares_in_nonet_minus_cage]
    #print(type(l_temp_squares_in_nonet_minus_cage))
    #print(type(l_possibilities))
    #print('l_possibilities_new = ', l_possibilities_new)

    return l_possibilities_latest


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
    display_grid(l_possibilities)

    l_possibilities_sort_cage_no = l_possibilities
    l_possibilities_sort_cage_no.sort(key=lambda i: i[2])
    print('l_possibilities_sort_cage_no = ', l_possibilities_sort_cage_no)
    # De-duplicate cage numbers
    #for sub_list in l_possibilities_sort_cage_no:
    #    l_possibilities_sort_cage_no.index[sub_list] = sub_list[2]
    l_cage_nos_temp = [sub_list[2] for sub_list in l_possibilities_sort_cage_no]
    print('l_cage_nos_temp = ', l_cage_nos_temp)
    l_cage_nos = list(set(l_cage_nos_temp))
    print('l_cage_nos = ', l_cage_nos)
    for cage_no_squares in l_cage_nos:
        if cage_fully_in_nonet(cage_no_squares, l_possibilities) and one_row_for_all_cage_squares(cage_no_squares, l_possibilities):
            l_possibilities_latest = delete_all_values_excluding_cage_in_nonet(cage_no_squares, l_possibilities)
            print('In delete_all_values_excluding_cage_in_nonet')
            pass

        #if cage_only_horizontal(cage_no_squares, l_possibilities) and one_row_for_all_cage_squares(cage_no_squares, l_possibilities):
        #    delete_all_values_excluding_cage_in_horizontal(cage_no_squares, l_possibilities)
        pass

        #if cage_only_vertical(cage_no_squares, l_possibilities) and one_row_for_all_cage_squares(cage_no_squares, l_possibilities):
        #    delete_all_values_excluding_cage_in_vertical(cage_no_squares, l_possibilities)
        pass

    l_possibilities_sort_square_no = l_possibilities
    l_possibilities_sort_square_no.sort(key=lambda i: (i[0], i[1]))
    print('l_possibilities_sort_square_no = ', l_possibilities_sort_square_no)
    # De-duplicate square numbers
    l_square_nos_temp = [(sub_list[0], sub_list[1]) for sub_list in l_possibilities_sort_square_no]
    print('l_square_nos_temp = ', l_square_nos_temp)
    l_square_nos = list(set(l_square_nos_temp))
    l_square_nos.sort(key=lambda i: (i[0], i[1]))
    print('l_square_nos = ', l_square_nos)
    for all_squares in l_square_nos:
        #if one_value_in_square[0,1] and one_row_for_this_square[0,1]:
        #    delete_all_values_excluding_square_in_nonet(all_squares[0,1])
        #    delete_all_values_excluding_horizontal_in_nonet(all_squares[0, 1])
        #    delete_all_values_excluding_vertical_in_nonet(all_squares[0, 1])
        pass

    display_grid(l_possibilities_latest)


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
