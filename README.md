# Самостоятельные работы (ИСР, ВСР)
## Инвариантная самостоятельная работа
## Задания
1.1. Разработать программу с реализацией функции для считывания json- данных из файла и вывод их в табличном виде на экран. Реализовать базовый синтаксис для обработки исключений (try .. except)

1.2. Дополнение программы для считывания данных проверкой утверждений или высказываний (assert). Создание отдельного блока для такой проверки (с помощью __name__) и скрипта командной строки для запуска этих проверок.

1.3. Дополнение программы для считывания данных с использованием менеджера контекстов и реализации расширенного синтаксиса для обработки исключений.

```json
{
	  "passengers": [
	      {
	        "Name": "Lois",
	        "Surname":"Frey",
            "Departure point":"Los-Angeles",
            "Landing point":"New York"
	      },
	      {
	        "Name": "Christina",
	        "Surname":"Milton",
            "Departure point":"Berkeley",
            "Landing point":"Baltimor"
	      },
	     {
	        "Name": "Evan",
	        "Surname":"Pitters",
            "Departure point":"Vegas",
            "Landing point":"Buffalo"
	      },
        {
	        "Name": "Kevin",
	        "Surname":"Hin",
            "Departure point":"Boston",
            "Landing point":"Cary"
	      }
	   ]
	}
```

![таблица](https://github.com/python-advance/sem5-exceptions-arinasaf11/blob/master/ISR/table.jpg?raw=true)

## Вариантная самостоятельная работа
## Задание 1.3
Создание программы для считывания данных формата CSV c использованием функционала модуля contextlib.

```python
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
```
![вывод_данных](https://github.com/python-advance/sem5-exceptions-arinasaf11/blob/master/IVR/titanic.jpg?raw=true)
