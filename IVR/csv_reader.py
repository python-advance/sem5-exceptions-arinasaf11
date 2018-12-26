import csv
#contextlib - модуль содержит вспомогательные функции для поддержки оператора with
#позволяет нам создать контекстный менеджер, используя функцию contextmanager в качестве декоратора. 
from contextlib import contextmanager

@contextmanager 
#и декорируем нашу функцию file_open с ним. 
#Это позволяет нам вызвать file_open используя оператор "with"
def file_open (file):
    try:
        data = open(file, 'r')
        reader = csv.reader(data) #создаем объект reader для чтения из файла
        yield reader
    except FileNotFoundError:
        print("File not found")
        reader=[]
        yield reader #функция возвращает генератор

 
def file_read(reader):
    for row in reader:
        lst =[]
        for el in row:
          lst.append(el)
        print(lst)

if __name__ == "__main__":
  with file_open ('titanic.csv') as f:
        file_read(f)
