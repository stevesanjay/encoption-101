'''
Created on 

@author: Raja CSP Raman

source:
    ?

model: base101
a b c d e f g h i j k l m n o p q r s t u v w x y z
g a m d r b e t y o z n k s q j w l c v u f h p x i
'''

base_str        = "abcdefghijklmnopqrstuvwxyz"
converted_str   = "gamdrbetyoznksqjwlcvufhpxi"

# with open ('input.txt','w') as file:
#     file.write("one")

# #  file_contents = file.write()
 


def enc_string(abc):

    base_str_list = list(base_str)
    converted_str_list = list(converted_str)
    # file_contents_list = list(file_contents)
    abc_list = list(abc)

    new_str = ""
    for letter in abc_list:

        print(f'letter : {letter}')

        base_index = base_str_list.index(letter)

        # print(f'base_index : {base_index}')

        converted_letter = converted_str_list[base_index]

        # print(f'converted_letter : {converted_letter}')

        new_str += str(converted_letter)

    return new_str

# def write_to_file(file_contents, input.txt):
#     encrypted_contents = enc_string(input.txt)
#     with open(filename, 'w') as f:
#         f.write(encrypted_contents)

def startpy():

    # print("Tact101")
   
    # file_contents = "one"
    print(enc_string("one"))
    
pass
if __name__ == '__main__':
    startpy()