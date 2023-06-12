# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt
import re
from pathlib import Path

# Здесь пишем код
file_task1_answer = open(Path(Path.cwd(), "test_file/task1_answer.txt"), "w+", encoding='utf-8')
file_task1_data = open(Path(Path.cwd(), "test_file/task1_data.txt"), mode='r', encoding='utf-8')
read_file_task1_data = file_task1_data.readlines()
for sting in read_file_task1_data:
    file_task1_answer.writelines(re.sub('[0-9]', '', str(sting)))
file_task1_answer.close()
file_task1_data.close()

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')