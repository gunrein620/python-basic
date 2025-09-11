print('초단위 시간을 받아 시/분으로 변환하는 프로그램')
sec = int(input('초단위 숫자를 입력하세요'))

min = sec // 60
hour = min // 60


print(f'{hour}시간 {min % 60}분 {sec % 60}초 입니다.')

