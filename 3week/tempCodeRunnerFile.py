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