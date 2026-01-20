import googletrans

translator = googletrans.Translator()

src = input('번역할 내용을 입력하세요')

dest = translator.translate(src, dest='en')
print(f'영어: {dest.text}')

dest = translator.translate(src, dest='ja')
print(f'일본어: {dest.text}')

