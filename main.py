# This is a sample Python script.

#The Github stuff was done as per https://medium.com/analytics-vidhya/how-to-share-the-pycharm-project-on-github-de837063c12

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import json

length_of_one_square=3
total_length=3

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def saveListToFile(listname, pathtosave):
    with open(pathtosave, 'a') as f:
        f.write(json.dumps(listname) + "\n")

    # Now read the file back into a Python list object
    #with open('test.txt', 'r') as f:
    #    a = json.loads(f.read())

def for_recursive(number_of_loops, range_list, execute_function, current_index=0, iter_list = []):
    #print('number_of_loops = ', number_of_loops, 'range_list = ', range_list)
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
    #print('index_list[:] = ', index_list[:])
    index_list_after_2 = index_list[2:]
    #res returns true if the elements of the list are in a strictly increasing order
    res = all(i < j for i, j in zip(index_list_after_2, index_list_after_2[1:]))

    if sum(index_list[2:]) == index_list[0] and index_list[1] == len(index_list[2:]) and res:
        #print ('res = ', res)
        temp_list = [length_of_one_square]
        index_list = temp_list + index_list
        saveListToFile(index_list, 'sum_no_of_squares_list')
        return print(index_list)

def create_list(length_of_one_square, total_length):
    import json

    last_number = length_of_one_square**2
    total_in_one_square = 0
    for x in range(1, length_of_one_square**2+1):
        print('x = ', x)
        total_in_one_square = total_in_one_square + x
        print('total_in_one_square = ', total_in_one_square)

    # total_in_shape, no_of_squares
    number_of_loops_lv=3
    for_recursive(range_list=[range(sum(range(1, number_of_loops_lv-1)), sum(range(length_of_one_square**2+3-number_of_loops_lv, length_of_one_square**2+1 )) + 1),
                              range(number_of_loops_lv-2, number_of_loops_lv-1),
                              range(1, length_of_one_square**2+1)],
                  execute_function=do_whatever, number_of_loops=number_of_loops_lv)
    number_of_loops_lv = 4

    for_recursive(range_list=[  range(sum(range(1, number_of_loops_lv-1 )), sum(range(length_of_one_square**2+3-number_of_loops_lv, length_of_one_square**2+1 )) + 1),
                                range(number_of_loops_lv-2, number_of_loops_lv-1),
                                range(1, length_of_one_square**2),
                                range(1, length_of_one_square**2+1)], execute_function=do_whatever, number_of_loops=number_of_loops_lv)
    number_of_loops_lv = 5

    for_recursive(range_list=[  range(sum(range(1, number_of_loops_lv-1 )), sum(range(length_of_one_square**2+3-number_of_loops_lv, length_of_one_square**2+1 )) + 1),
                                range(number_of_loops_lv-2, number_of_loops_lv-1),
                                range(1, length_of_one_square**2-1),
                                range(1, length_of_one_square**2),
                                range(1, length_of_one_square**2+1)], execute_function = do_whatever, number_of_loops = number_of_loops_lv)
    number_of_loops_lv = 6

    for_recursive(range_list=[  range(sum(range(1, number_of_loops_lv-1 )), sum(range(length_of_one_square**2+3-number_of_loops_lv, length_of_one_square**2+1 )) + 1),
                                range(number_of_loops_lv-2, number_of_loops_lv-1),
                                range(1, length_of_one_square**2-2),
                                range(1, length_of_one_square**2-1),
                                range(1, length_of_one_square**2),
                                range(1, length_of_one_square**2+1)], execute_function = do_whatever, number_of_loops = number_of_loops_lv)
    number_of_loops_lv = 7

    for_recursive(range_list=[  range(sum(range(1, number_of_loops_lv-1 )), sum(range(length_of_one_square**2+3-number_of_loops_lv, length_of_one_square**2+1 )) + 1),
                                range(number_of_loops_lv-2, number_of_loops_lv-1),
                                range(1, length_of_one_square**2-3),
                                range(1, length_of_one_square**2-2),
                                range(1, length_of_one_square**2-1),
                                range(1, length_of_one_square**2),
                                range(1, length_of_one_square**2+1)], execute_function = do_whatever, number_of_loops = number_of_loops_lv)
    number_of_loops_lv = 8

    for_recursive(range_list=[  range(sum(range(1, number_of_loops_lv-1 )), sum(range(length_of_one_square**2+3-number_of_loops_lv, length_of_one_square**2+1 )) + 1),
                                range(number_of_loops_lv-2, number_of_loops_lv-1),
                                range(1, length_of_one_square**2-4),
                                range(1, length_of_one_square**2-3),
                                range(1, length_of_one_square**2-2),
                                range(1, length_of_one_square**2-1),
                                range(1, length_of_one_square**2),
                                range(1, length_of_one_square**2+1)], execute_function = do_whatever, number_of_loops = number_of_loops_lv)
    number_of_loops_lv = 9

    for_recursive(range_list=[  range(sum(range(1, number_of_loops_lv-1 )), sum(range(length_of_one_square**2+3-number_of_loops_lv, length_of_one_square**2+1 )) + 1),
                                range(number_of_loops_lv-2, number_of_loops_lv-1),
                                range(1, length_of_one_square**2-5),
                                range(1, length_of_one_square**2-4),
                                range(1, length_of_one_square**2-3),
                                range(1, length_of_one_square**2-2),
                                range(1, length_of_one_square**2-1),
                                range(1, length_of_one_square**2),
                                range(1, length_of_one_square**2+1)], execute_function = do_whatever, number_of_loops = number_of_loops_lv)
    number_of_loops_lv = 10

    for_recursive(range_list=[  range(sum(range(1, number_of_loops_lv-1 )), sum(range(length_of_one_square**2+3-number_of_loops_lv, length_of_one_square**2+1 )) + 1),
                                range(number_of_loops_lv-2, number_of_loops_lv-1),
                                range(1, length_of_one_square**2-6),
                                range(1, length_of_one_square**2-5),
                                range(1, length_of_one_square**2-4),
                                range(1, length_of_one_square**2-3),
                                range(1, length_of_one_square**2-2),
                                range(1, length_of_one_square**2-1),
                                range(1, length_of_one_square**2),
                                range(1, length_of_one_square**2+1)], execute_function = do_whatever, number_of_loops = number_of_loops_lv)
    number_of_loops_lv = 11

    for_recursive(range_list=[  range(sum(range(1, number_of_loops_lv-1 )), sum(range(length_of_one_square**2+3-number_of_loops_lv, length_of_one_square**2+1 )) + 1),
                                range(number_of_loops_lv-2, number_of_loops_lv-1),
                                range(1, length_of_one_square**2-7),
                                range(1, length_of_one_square**2-6),
                                range(1, length_of_one_square**2-5),
                                range(1, length_of_one_square**2-4),
                                range(1, length_of_one_square**2-3),
                                range(1, length_of_one_square**2-2),
                                range(1, length_of_one_square**2-1),
                                range(1, length_of_one_square**2),
                                range(1, length_of_one_square**2+1)], execute_function = do_whatever, number_of_loops = number_of_loops_lv)

    """

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')
    """
if __name__ == '__main__':
    #possib(total, no_of_squares, l_combin=None)
    #possib(13, 3, l_combin=None)
    #print_hi('possib(total, no_of_squares, l_combin=None) =', possib(1, 1, l_combin=None))
    create_list(length_of_one_square, total_length)
#print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
