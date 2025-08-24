import os
import shutil

class FileSystemManager:
    def __init__(self, path):
        self.path = path

    def copy_file(self, source_file, destination_file):
        """
        Копирует информацию файла 1 в файл 2, если они одного типа
        """
        try:
            shutil.copy(source_file, destination_file)
            print(f"Файл {source_file} скопирован в {destination_file}")
        except Exception as e:
            print(f"Ошибка в копировании файла: {e}")

    def delete_file(self, file_path):
        """
        Удаляет файл
        """
        try:
            os.remove(file_path)
            print(f"Файл {file_path} удалён")
        except Exception as e:
            print(f"Ошибка в удалении файла: {e}")

    def count_files_in_folder(self):
        """
        Подсчитывает количество файлов в папке
        """
        count = 0
        for root, dirs, files in os.walk(self.path):
            count += len(files)
        return count

    def search_files_by_filter(self, filter_string):
        """
        Ищет файлы, в которых содержится ключевое слово
        """
        found_files = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if filter_string in file:
                    found_files.append(os.path.join(root, file))
        return found_files

def main():
    manager = FileSystemManager(input("Укажите папку: "))

    while True:
        print("\nКомманды:")
        print("1. Скопировать файл")
        print("2. Удалить файл")
        print("3. Посчитать количество файлов в папке")
        print("4. Найти файл по фильтру")
        print("5. Выйти")

        command = input("Введите число нужной комманды: ")

        if command == "1":
            source_file = input("Укажите файл из которого будет произведено копирование: ")
            destination_file = input("Укажите файл в который будет произведено копирование: ")
            manager.copy_file(source_file, destination_file)
        elif command == "2":
            file_path = input("Укажите файл для удаления: ")
            manager.delete_file(file_path)
        elif command == "3":
            print(f"Количество файлов в папке: {manager.count_files_in_folder()}")
        elif command == "4":
            filter_string = input("Введите ключевое слово: ")
            found_files = manager.search_files_by_filter(filter_string)
            print("Найдены файлы:")
            for file in found_files:
                print(file)
        elif command == "5":
            break
        else:
            print("Невозможная комманда")

if __name__ == "__main__":

    main()
