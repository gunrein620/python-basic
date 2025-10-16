blood = {'A':0, 'B':0, 'AB':0, 'O':0}

while True:
  s = input('혈액형 입력(종료시 q):')
  if s == 'q':
    break
  elif s in blood:
    blood[s] += 1
  else:
    print('없는 혈액형입니다.')
  
print(blood.items())