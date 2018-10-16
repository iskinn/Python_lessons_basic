# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os, sys

# Создаем директории
def create_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), '{0}'.format(dir_name))
    try:
        os.mkdir(dir_path)
        print("\nДиректрия {0} создана".format(dir_name))
    except FileExistsError:
        print("\nДиректория {0} уже существует")

# Удаляем директории
def rm_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), '{0}'.format(dir_name))
    try:
        os.rmdir(dir_path)
        print("\nДиректрия {0} удалена".format(dir_name))
    except FileNotFoundError:
        print("\nДиректория {0} не существует".format(dir_name))

for i in range(1,10):
    dir_name = 'dir_' + str(i)
    create_dir(dir_name)

for i in range(1,10):
    dir_name = 'dir_' + str(i)
    rm_dir(dir_name)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir():
    print("\nПапки в текущем каталоге:")
    for x in (list(i for i in os.listdir(path=os.getcwd()) if os.path.isdir(i))): print(x)

list_dir()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os, sys, re
from shutil import copyfile

pattern_filename = '\w+\.*\w*$'
filename = sys.argv[0]

a = os.path.dirname(filename) + "/" + "copy_" + (re.search(pattern_filename,filename)).group(0)

copyfile(filename, a)
