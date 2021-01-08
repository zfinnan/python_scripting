hello_file = open("hello.txt", "w")
ga_intro = "Hello to all of my GA family"
hello_file.write(ga_intro)
# print(hello_file.read())
hello_file.close()

car_file = open("car.txt", "w")
new_car_list = 'Tesla Model S\nMercedes C300\nToyota Camry'
car_file.write(new_car_list)
# print(car_file.read())
car_file.close()

# create a file
# my_new_file = open('person.txt', "w")
# my_new_file.write('Zach Finnan\nMike\nDexter\nPete')
# print(my_new_file.readlines())
# my_new_file.close()

with open('person.txt') as people:
    people_list = people.readlines()

    for each_person in people_list:
        print(each_person)

# person_file = open('person.txt')
# print(person_file.read())
# person_file.close()

# with open('person.txt', 'w') as person_file:
#     person_file.write('Pete')

# append to a file
# with open('person.txt', 'a') as person_file:
#     person_file.write('\nMike\nDexter')

# with open('person.txt', 'r+') as person_file:
#     print(person_file.read())
#     person_file.write('\nYvonne')
#     print(person_file.read())

# come back here.
# txt_list = hello_file.read().split(' ')
# print(txt_list)

# with open('hello_txt', 'w+') as hello_file:
#     print(hello_file.read())
    