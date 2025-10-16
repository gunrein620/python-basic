langs = {'C':0, 'Java':0, 'JS':0, 'Python':0}

while True:
  s = input('선호하는 언어 입력(종료시 q):')
  if s == 'q':
    break
  elif s in langs:
    langs[s] += 1
  else:
    print('잘못된 입력.')
  
for key, value in langs.items():
  print(key, value)