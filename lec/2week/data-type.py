# 문자열 타입
name = "Alice"
print(type(name))

# 숫자 타입
age = 25
print(type(age))

# 불리언 타입
is_student = True
print(type(is_student))

#구조적 자료형 
# 리스트 : 가변성, 수정 가능
numbers = [1,2,3,4,5]
print(type(numbers))

# 튜플 : 불변성, 수정 불가능
coordinates = (10,20)
print(type(coordinates))

# 딕셔너리
person = {"name": "Alice", "age": 25}
print(type(person))

# 집합
unique_numbers = {1,2,3,4,5}
print(type(unique_numbers))

# 네임드 튜플
from collections import namedtuple
named_tuple = namedtuple("Person", ["name", "age"])
print(type(named_tuple))