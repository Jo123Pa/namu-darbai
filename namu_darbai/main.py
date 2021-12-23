# Python faile padaryti šiuos veiksmus (atskirai, ne iškart):
# Importuoti modulį datetime.
# Atsispausdinti šiandienos datą ir laiką kartu, tik datą (date.today()) bei tik laiką (.now().time()).
# Iš paketo datetime importuoti modulį date.
# Atsispausdinti šiandienos datą.
# Iš paketo datetime importuoti modulį date kaip data (as data).
# Atsispausdinti šiandienos datą.

import datetime as dt
now = dt.datetime.now()
date = dt.datetime.today().date()
time = dt.datetime.now().time()


from datetime import date 
print(date.today())

from datetime import date as data
print(data.today())
