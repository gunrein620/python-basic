print('정수를 입력하면 3의 배수이면서 5의 배수인 수를 찾는 프로그램입니다.')
num = int(input('정수를 입력하세요 :'))

if num%3 == 0 and num%5 == 0:
  print('3과 5의 배수 O.')
else:
  print('3과 5의 배수 X')
