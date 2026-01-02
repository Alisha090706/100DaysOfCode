# file=open('Day24/Files/my_file.txt')
# contents=file.read()
# print(contents)
# file.close()

''' Whenever a file is opened using file_variable=open(file_name), we need to close the file manually.'''


'''If we open a file using "with" keyword, we don't need to manually close the file.'''

with open('Day24/Files/my_file.txt') as file:
    '''we can not write in this files as the files is only opened in read-only mode'''
    contents=file.read()
    print(contents)

with open('Day24/Files/new_file.txt','w') as file:
    '''If the file doesn't exist, it is created. This does not work in read mode'''
    file.write('Hello! This is a new file.')
