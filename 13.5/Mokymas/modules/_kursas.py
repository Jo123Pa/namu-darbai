# Faile python_kursas.py sukurti objekto klasę PythonKursas, kuri paveldėtų viską iš klasės Kursas,
# bei perrašytų metodą destyti() taip, kad jis spausdintų „Vyksta programavimas"

from Mokymas.modules.kursas import Kursas

class PythonKursas(Kursas):
    def __init__(self, pavadinimas, destytojas, trukme):
        super(). __init__(pavadinimas, destytojas, trukme)

    def destyti(self):
        print('Vyksta programavimas!')


