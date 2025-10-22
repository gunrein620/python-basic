import random

print('숫자 맞추기게임 1-10')
target_num = random.randint(1,10)
op_num = int(input('도전할 기회를 입력하세요:'))

for i in range(op_num):
  ans = int(input(f'정답은? (남은 기회{op_num - i})'))
  if ans == target_num:
    print(f'축하합니다.')
    break
  else:
    print(f'다시 시도하세요')
print(f'정답은 {target_num} 이였습니다.')