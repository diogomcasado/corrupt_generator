from fileinput import filename
import numbers
import os
import random
import string

os.system('cls')

file_path = os.path.abspath(os.path.dirname(__file__))

extensions = 'doc', 'docx', 'pdf', 'ppt', 'mp3', 'exe', 'zip', 'png'
letters = string.ascii_lowercase


# config for random generation
min_file_size = 1
max_file_size = 15
min_length = 8
max_length = 14
name_upper = True
name_numbers = True

if name_upper:
    letters += string.ascii_uppercase

if name_numbers:
    letters += string.digits


# function to convert megabytes to bytes
def get_bytes(mb):
    mb = 1024 * 1024 * mb
    mb = round(mb)
    return mb


# function to create a random lowercase name with extension
def random_name():
    length = random.randint(min_length, max_length)
    extension = extensions[random.randint(0, len(extensions) - 1)]

    name = ''.join(random.choice(letters) for i in range(length))

    full_name = name + '.' + extension
    return full_name


# function to create the corrupted file
def create_file(name, size):
    path = os.path.join(file_path, name)
    with open(path, 'wb') as fout:
        fout.write(os.urandom(size))
    print('\n' + name + ' created with ' + str(size) + ' bytes\n')


# ask for file size
while True:
    file_size = input('Insert file size in MB (r for random): ')

    try:
        if file_size == 'r':
            file_size = random.uniform(min_file_size, max_file_size)
            file_size = get_bytes(file_size)
            break

        elif float(file_size):
            if float(file_size) > 0:
                file_size = get_bytes(float(file_size))
                break

    except ValueError:
        print('Invalid')


# ask for file name
while True:
    file_name = ''
    try:
        print('\nInsert file name with extension')
        file_name = input('ex: file.pdf, music.mp3 (r for random): ')
    finally:
        if file_name == 'r':
            file_name = random_name()
            create_file(file_name, file_size)
        elif '.' not in file_name:
            continue
        elif file_name.endswith('.'):
            continue
        else:
            create_file(file_name, file_size)
        break
