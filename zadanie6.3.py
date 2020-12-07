# Написать функцию перевода размеров женского белья из международного во все остальные. 
# Внтри функции нужно просто обращаться к правильно составленному словарю.
inter = ['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL']
clothing = {
    # 'waist' : ['']
    # 'hips' :
    'Ru': [42, 44, 46, 48, 50, 52, 54, 56], #Россия
    'Ge' : [36, 38, 40, 42, 44, 46, 48, 50], #Германия
    'US' : [8, 10, 12, 14, 16, 18, 20, 22], #США
    'Fr' : [38, 40, 42, 44, 46, 48, 50, 52], #Франция
    'UK': [24, 26, 28, 30, 32, 34, 36, 38] #Англия
}

def size_convert(size):
    s = inter.index(size)
    for key, value in clothing.items():
        print(key, value[s])


size = input('Enter your international size: ')
a = size_convert(size)
