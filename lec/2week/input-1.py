name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))

print("안녕하세요, " + name + "님!")
if age > 19:
  print("당신은 성인입니다.")
else:
  print("당신은 미성년자입니다.")