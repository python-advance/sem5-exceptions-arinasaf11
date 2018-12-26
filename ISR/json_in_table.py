import json

"""Функция для считывания json- данных из файла"""
def json_file_reader(file_name):
    try:
        file = open(file_name, 'r')
        data = json.loads(file.read()) #json.loads - считывание строки в формате JSON в объект Python
        file.close()
    except FileNotFoundError:
        data='File not found'
    return data

"""функция для вывода данных в виде таблицы"""
def printJson(data):
    print( #выводим большую строку с графами нашей таблицы
		'Name'.ljust(16) +    #ljust - дополняет строку до указанной длины указанным символом.
		'Surname'.ljust(16) +
		'Departure point'.ljust(16) +
		'Landing point'.ljust(16)
	)
    print('-'*16*4)
    for i in data["passengers"]: 
        print(
		 str(i["Name"]).ljust(16) + 
		 str(i["Surname"]).ljust(16) +
		 str(i["Departure point"]).ljust(16) +
		 str(i["Landing point"]).ljust(16)
	    )

file_name = 'passengers.json'




"""Cчитывание json-файла с использованием менеджера контекстов"""

with open(file_name, 'r') as f:
    try:
        data = json.load(f)
    except JSONDecodeError:
        print("Not a JSON file")
    else:
        print(data)

printJson(json_file_reader(file_name))

