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






# file54 = "pattern54.txt"
# file55 = "pattern55.txt"
# file56 = "pattern56.txt"
# output = "files2combine.txt"

# # def pattern():

# with open("pattern54.txt",'r') as f1:
#         content54 = f1.read()
# with open("pattern55.txt",'r') as f:
#         content55 = f.read()
# with open("pattern56.txt",'r') as f2:
#         content56 = f2.read()



# with open("files2combine.txt",'w') as file:
#         file.write(content54)
#         file.write("\n")
#         file.write(content55)
#         file.write("\n")
#         file.write(content56)   



