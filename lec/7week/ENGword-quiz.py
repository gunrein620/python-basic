import googletrans
translator = googletrans.Translator()

words = {}

def registration():
  s = input('등록할 단어:')
  if s in words:
    print("등록된 단어입니다.")
  else:
    words[s] = translator.translate(s, dest='en').text

def quiz():
  for key, value in words.items():
    ans = input(f'{key}의 영어 이름은?:')
    if ans == value:
      print('정답^^')
    else:
      print('오답ㅜㅜ')
      
while True:
  option = int(input('1:등록 | 2:퀴즈 | 3: 종료'))
  
  if option == 1:
    registration()
  elif option == 2:
    quiz()
  elif option == 3:
    print('종료합니다.')
    break
  else:
    print('잘못된 입력.')
  