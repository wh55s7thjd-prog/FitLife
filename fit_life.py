"""Проект FitLife — MVP версия 1.0."""

WATER_PER_KG = 30  # воды на килограмм надо в миллилитрах
ML_PER_LITER = 1000  # миллилитров в литре
# 1. Знакомство
user_name = input('Введите имя: ')
user_age = int(input('Введите возраст: '))
# 2. Сбор данных
user_weight = float(input('Введите ваш вес в килограммах: '))
user_height = float(
    input('Введите ваш рост в метрах, используя точку (например: 1.75): ')
)
# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight / (user_height ** 2)
# Подсчет воды: вес * 30 мл
water_needed = user_weight * WATER_PER_KG  # воды надо в миллилитрах
water_needed = water_needed / ML_PER_LITER  # воды надо в литрах
# 4. Вывод красивого результата
print(f'Привет, {user_name}!')
print(f'Отчет для пользователя: {user_name}, {user_age} лет')
print(f'Твой Индекс Массы Тела: {round(bmi, 1)}')
print(f'Рекомендуемая норма воды: {round(water_needed, 1)} литра в день')
print()
print('Расчет окончен. Будьте здоровы!')
