user = input('Ingrese lista de paises separados por comas: ')

Paises = user.split(',')

SetPaises = set((Paises))

ListaPaises = list(SetPaises)

ListaOrdenada = sorted(ListaPaises)
print(ListaOrdenada)