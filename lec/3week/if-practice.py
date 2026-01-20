age = 0

print('안녕하세요 00 놀이 공원입니다.')
print('나이를 입력해주시면 나이에 따른 할인률을 알려드립니다.')
age = int(input('나이를 입력하세요:'))

if age < 8 :
  print('30% 할인')
elif age < 60:
  print('기본입장료')
else :
  print('20% 할인')