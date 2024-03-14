def print_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                print(line, end='')
    except:
        print('Файл не найден')


# TEST_5:
with open('Precepts_of_Zote.txt', 'w', encoding='utf-8') as file:
    file.writelines(
        ['Сражения и путешествия берут своё\n', 'Во время отдыха твоё тело становится сильнее, а раны заживают'])

print_file_content('Precepts_of_Zote.txt')