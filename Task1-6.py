a = int(input('Введите начальную дистанцию, пробегаемую спортсменом в день: '))
b = int(input('Введите требуемое расстояние: '))
day = 1
while a < b:
    a = a * 1.1
    day = day + 1
print(f'Спортсмен добъется необходимого результата на {day} день')

