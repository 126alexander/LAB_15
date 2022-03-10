import os

path = os.getcwd()
print("Текущая директория:", path)
print("Базовое имя пути:", os.path.split(path)[1])
print("Каталог пути:", os.path.split(path)[0])
