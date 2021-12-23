# Sukurti naują projektą (PyCharm programoje) Jame sukurti failą modulis.py, kuriame:
#
# Kintamajam kintamasis priskirti reikšmę „Čia yra kintamasis“
# Sukurti funkciją funkcija(), kuri atspausdina „Čia yra funkcija“.
# Sukurti klasę Objektas, kurį iniciavus atspausdina „Čia yra klasė“.
# Sukurti failą main.py, kuriame:
#
# Importuoti modulį modulis
# Atspausdinti importuotą kintamąjį kintamasis
# Paleisti importuotą funkciją funkcija()
# Inicijuoti importuotos klasės Objektas() objektą

import kintamasis
import funkcija
import objektas



def main():
    print(kintamasis)
    funkcija.funkcija()
    print(objektas.Objektas())



main()