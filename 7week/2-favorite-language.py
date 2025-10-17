langs = {}

while True:
  s = input('선호하는 언어 입력(종료시 q):')
  if s == 'q':
    break
  else:
    s = s.lower()  # 입력을 소문자로 변환 (JS → js)
    
    if s in langs:  # 이미 딕셔너리에 존재하는 경우
      langs[s] += 1  # 카운트 증가
    else:  # 처음 입력되는 경우
      langs[s] = 1  # 새로운 키를 1로 초기화
      
for key, value in langs.items():
  print(key, value)