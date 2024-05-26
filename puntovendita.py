from dataclasses import dataclass
import pandas as pd
from enum import Enum
from const import SHEET_PUNTI_VENDITA
import re



class PuntoVenditaKeys(Enum):
  codice = "codice"
  descrizione = "descrizione"
    
@dataclass
class PuntoVendita:
  codice: str
  descrizione: str


puntovendita_types = {
  "codice": str,
  "descrizione": str,  
}

puntovendita_keys = PuntoVendita.__annotations__.keys()

def fetchPuntiVenditaMegagest(filename: str) -> dict[str, PuntoVendita]:
  df = pd.read_excel(io=filename, sheet_name=SHEET_PUNTI_VENDITA,dtype=puntovendita_types)
   
  puntivendita = {}
  regex = r'MEGAGEST*'
  
  for index, row in df.iterrows():
    # print(row['codice'])
    descr = row[PuntoVenditaKeys.descrizione.value]
    if re.search(regex, descr):
      puntovendita = PuntoVendita(codice=row["codice"], descrizione=descr)
      puntivendita[ descr ] = puntovendita
    
  
  return puntivendita
  
  
if __name__ == "__main__":
  print(fetchPuntiVenditaMegagest(filename="venduto 2024.xlsx"))