"""
Задание "Раз, два, три, четыре, пять .... Это не всё?":
Все ученики урбана, без исключения, - очень умные ребята. Настолько умные, что иногда по утру сами путаются в том, что
 намудрили вчера вечером.
Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые). Тем не менее, даже после сна,
 его код остался рабочим и выглядел следующим образом:

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.

Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения для таких структур он
 не нашёл.

Помогите сокурснику осуществить его задумку.

Что должно быть подсчитано:

    Все числа (не важно, являются они ключами или значениям или ещё чем-то).
    Все строки (не важно, являются они ключами или значениям или ещё чем-то)


Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

Входные данные (применение функции):
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


Выходные данные (консоль):
99


Примечания (рекомендации):

    Весь подсчёт должен выполняться одним вызовом функции.
    Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
    Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
    Для определения типа данного используйте функцию isinstance.
"""


def magic_sum(struct_):
    m_sum = 0

    for i in struct_:
        if isinstance(i, int):
            m_sum += i
        elif isinstance(i, str):
            m_sum += len(i)
        elif isinstance(i, dict):
            m_sum += magic_sum(dict(i).keys())
            m_sum += magic_sum(dict(i).values())
        elif isinstance(i, set):
            m_sum += magic_sum(list(i))
        else:
            m_sum += magic_sum(i)
    return m_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(magic_sum(data_structure))
