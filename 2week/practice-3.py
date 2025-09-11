americano = 3000
latte = 3300
greentea = 3600 

ac = int(input('아메리카노 주문개수:'))
lc = int(input('라떼 주문개수:'))
gc = int(input('그린티 주문개수:'))

print(f'총 가격은 {(americano * ac)+(latte * lc)+(greentea * gc)} 원입니다.')