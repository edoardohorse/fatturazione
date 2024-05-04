import pandas as pd
from utils import *
from buono import *

filename = "venduto 2024 - Copia edo prova.xlsx"
sheet = "GENNAIO 2024"

df = pd.read_excel(io=filename, sheet_name=sheet)
df = initDataFrame(df)


print(df)

row = epurateRowByIndex(df, 0)


buono = Buono(tipo_record=TipoRecord(value=2),
              descrizione_articolo=DescrizioneArticolo(value="MACCHERONI_INTEGRALI"))

print(buono.__interpolate__())
# print(buono.tipo_record.__value__())
# print(buono.descrizione_articolo.__value__())



""" for key in row.keys():
  if row[key] is not None:
    print(f"{key} {row[key]}") """