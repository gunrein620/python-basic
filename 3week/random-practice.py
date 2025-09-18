import random

a = random.randint(10,50)
b = random.randint(2, 9)
my_quotient = int(input(f'{a}를 {b}로 나눈 몫:'))
print(a/b == my_quotient)
my_remainder = int(input(f'{a} 를 {b}로 나눈 나머지:'))
print(a%b == my_remainder)
