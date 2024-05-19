# 3. Работаем с выводом данных
# 2. Сдача всем
def is_natural(string):
    while True:
        print(string)
        var = input()
        if var.isdigit() and int(var) > 0:
            return int(var)
        print('Введено некорректное число: ' + var)


print('Введите название товара:')
name = input()
price = is_natural('Введите цену товара руб/кг (натуральное число):')
weight = is_natural('Введите вес товара кг (натуральное число):')
money = is_natural('Введите количество денежных средств у пользователя руб (натуральное число):')

if price * weight <= money:
    print('Чек\n' + name + ' - ' + str(weight) + 'кг' + ' - ' + str(price) + 'руб/кг' + '\nИтого: ' +
          str(price * weight) + 'руб' + '\nВнесено:' + str(money) + 'руб' + '\nСдача: ' + str(money - price * weight)
          + 'руб')
else:
    print('У пользователя недостаточно средств.')
