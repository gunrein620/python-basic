menus = []
menus.append('짜장면')
menus.append('짬뽕')
menus.append('볶음밥')

print(menus[-1])
print(menus[-2])
print(menus[-3])

print('-'*30)

for i in range(len(menus)):
  print(menus[i])

print('-'*30)

for i,a in enumerate(menus):
  print(i,a)
  
print('-'*30)
### 슬라이싱
letters = ['A','B','C','D','E']

print(letters[1:3])             


