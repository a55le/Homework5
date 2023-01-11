#Задание 1
import random
k = int(input("Введите натуральную степень k"))
plus_minus = ['+', '-']
polynomial_magnitude = random.randint(1,3)
polynomial_a_coefficient = ''
polynomial_b_coefficient = ''
polynomial_c_coefficient = ''
polynomial = ''
first_plus_minus = random.choice(plus_minus)
second_plus_minus = random.choice(plus_minus)
therd_plus_minus = random.choice(plus_minus)
if polynomial_magnitude == 1:
    polynomial_a_coefficient_yes_no = random.randint(1,2)
    if polynomial_a_coefficient_yes_no == 1:
        polynomial_a_coefficient = random.randint(1,10)
    polynomial = f'{first_plus_minus}{polynomial_a_coefficient}x**{k}'
if polynomial_magnitude == 2:
    polynomial_a_coefficient_yes_no = random.randint(1,2)
    if polynomial_a_coefficient_yes_no == 1:
        polynomial_a_coefficient = random.randint(1,10)
    polynomial_b_coefficient_yes_no = random.randint(1, 2)
    if polynomial_b_coefficient_yes_no == 1:
        polynomial_b_coefficient = random.randint(1,10)
    polynomial = f'{first_plus_minus}{polynomial_a_coefficient}x**{k} {second_plus_minus} {polynomial_b_coefficient}x'
if polynomial_magnitude == 3:
    polynomial_a_coefficient_yes_no = random.randint(1,2)
    if polynomial_a_coefficient_yes_no == 1:
        polynomial_a_coefficient = random.randint(1,10)
    polynomial_b_coefficient_yes_no = random.randint(1, 2)
    if polynomial_b_coefficient_yes_no == 1:
        polynomial_b_coefficient = random.randint(1,10)
    polynomial_c_coefficient = random.randint(1,10)
    polynomial = f'{first_plus_minus}{polynomial_a_coefficient}x**{k} {second_plus_minus} {polynomial_b_coefficient}x {therd_plus_minus} {polynomial_c_coefficient}'
my_file = open('poly.txt', 'w')
my_file.write(f'{polynomial}')
my_file.close()
#Задание 2
poly_1_adres_text = 'Введите адрес файла с первым многочленом. Многочлен должен быть строго в формате по типу -3x**2 + 5x -9 = 0. Внимание, слэши в адресной строки должны смотреть вправо. Если хотите проверить работоспособность программы, введите в эту строку значение "default", при данном значении первый многочлен и второй будут автоматичеси взяты из встроенных файлов\n'
poly_2_adres_text = 'Введите адрес файла со вторым многочленом. Многочлен должен быть строго в формате по типу -3x**2 + 5x -9 = 0. Внимание, слэши в адресной строки должны смотреть вправо. Если хотите проверить работоспособность программы, введите в эту строку значение "default", при данном значении первый многочлен и второй будут автоматическ взяты из встроенных файлов\n'
poly1_adres = input(poly_1_adres_text)
poly2_adres = input(poly_2_adres_text)
if poly1_adres or poly2_adres == 'default':
    poly1_adres = 'poly1.txt'
    poly2_adres = 'poly2.txt'
