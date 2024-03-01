'''
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/370357/python-variable-scope-error
'''

# def test():

#     city = "Phoenix"

#     first_flag = ('a' in city)
#     second_flag = ('i' in city)

#     print(f'first_flag: {first_flag}')
#     print(f'second_flag: {second_flag}')

#     if (first_flag and second_flag):
#         print('Both a and i are available')
#     else:
#         print('a and i missing')

#     pass

def city_name():
    with open("city1.txt", 'r') as input_file:
        cities = input_file.readlines()  # Split the string into a list of words
        unique_cities = set(cities)  # Convert the list to a set to remove duplicates
    with open("city_result_duplicate.txt", 'w') as output_file:
        for city in unique_cities:
            output_file.write(city)
            # output_file.write("\n")

    







def startpy():
    city_name()
    
    # test()
    

if __name__ == '__main__':
    startpy()