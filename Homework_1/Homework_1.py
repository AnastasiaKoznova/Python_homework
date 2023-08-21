#Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
#Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
#Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = float(input('Input side length "A"'))
b = float(input('Input side length "B"'))
c = float(input('Input side length "C"'))
if a > b+c or b > a+c or c > a+b:
    print('The triangle doesnt exist!!!')
else:
    if a != b !=c:
        print('The triangle is scalen.')
    if a == b != c or a != b == c:
        print('The triangle is isoscales.')
    if a == b == c:
        print ('The triangle is eguilateral.')