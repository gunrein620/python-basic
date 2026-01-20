capitals = {'대한민국':'서울', '미국':'워싱턴', '일본':'도쿄'}

nation = input('국가이름:')

if nation in capitals:
  print(capitals[nation])
else:
  print('해당국가는 등록되지 않았습니다.')