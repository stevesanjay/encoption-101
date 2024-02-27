'''
Created on 

@author: Raja CSP Raman

source:
#     https://stackoverflow.com/questions/370357/python-variable-scope-error
# '''

import sys

def read_input(filename):

    line_list = []

    # read input file
    with open(filename,'r')as file:
        # input = file.readline()

        # Read each line from the file
        for line in file:
            line_list.append(line.strip())

    return line_list


def create_pattern_1():

    """

        Sample line:
        5601 Steeles AvenueWest
    """

    # read input file
    line_list = read_input("input1.txt")

    # write result to output file
    with open("pattern1.txt",'a')as f:

        for c_line in line_list:

            # skip the content starts with #
            if(c_line.startswith("#")):
                print(f'skipping {c_line}')
                continue    

            words   = c_line.split() 
            
            content = words[0]+'\t'+"HOUSE_NO"
            content += '\n'+ words[1]+'\t'+"STREET_NAME"
            content += '\n'+ words[2]+'\t'+"STREET_NAME"
            content += '\n' * 2

            print(f'added {c_line}')

            f.write(content)

    print(f"Done Pattern 1")

def create_pattern_2():
    line_list = read_input("input2.txt")

    with open("pattern2.txt",'a')as f:
        for l_list in line_list:
            words = l_list.split()
            content = words[0]+'\t'+"STREET_NAME"
            content += '\n'+ words[1]+'\t'+"STREET_NAME"
            content += '\n' * 2
            f.write(content)

    print(f"Done Pattern 2")


def create_pattern_54():
    line_list = read_input("input54.txt")

    with open("pattern54.txt",'a')as f:
        for f_list in line_list:
            words = f_list.split()
            # for index, value in enumerate(words):
            #     print("Index:", index, "Value:", value)
            content = words[0]+" "+words[1]+'\t'+"HOUSE_NO"
             
            content += '\n'+ words[3]+'\t'+"SUITE_NO"
            content += '\n' * 2
            f.write(content)

    print(f"Done Pattern 54")

def create_pattern_55():
    line_list = read_input("input55.txt")

    with open("pattern55.txt",'a')as f:
        for f_list in line_list:
            words = f_list.split()
            content = words[0]+" / "+words[2]+'\t'+"STREET_NAME"
            content += '\n' * 2
            f.write(content)


def create_pattern_56():
    line_list = read_input("input56.txt")
    with open("pattern56.txt",'a') as f:
        for f_list in line_list:
            words = f_list.split()
            content = words[0]+'\t'+"HOUSE_NO"
            content += '\n'+ words[1]+'\t'+"SUITE_NO"
            content += '\n' * 2
            f.write(content)
def startpy():

    # print("Tact101")

    pattern_no = int(sys.argv[1])

    if(pattern_no == 1):
        create_pattern_1()
    elif(pattern_no == 2):
        create_pattern_2()
    elif(pattern_no == 54):
        create_pattern_54()
    elif(pattern_no == 55):
        create_pattern_55()
    elif(pattern_no == 56):
        create_pattern_56()

    else:
        print("Pattern not available")
    
    

if __name__ == '__main__':
    startpy()