'''
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/370357/python-variable-scope-error
'''

import sys

def read_file(filename):
    
        with open( filename ,'r') as a:
            word = a.readlines()

        print(f'word.type: {type(word)}')
        with open("result.txt", 'w') as output_file:
            for idx, item in enumerate(word):
                # print(f'i.type: {type(item)}')
            # if i % 3==0:
                if(idx + 1) % 3 != 0:
                    output_file.write(item.strip())
                    output_file.write("\n")
                    

# read_file()
            
              

def startpy():

    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    read_file(filename) 

if __name__ == '__main__':
       
    startpy()