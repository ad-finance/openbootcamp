import functools

lista = [2,34,5,6,7,8,9,1,3]

filtrada = list(filter(lambda x: x % 2, lista))
print("Numeros impares: ",filtrada)
print("Suma de numeros impares: ", functools.reduce(lambda a,b: a+b, filtrada))