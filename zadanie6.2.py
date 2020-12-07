# Создать структуру данных для студентов из имен и фамилий, можно случайных. 
# Придумать структуру данных, чтобы указывать, в какой группе учится студент 
#(Группы Python, FrontEnd, FullStack, Java). Студент может учиться в нескольких группах. Затем вывести:
# студентов, которые учатся в двух и более группах
# студентов, которые не учатся на фронтенде
# студентов, которые изучают Python или Java

a_class = {
    'Artemov_Artem' : ['Java'],
    'Alexandrov_Alex' : ['Python', 'FrontEnd'],
    'Denisov_Denis' : ['Java'],
    'Ignatov_Ignat' : ['FrontEnd'],
    'Gerdach_Polina' : ['FrontEnd'],
    'Vichko_Vlad' : ['Python', 'FullStack'],
    'Kasre_Yurii' : ['Python'],
    'Zubrov_Vlad' : ['FrontEnd', 'Java']
}

a = []
b = []
c = []
for key, value in a_class.items():
    
    if len(value) > 1:
        a.append(key)
    if 'FrontEnd' not in value:
        b.append(key)
    if 'Python' in value or 'Java' in value:
        c.append(key)
print(f'students who study in two or more groups: {a}, \n')
print(f'students who do not study on the frontend: {b},\n')
print(f'students who are learning Python or Java: {c}')
    

