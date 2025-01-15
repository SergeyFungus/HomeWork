import os, time


class Informer:
    def info(self, directory):
        for (dirpath, dirnames, filenames) in os.walk(directory):
            for file in filenames:
                filepath = os.path.join(dirpath, file)
                filetime = os.path.getmtime(filepath)
                formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
                filesize = os.path.getsize(filepath)
                parent_dir = os.path.dirname(filepath)  # os.path.split(os.getcwd())[0]
                print(f'Обнаружен файл: {file}\n'
                      f'Путь: {filepath}\n'
                      f'Размер: {filesize} Байт\n'
                      f'Время изменения: {formatted_time}\n'
                      f'Родительская директория: {parent_dir}\n')


informer = Informer()
while True:
    directory = input('Введите путь к директории или -1 для выхода:\n')
    if directory == -1:
        break
    else:
        informer.info(directory)