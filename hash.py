tuple_a = (1,2,3)
tuple_b = (1,2,3)

tuple_a.__hash__() # 
tuple_b.__hash__()

print(id(tuple_a) == id(tuple_b)) # True
print(tuple_a.__hash__())
print(id(tuple_a))