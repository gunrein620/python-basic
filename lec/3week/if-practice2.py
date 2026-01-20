print('높이뛰기 기록을 입력 받아 가장높은 값을 출력하는 프로그램입니다.')
print('선수에게는 총 3번의 기회가 있습니다.')

a = float(input(f'1차 시기:'))
b = float(input(f'2차 시기:'))
c = float(input(f'3차 시기:'))

# 방법 1: 기본적인 if-elif-else 구조 (가장 명확하고 이해하기 쉬움)
if a >= b and a >= c:
    print(f'최고 기록: {a}m')
elif b >= c:
    print(f'최고 기록: {b}m')
else:
    print(f'최고 기록: {c}m')

print()

# 방법 2: max() 함수 사용 (가장 효율적이고 간단함 - 추천!)
highest = max(a, b, c)
print(f'최고 기록: {highest}m')

print()

# 방법 3: 리스트와 max() 활용
records = [a, b, c]
attempts = ['1차', '2차', '3차']
max_record = max(records)
max_index = records.index(max_record)
print(f'최고 기록: {max_record}m ({attempts[max_index]} 시기)')

print()

# 방법 4: 중첩 if문 (비추천 - 복잡함)
if a >= b:
    if a >= c:
        print(f'최고 기록: {a}m')
    else:
        print(f'최고 기록: {c}m')
else:
    if b >= c:
        print(f'최고 기록: {b}m')
    else:
        print(f'최고 기록: {c}m')