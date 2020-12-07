a_class = {
    'Artemov_Artem' : [5, 3, 4, 3, 5, 4, 5],
    'Alexandrov_Alex' : [3, 3, 3, 4, 5, 5, 3],
    'Denisov_Denis' : [4, 5, 3, 5, 4, 3, 5],
    'Ignatov_Ignat' : [4, 3, 2, 4, 3, 3, 2, 4],
    'Gerdach_Polina' : [4, 5, 4, 5, 5, 4, 5]
}

mini = sum(a_class['Artemov_Artem'])
maxi = sum(a_class['Artemov_Artem'])

for i in a_class:
    if sum(a_class[i])<mini:
        worst = i
    if sum(a_class[i])>maxi:
        best = i

print(f'Best student: {best} \nWorst sudent: {worst}')

