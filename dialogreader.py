import random
import os


def get_dialog(chatter_folder, used_indicies=[]):
    '''params: string for chatter folder that dialog is stored in ex:"funfactfred"
    list of used indicies to prevent repeat dialog
    return: one line of dialog and index in a tuple'''
    #get directory of this file
    project_path = os.path.dirname(os.path.abspath("__file__"))
    rel_path = "\character-dialogs\\" + chatter_folder + "\\dialog.txt"
    #add rel path to directory of this file
    file_path = project_path + rel_path

    with open(file=file_path, mode='r') as infile:
        lines = infile.readlines()

        #prevents infinite loop, don't remove
        if len(used_indicies) >= len(lines):
            return "I have no more to say", -1
        index = -1
        while index in used_indicies or index == -1:
            index = random.randrange(0, len(lines))
        dialog = add_newlines(lines[index])
        return dialog, index


def get_dialog_mult(chatter_folder, number_of_lines, used_indicies=[]):
    '''params: string for chatter folder dialog is stored in
    int for number of lines to return
    int previous_index for starting at a certain point in file
    list of used indicies to prevent repeat dialog
    returns: list of dialog and list of indicies in a tuple'''
    dialog_list = []
    i_list = []
    for x in range(0, number_of_lines):
        exclude_i = i_list + used_indicies
        d, i = get_dialog(chatter_folder=chatter_folder, used_indicies=exclude_i)
        dialog_list.append(d)
        i_list.append(i)
    return dialog_list, i_list


def get_dialog_mult_non_rand(chatter_folder, number_of_lines, prev_index):
    pass


def add_newlines(dialog):
    if dialog[-1] != "\n":
        dialog += "\n"
    if len(dialog) > 76:
        for i in range(1, (len(dialog) // 76) + 1):
            dialog = dialog[:i*76] + "\n" + dialog[i*76:]
    return dialog