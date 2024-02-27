





import sys

def apply_pattern(input_filename, output_filename, pattern_number):
    templates = {
        1: "{house_number}\tHOUSE_NO\n{street_name}\tSTREET_NAME\n",
        2: "{street_name}\tSTREET_NAME\n"
    }

    
    with open("input1.txt",'r')as file:
     input = file.readline() 
    template = templates.get(pattern_number)
    
    if template :
            with open("patter1.txt",'w')as f:
        # for line in file:
             words = input.split()
        # for word in words:
            f.write(words[0]+'\t'+"HOUSE_NO"+'\n'+ words[1]+'\t'+"STREET_NAME"+'\n'+ words[2]+'\t'+"STREET_NAME")


    


with open("input2.txt",'r')as file:
    input2 = file.readline()
    # print(input)
    with open("pattern2.txt",'w')as f:
        # for line in file:
            words = input2.split()
        # for word in words:
            f.write(words[0]+'\t'+"STREET_NAME"+'\n'+ words[1]+'\t'+"STREET_NAME")



