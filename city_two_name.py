'''
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/370357/python-variable-scope-error
'''

# def city_name():




    # city = "Phoenix"

    # first_flag = ('a' in city)
    # second_flag = ('i' in city)

    # print(f'first_flag: {first_flag}')
    # print(f'second_flag: {second_flag}')

    # if (first_flag and second_flag):
    #     print('Both a and i are available')
    # else:
    #     print('a and i missing')

    # pass



def city_name():
    with open("city_duplicate.txt", 'r') as input_file:
        cities = input_file.readlines()
    with open("city_result_two.txt", 'w') as output_file:
        for city in cities:
            print(len(city))
            if len(city) == 10:
                # print("it have 10 characters")
                output_file.write(city)
                output_file.write("\n")
            else:
                print("its not have more than 10 characters")
                # if 'a' and 'i' in city:
        

            # shortened_city = city[:10]  # Extract first 10 characters of the city name
            # output_file.write(shortened_city)
            # output_file.write("\n")






def startpy():
    city_name()
    
    # test()
    

if __name__ == '__main__':
    startpy()