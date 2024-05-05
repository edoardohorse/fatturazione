from dataclasses import dataclass
from typing import List

from articolo import *
from formato import FormatoColumn, extractFormatiConQuantitaFromRow
from utils import epurateNaNOfRowByIndex
import pandas as pd


@dataclass
class Buono:
  articoli : List[Articolo]

  def __interpolate__(self):
    stringCsv = ""

    for articolo in self.articoli:
      stringCsv = stringCsv+articolo.__interpolate__() + '\r\n'

    return stringCsv

def NuovoBuono(df: pd.DataFrame, index: int) -> Buono:
  rowCleaned = epurateNaNOfRowByIndex(df, index)

  articoli = []
  
  formatiFromRow = extractFormatiConQuantitaFromRow(rowCleaned)

  for codiceFormato in formatiFromRow:
    formatoColumn: FormatoColumn = formatiFromRow[codiceFormato]

    importoNetto = round(formatoColumn.quantita*float(formatoColumn.formato.prezzo), 2)
    
    # print(formatoColumn.formato.articolo)
    articolo = Articolo(
      tipo_record           = TipoRecord          (value=2),
      progressivo           = Progressivo         (value=""), # TODO
      codice_articolo       = CodiceArticolo      (value=formatoColumn.formato.codice),
      descrizione_articolo  = DescrizioneArticolo (value=formatoColumn.formato.articolo),
      unita_di_misura       = UnitaDiMisura       (value="PZ"),
      quantita              = Quantita            (value=formatoColumn.quantita),
      prezzo_unitario       = PrezzoUnitario      (value=formatoColumn.formato.prezzo),
      importo_netto         = ImportoNetto        (value=importoNetto),
      tipo_IVA              = TipoIVA             (value=" "),
      aliquota_IVA          = AliquotaIVA         (value=formatoColumn.formato.iva),
      tipo_movimento        = TipoMovimento       (value=" "),
      tipo_cessione         = TipoCessione        (value="1"),
      tipo_reso             = TipoReso            (value=""),
      data_ordine           = DataOrdine          (value=rowCleaned["data"]),
      ean                   = EAN                 (value=formatoColumn.formato.ean)
    )

    articoli.append(articolo)

  buono : Buono = Buono(articoli=articoli)
  # print(buono)
  # print(buono.__interpolate__())
  return buono

""" 
if __name__ == "__main__":

  exit() """