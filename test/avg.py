### 심사위원 N명의 점수를 입력받고 평균값을 구하는 프로그램
judge = int(input('심사위원 수는?'))
sum = 0

for i in range(judge):
  score = int(input(f'심사위원{i+1}의 평가점수:'))
  sum += score
avg = sum / judge
print(f'평균점수는 {avg}')

