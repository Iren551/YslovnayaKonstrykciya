#number = int(input('Введите число: '))
#if number % 3 == 0 and number % 5 == 0:
#    print('FizzBuzz')
#elif number % 3 == 0:
#    print('Fizz')
#elif number % 5 == 0:
#    print('Buzz')
#else:
#    print('Число не подходит')

number1 = int(input('First: '))
number2 = int(input('Second: '))
number3 = int(input('Third: '))
if number1 == number2 and number1 == number3:
    print('Все', 3, 'числа равны между собой')
elif number1 == number2 or number2 == number3 or number3 == number1:
    print('Равны', 2, 'числа из введенных')
else:
    print(0, 'равных чисел')