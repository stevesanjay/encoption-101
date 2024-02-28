
'''
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/370357/python-variable-scope-error
'''

import sys

def read_city(file_name):
    line_list =[]
    with open(file_name,'r') as input_file:
        
        for line in input_file:
            line_list.append(line.strip())
    return line_list


def len_city():
    line_list = read_city("input10.txt")
    with open("pattern10.txt", "a") as output_file:
        for line in line_list:
                 
            # city = line.strip()
            length = len(line)
            output_file.write(f"{line}={length}\n")
    # return len_city()



def startpy():
    pattern_no = int(sys.argv[1])

    if(pattern_no == 1):
        len_city()


    # print("Tact101")
    

if __name__ == '__main__':
    startpy()




