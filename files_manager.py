import os
import shutil
#функция проводника

#создание файла
def create_file(names_files, text=None):
	with open(names_files, 'w', encoding='utf-8') as f:
		if text:
			f.write(text)

#создание папки
def create_papka(names_papka):
	try:
		os.mkdir(names_papka)	
	except FileExistsError:
		print('Файл с таким именем уже есть')	

#вывод всего в папке
def spisok_file():
	print(os.listdir())

#удалить папку
def delete_papka(names_papka_delete):
	os.rmdir(names_papka_delete)

#удалить файл
def delete_file(names_files_delete):
	os.remove(names_files_delete)
#удалить файл
def copy_file(names_f, new_names_f):
	shutil.copy(names_f, new_names_f)

commands_one = ('start')
#пишем команду
while commands_one != 'stop':
	commands_one = input('Напишите свою команду ')
	
	if commands_one == 'createf':
		names = input('Напишите название файла создания ')
		if __name__ == '__main__':
			create_file(names)

	elif commands_one == 'createp':
		names = input('Напишите название папки создания ')
		if __name__ == '__main__':
			create_papka(names)

	elif commands_one == 'list':
		if __name__ == '__main__':
			spisok_file()

	elif commands_one == 'deletef':
		names = input('Напишите название файла удаления ')
		if __name__ == '__main__':
			delete_file(names)

	elif commands_one == 'deletep':
		names = input('Напишите название папки удаления ')
		if __name__ == '__main__':
			delete_papka(names)

	elif commands_one == 'copy':
		names = input('Напишите название файла копирования ')
		two_name = input('Напишите название папки копирования ')
		if __name__ == '__main__':
			copy_file(names, two_name)

	else:
		print('Нет такой комманды')

