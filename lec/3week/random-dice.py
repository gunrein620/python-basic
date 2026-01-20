import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print(f'주사위1:{dice1} | 주사위2: {dice2}')

if dice1 > dice2:
  print('주사위1 승리')
elif dice1 < dice2:
  print('주사위2 승리')
else:
  print('무승부')