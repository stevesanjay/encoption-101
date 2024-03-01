'''
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/370357/python-variable-scope-error
'''



def city_name():
    with open("city.txt", 'r') as input_file:
        cities = input_file.readlines()
        total_cities = len(cities)
        skipped_cities = []
    with open("city_result_two.txt", 'w') as output_file:
        count = 0 
        for city in cities:
            # print(len(city))
            if len(city) <= 10:
                output_file.write(city)
                count += 1
            else:
                skipped_cities.append(city.strip())
        print(f'Total number of cities with 10 characters or fewer written to the file: {count}')
        print(f'Total number of skipping cities :{total_cities - count}')

        if skipped_cities:
            print("Skipped cities:")
            for skipped_city in skipped_cities:
                print(skipped_city)




def startpy():
    city_name()
    

if __name__ == '__main__':
    startpy()