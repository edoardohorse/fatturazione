from dataclasses import dataclass
import pandas as pd

SHEET_FORMATI = 'Formati'

from enum import Enum

class FormatoKeys(Enum):
  articolo= "articolo"
  ean     = "ean"
  codice  = "codice"
  grammi  = "grammi"
  lprezzo = "lprezzo"
  sconto  = "sconto"
  iva     = "iva"
    
@dataclass
class Formato:
  articolo: str
  ean: str
  codice: str
  grammi: str
  lprezzo: str
  sconto: str
  iva: str

formato_keys = Formato.__annotations__.keys()

def fetchFormati(filename: str) -> dict[str, Formato]:
  df = pd.read_excel(io=filename, sheet_name=SHEET_FORMATI)
  
  formati = {}

  for index, row in df.iterrows():


    formato = Formato(
      articolo=row["articolo"],
      ean     =row["ean"],
      codice  =row["codice"],
      grammi  =row["grammi"],
      lprezzo =row["lprezzo"],
      sconto  =row["sconto"],
      iva     =row["iva"]
    )

    formati[formato.codice] = formato

  return formati

if __name__ == "__main__":
  print(fetchFormati(filename="venduto 2024.xlsx"))