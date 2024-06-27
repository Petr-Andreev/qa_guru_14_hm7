import os
import zipfile
import pytest

import files
from script_os import CURRENT_DIRECTORY, FILES_DIR, FOLDER_DIR

folder_name = 'my_folder'
# Полный путь к папке
folder_path = os.path.join(CURRENT_DIRECTORY, folder_name)


source_folder = FILES_DIR
output_zip = FOLDER_DIR
#@pytest.fixture(scope='function', autouse=True)
def test_checking_folder():
    # Проверяем, существует ли папка
    if not os.path.exists(folder_path):
        # Создаем папку, если она не существует
        os.mkdir(folder_path)
        print(f'Папка {folder_name} была успешно создана в директории {CURRENT_DIRECTORY}.')
    else:
        print(f'Папка {folder_name} уже существует в директории {CURRENT_DIRECTORY}.')

def test_create_archive():
    with zipfile.ZipFile('my_archive.zip', 'w') as zf: # создаем архив
        for file in 'file_example_XLSX_50.xlsx, import_empl_csv.csv, python_testing_with_pytest.pdf': # добавляем файлы в архив
            add_file = os.path.join(FILES_DIR, file) # склеиваем путь к файлам которые добавляют в архив
            zf.write(add_file, os.path.basename(add_file)) # добавляем файл в архив



    # yield

    # удаление_файлов_после_архивации() # удаляем файлы после архивации
