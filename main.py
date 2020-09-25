# creating a file just for writing the content of our aim
# file1 = open('aim.txt', 'w+')
# str1 = 'our idea is to implement a dictionary where i' \
#            ' have a certain name in the dictionary and if the' \
#            ' user input any word i have to tell the meaning of' \
#            ' that word from our dictionary if it exist'
# file1.write(str1)

# lets start our project
#
# class My_dictionary(dict):
#     def __init__(self):
#         self = dict()
#
#     # function to add key:value
#     def add(self, key, value):
#         self[key] = value
#
#
# dict_obj = My_dictionary()
# dict_obj.key = input("enter the word")
# dict_obj.value = input("enter the value")
#
# dict_obj.add(dict_obj.key, dict_obj.value)
# print(dict_obj)

dict1 = {
    'apple': 'its a kind of fruit',
    'lady finger': 'its a kind of vegetables',
    'rose': 'its a kind of flower and it is very close to love',
    'laugh': 'when a person express their feeling in happy time, it is called that he is laughing. so it is nothing '
             'but a emotion ',
    'water': 'its a liquor which is being used by the all living things for surviving'
}


def search_word():
    word = input('enter the word: ')
    if word in dict1:
        print('meaning is:', end='')
        print(dict1[word])
    else:
        print('word not found')


search_word()

num1 = int(input('press any integer to continue search:'))

while num1:
    search_word()
    num1 = int(input('press any integer to continue search:'))
