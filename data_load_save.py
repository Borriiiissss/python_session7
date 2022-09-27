
def find_info():
    print('модуль поиска')
    user_inp = input('введите данные для поиска: ').lower()
    with open ('db.csv', 'r') as reading:
        for line in reading:
            if line.lower().count(user_inp):
                print (f'данные найдены {line}')

def add_info():
    print ('модуль добавления')
    user_inp = input('введите данные для добавления: ').lower()
    with open ('db.csv', 'a') as adding:
        adding.writelines(user_inp)
    print (f'данные добавлены {user_inp}')

def delete_info():
    print ('модуль удаления')
    user_inp = input('введите данные для удаления: ').lower()
    with open ('db.csv', 'r') as reading:
        for line in reading:
            if line.lower().count(user_inp):
                print (f'эти данные будут удалены {line} ')
                delete_line(line)
                
def delete_line(line):
    with open ('db.csv', 'r') as reading:
        data = reading.read()
        data = data.replace(line, '')
    with open('db.csv', 'w') as writing_operation:
        writing_operation.writelines(data)

def import_info():
    print ('модуль импортирования')
    user_inp = input('введите название файла для импорта: ')
    with open (user_inp, 'r') as reading:
        data = reading.read()
    with open ('db.csv', 'a') as adding:
        adding.writelines('\n')
        adding.writelines(data)
    print (f'данные добавлены {data}')

def export_info():
    print ('модуль экспортирования')
    user_inp = input('введите название файла для экспора: ')
    with open ('db.csv', 'r') as reading:
        data = reading.read()
    with open(user_inp, 'w') as writing_operation:
        writing_operation.writelines(data)
    print (f'данные экспортированы {data}')
    