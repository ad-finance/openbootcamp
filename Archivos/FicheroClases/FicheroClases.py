import pickle

class Pago:
    Moneda = ""
    Monto = 100

    def __init__(self, Moneda, Monto):
        self.Moneda = Moneda
        self.Monto = Monto

    def getMoneda(self):
        return self.Moneda

f = open('datosPago.bin', 'rb')
Moneda = pickle.load(f)
f.close()

print("Monto: ", Moneda.Monto, Moneda.getMoneda())
