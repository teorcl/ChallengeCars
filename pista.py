class Pista():
    def __init__(self):
        self.longitud_pista = 0

    def asignar(self):
        self.longitud_pista = int(input('Ingrese la lingutud de la pista, este valor estará km: '))
        return self.longitud_pista

pista1 = Pista()
pista1.asignar()