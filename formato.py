from dataclasses import dataclass
import pandas as pd
from enum import Enum
from const import FILENAME
from utils import epurateNaNOfRowByIndex, fetchDataFromVenduto

SHEET_FORMATI = 'Formati'



class FormatoKeys(Enum):
  articolo= "articolo"
  ean     = "ean"
  codice  = "codice"
  grammi  = "grammi"
  prezzo = "prezzo"
  sconto  = "sconto"
  iva     = "iva"
    
@dataclass
class Formato:
  articolo: str
  ean: str
  codice: str
  grammi: str
  prezzo: str
  sconto: str
  iva: str

@dataclass
class FormatoColumn:
  column : str
  quantita: int
  formato: Formato

formato_types = {
  "articolo": str,
  "ean": str,
  "codice": str,
  "grammi": str,
  "prezzo": str,
  "sconto": str,
  "iva": str  
}

formato_keys = Formato.__annotations__.keys()

# fetch formato from sheet Formati and return a dict of them
def fetchFormati(filename: str) -> dict[str, Formato]:
  df = pd.read_excel(io=filename, sheet_name=SHEET_FORMATI,dtype=formato_types)
  
  formati = {}

  for index, row in df.iterrows():

    formato = Formato(
      articolo= row["articolo"],
      ean     = row["ean"],
      codice  = row["codice"],
      grammi  = row["grammi"],
      prezzo  = row["prezzo"],
      sconto  = row["sconto"],
      iva     = row["iva"]
    )

    formati[formato.codice] = formato

  return formati

def extractFormatiConQuantitaFromRow(row: pd.Series)->dict[str,int]:
  formatoCodici = FORMATI_DATA.keys()
  
  formatiEstratti: dict[FormatoColumn] = {}

  for col in row.index:
    if col.split(" ")[0] in formatoCodici:
      codice = col.split(" ")[0]
      formatiEstratti[codice] = FormatoColumn(column=col, quantita=row[col], formato=FORMATI_DATA[codice])

  # print(formatiEstratti)
  return formatiEstratti



FORMATI_DATA = fetchFormati(filename=FILENAME)

if __name__ == "__main__":
  # print(fetchFormati(filename="venduto 2024.xlsx"))
  df = fetchDataFromVenduto()
  row = epurateNaNOfRowByIndex(df, 0)
  print(row)
  extractFormatiConQuantitaFromRow(row)