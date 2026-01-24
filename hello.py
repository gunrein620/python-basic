x = [1,2,3,4,5,6,7,8,9,10]

result = list(filter(lambda a: a%2== 0,x))
print(result)

#list 컴프리헨션 
result = [a for a in x if a % 2 == 0]
print(result)