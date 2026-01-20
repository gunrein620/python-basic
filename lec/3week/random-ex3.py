import random

user = input('가위, 바위, 보 중 하나를 입력하세요:')

com_rand = random.randint(1,3)
if com_rand == 1:
  computer = '가위'
elif com_rand == 2:
  computer = '바위'
else:
  computer = '보'
  
print(f'사용자: {user} | 컴퓨터: {computer}')

# 방법 1: 명확한 조건문
if user == computer:
  print('비겼습니다.')
elif (user == '가위' and computer == '보') or \
     (user == '바위' and computer == '가위') or \
     (user == '보' and computer == '바위'):
  print('이겼습니다!')
else:
  print('졌습니다!')

print()

# 방법 2: 딕셔너리 활용 (더 깔끔함)
win_cases = {
    '가위': '보',
    '바위': '가위', 
    '보': '바위'
}

if user == computer:
    print('비겼습니다.')
elif win_cases.get(user) == computer:
    print('이겼습니다!')
else:
    print('졌습니다!')