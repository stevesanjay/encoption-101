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
        # print(f'files.datatype : {type(files)}')
        # for path in files:
        #     print(path)
    except FileNotFoundError:
        print("Folder not found.")
    return files

def combine_all_files(s_file_paths, output_path):
    with open(output_path,'w') as fl1:
        for o_path in s_file_paths:
            source_full_path = f"{FOLDER_BASE_PATH}{o_path}"
            print(f'source_full_path : {source_full_path}')
            with open(source_full_path,'r') as fl2:
                content = fl2.read()
                # print(f'content : {content}')
                fl1.write(content)

    print(f'All files added')

def startpy():
    source_file_paths = list_files(FOLDER_BASE_PATH)
    output_path = 'final.txt'
    combine_all_files(source_file_paths, output_path)
    # print("Tact101")





    

if __name__ == '__main__':
    startpy()
