from random import choice
names = '''Алексей
Артём
Вадим
Владимир
Валентин
Данил
Денис
Дмитрий
Егор
Кирилл
Леонид
Максим
Матвей
Никита
Олег
Павел
Пётр
Роман
Сергей
Станислав'''.split('\n')
names2 = '''Иванов
Смирнов
Кузнецов
Попов
Васильев
Петров
Соколов
Михайлов
Новиков
Фёдоров
Морозов
Волков
Алексеев
Лебедев
Семёнов
Егоров
Павлов
Козлов
Степанов
Николаев'''.split('\n')
names3 = '''Аля
Настя
Аня
Ника
Вика
Катя
Лена
Ира
Ксюша
Лара
Марина
Маша
Надя
Наташа
Нина
Оксана
Оля
Света
Таня
Юля'''.split('\n')
names4 = '''Иванова
Смирнова
Кузнецова
Попова
Васильева
Петрова
Соколова
Михайлова
Новикова
Фёдорова
Морозова
Волкова
Алексеева
Лебедева
Семёнова
Егорова
Павлова
Козлова
Степанова
Николаева'''.split('\n')
def generate():
    return choice([choice(names) + ' ' + choice(names2),
                   choice(names3) + ' ' + choice(names4)])

    