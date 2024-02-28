'''
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/370357/python-variable-scope-error
''' 

import os

FOLDER_BASE_PATH = "/Users/tactlabs2/Downloads/patterns_rj/"

def list_files(folder_path):
    try:
        files = os.listdir(folder_path)
        print(f'files.datatype : {type(files)}')
        # for path in files:
        #     print(path)
    except FileNotFoundError:
        print("Folder not found.")
    return files

def get_line_count_of_file(current_file):

    file_fullpath = f"{FOLDER_BASE_PATH}{current_file}"
    try:
        with open(file_fullpath,'r') as file:
            line_count = sum(1 for line in file)
            return line_count
    except FileNotFoundError:
        print(f"file not found: {current_file}")
        return -1


def startpy():

    files_in_folder = list_files(FOLDER_BASE_PATH)
    # print(files_in_folder)

    for cfile in files_in_folder:
        # print(cfile)

        c_file_line_count = get_line_count_of_file(cfile)

        print(f'{cfile} - {c_file_line_count}')
    

if __name__ == '__main__':
    startpy()






d



