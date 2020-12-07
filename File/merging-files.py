# В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны,
# пример для выполнения домашней работы можно взять тут
#
# Необходимо объединить их в один по следующим правилам:
#
# Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них
# (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
# Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем

#подсчет количества строк в файле
def line_in_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        count_line = 0
        for _ in f:
            count_line += 1

    return count_line

#анализ файлов от минимум до максимум и печать всей информации в новый файл
def min_file_to_max(file1, file2, file3, new_file):

    file1_line = line_in_file(file1)
    file2_line = line_in_file(file2)
    file3_line = line_in_file(file3)

    dict_file = {file1: file1_line, file2: file2_line, file3: file3_line }

    list_d = list(dict_file.items())
    list_d.sort(key=lambda i: i[1])

    with open(new_file, 'a', encoding='utf-8') as f:
        for i in range(3):
            name_and_line = str(list_d[i][0]) + "\n" + str(list_d[i][1]) +"\n"
            f.write(name_and_line)
            with open(list_d[i][0], 'r', encoding='utf-8') as f2:
                tmp_text = f2.readlines()
                f.write(''.join(tmp_text) + '\n')


file1 = '1.txt'
file2 = '2.txt'
file3 = '3.txt'
new_file = 'new_file.txt'

min_file_to_max(file1, file2, file3, new_file)