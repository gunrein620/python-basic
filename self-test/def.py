def prepare_shop():
  print('1. open the door')
  print('2. turn on the light')
  print('3. play Music')
  print('4. turn on the 간판')
  
prepare_shop() 

def order_menu(name, qauntity):
  print(name, qauntity,"개 주문이 접수되었습니다.")
  print("주방에 주문이 접수 됩니다.")
  
order_menu("타코야끼",3)
order_menu("생맥주 ",3)

def charge_order(cost, qauntity):
  return int(cost) * int(qauntity)

total_cost = charge_order(input("개당금액"),input("수량"))
print(f'총 지불하실 금액은 {total_cost}원 입니다.')
