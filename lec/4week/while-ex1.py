import random

guess_num = 0
target = random.randint(1, 10)

print('숫자멎추기 게임 1 - 10 숫자')
while guess_num != target:
  guess_num = int(input('예측 숫자 입력')) 
  if guess_num == target:
    break
  else:
    print("아닙니다 다시 시도하세요")
    
print(f'축하합니다. 정답은 {target} 이였습니다.')