def split_coeff(file_adres):
    import math
    import re
    #Открытие файла
    poly_file = open(file_adres, 'r')
    poly = poly_file.read()
    poly = list(poly)
    poly_file.close()
    #Выделение конца и его срез
    poly2 = ''
    poly_ended = ''
    if '=' in poly:
        end_index = poly.index('=')
        poly_ended = poly[end_index::]
        poly.pop(len(poly)-1)
        poly.pop(len(poly)-2)
    for i in range(len(poly)):
        poly2 = poly2 + poly[i]
    #Выделение коэффицентов
    poly_split = poly2.split()
    poly_abc_lenght = math.ceil(len(poly_split) / 2)
    poly_abc = [''] * poly_abc_lenght
    poly_abc[0] = poly_split[0]
    poly_split.pop(0)
    poly_split_index1 = 0
    poly_split_index2 = 1
    poly_digits = 0
    for i in range(len(poly_abc)):
        if i == 0:
          continue
        else:
            poly_abc[i] = poly_split[poly_split_index1] + poly_split[poly_split_index2]
            poly_split_index1 = poly_split_index1 + 2
            poly_split_index2 = poly_split_index2 + 2
    #Выбор целочисленных коэффицентов(c)
    poly_abc_splitted = []
    for i in (poly_abc):
       if re.match(r'^[+-][0-9]+$', i):
           poly_digits = poly_digits + int(i)
    poly_abc_splitted = []
    #Разделение коэффицентов на две части
    for i in (poly_abc):
        index = re.search(r'[a-zA-Z]', i)
        if index == None:
            continue
        else:
            index_start = index.start()
            poly_abc_splitted.append(i[:index_start:])
            poly_abc_splitted.append(i[index_start::])
    return poly_abc_splitted, poly_digits, poly_ended
poly1 = split_coeff(poly1_adres)
poly2 = split_coeff(poly2_adres)
#Складываем a,b обоих многочленов
poly = ''
poly_splitted = poly1[0] + poly2[0]
poly_splitted2 = []
poly_splitted3 = []
poly_index = -1
poly_index2 = 0
poly_digit = poly1[1] + poly2[1]
for i in range(int(len(poly_splitted)/2)):
    poly_index = poly_index + 2
    poly_splitted2.append(poly_splitted[poly_index])
for i in range(int(len(poly_splitted)/2)):
    poly_splitted3.append(poly_splitted[poly_index2])
    poly_index2 = poly_index2 + 2



verifiable1 = None
verifiable2 = None
item_index1 = 0
item_index2 = 0
for item in(poly_splitted2):
    verifiable1 = int(poly_splitted3[item_index1])
    verifiable2 = item
    poly_splitted2[item_index1] = ''
    poly_splitted3[item_index1] = 0
    item_index1 = item_index1 + 1
    for i2 in range(len(poly_splitted2)):
        if verifiable2 == poly_splitted2[i2]:
            verifiable1 = verifiable1 + int(poly_splitted3[i2])
            poly_splitted2[i2] = ''
            poly_splitted3[i2] = 0
    if verifiable1 == 0:
        continue
    elif verifiable1 < 0:
        poly = poly + str(verifiable1) + verifiable2
    else:
        poly = poly + '+' + str(verifiable1) + verifiable2
#Работа с концом многочлена
poly_ended = 0
poly_ended1 = poly1[2]
poly_ended2 = poly2[2]
poly_ended1_1 = ''
poly_ended2_1 = ''
if poly1[2] or poly2[2] != '':
    poly_ended_true_or_false = True
else:
    poly_ended_true_or_false = False
if poly_ended_true_or_false is True:
    if poly_ended1 != '':
        poly_ended1 = poly_ended1[2::]
        for i in(poly_ended1):
            poly_ended1_1 = poly_ended1_1 + i
        poly_ended1_1 = int(poly_ended1_1)
        if poly_ended2 != '':
            poly_ended2 = poly_ended2[2::]
            for i in(poly_ended2):
                poly_ended2_1 = poly_ended2_1 + i
            poly_ended2_1 = int(poly_ended2_1)
poly_ended = poly_ended1_1 + poly_ended2_1
if poly_digit > 0:
    poly = poly + '+' + str(poly_digit)
else:
    poly = poly + str(poly_digit)
if poly_ended_true_or_false is True:
    poly = poly + '=' + str(poly_ended)



poly_write = open('poly_answer.txt', 'w')
poly_write.write(poly)
poly_write.close()
print('Сумма многочленов находится в файле poly_answer, если его ранее не было, то он был автоматически создан, в противном случае информация была перезаписана')