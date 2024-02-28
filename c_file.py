'''
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/370357/python-variable-scope-error
'''

file1 = "pattern1-input-testing.txt"
file2 = "pattern2-input-testing.txt"
file3 = "pattern3-input-testing.txt"
# output = "files2combine.txt"

def file_path(file_paths,output_paths):
    with open(output_paths,'w') as fl1:
        for o_path in file_paths:
            with open(o_path,'r') as fl2:
                fl1.write(fl2.read())





# # def combine(file1,file2,file3):
#     with open(file1,'r') as f1:
#         content1 = f1.read()
#     with open(file2,'r') as f:
#         content2 = f.read()
#     with open(file3,'r') as f2:
#         content3 = f2.read()

# def c_write():
    # with open("files2combine.txt",'w') as file:
    #     file.write(content1)
    #     file.write("\n")
    #     file.write(content2)
    #     file.write("\n")
    #     file.write(content3) 

def startpy():
    file_paths = [file1,file2,file3]
    output_paths = 'files2combine.txt'
    file_path(file_paths,output_paths)
    # print("Tact101")





    

if __name__ == '__main__':
    startpy()






# # def pattern():





with open("files2combine.txt",'w') as file:
        file.write(content54)
        file.write("\n")
        file.write(content55)
        file.write("\n")
        file.write(content56)   