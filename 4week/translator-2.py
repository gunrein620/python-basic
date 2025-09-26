import googletrans

translator = googletrans.Translator()
while True:
  lang = input('도착어 선택(영어, 일본어, 독일어 | 종료 |:')
  if lang == '종료':
    print('종료합니다.')
    break
  elif lang=='영어':
    lang = 'en'
  elif lang=='일본어':
    lang = 'ja'
  elif lang=='독일어':
    lang = 'de'
  else:
    print('잘못입력했습니다.')
    continue
  src = input('번역할 내용을 입력하세요')
  dest = translator.translate(src,dest=lang)
  print(dest.text)