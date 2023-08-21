#Task 2
#Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
#Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
#Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MIN_LIMIT = 0
MAX_LIMIT = 100000
UNITY = 1
MIN_PRIME_NUM = 2

input_num = -1

while not (MIN_LIMIT <= input_num <= MAX_LIMIT):
    input_num = int(input('Input number'))

if input_num >= MIN_PRIME_NUM:
    sum = 0
    for i in range(UNITY, input_num + 1):
        if input_num % i == 0:
            sum += 1
    if sum <= 2:
        print(f'Number {input_num} is prime.')
    else:
        print(f'Number {input_num} is composite.')
else:
    print('Wrong!')