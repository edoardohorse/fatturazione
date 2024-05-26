from dataclasses import dataclass
from typing import List

from articolo import *
from formato import FormatoColumn, extractFormatiConQuantitaFromRow
from utils import epurateNaNOfRowByIndex, Field
import pandas as pd
from const import CODICE_FORNITORE
from puntovendita import PuntoVendita

@dataclass
class TipoRecord(Field):
  length : int = 2
  mandatory: bool = True

@dataclass
class Progressivo(Field):
  length : int = 5
  mandatory: bool = False

@dataclass
class NumeroFattura(Field):
  length : int = 6
  mandatory: bool = True

@dataclass
class Datafattura(Field):
  length : int = 6
  mandatory: bool = True

@dataclass
class RifBolla(Field):
  length : int = 6
  mandatory: bool = False

@dataclass
class Databolla(Field):
  length : int = 6
  mandatory: bool = False

@dataclass
class Codicefornitore(Field):
  length : int = 15
  mandatory: bool = True

@dataclass
class TipocodFornitore(Field):
  length : int = 1
  mandatory: bool = True

@dataclass
class CodiceClienteforn(Field):
  length : int = 15
  mandatory: bool = False

@dataclass
class CodiceCooperativa(Field):
  length : int = 15
  mandatory: bool = False

@dataclass
class Codicesocio(Field):
  length : int = 15
  mandatory: bool = True

@dataclass
class TipoCodicesocio(Field):
  length : int = 1
  mandatory: bool = True

@dataclass
class TipoDocumento(Field):
  length : int = 1
  mandatory: bool = True

KEYS_TO_INTERPOLATE = [
'tipo_record',
'progressivo',
'rifFattura',
'data_fattura',
'rif_bolla',
'data_bolla',
'codice_fornitore',
'tipocodFornitore',
'codice_clienteforn',
'codice_cooperativa',
'codice_socio',
'tipo_codicesocio',
'tipo_documento',
]

@dataclass
class Buono:
  articoli : List[Articolo] = None
  index: int  = None
  tipo_record :        Optional[TipoRecord] = None        #01
  progressivo :        Optional[Progressivo] = None       #02
  rifFattura :         Optional[NumeroFattura] = None     #03
  data_fattura :       Optional[Datafattura] = None       #04
  rif_bolla :          Optional[RifBolla] = None          #05
  data_bolla :         Optional[Databolla] = None         #06
  codice_fornitore :   Optional[Codicefornitore] = None   #07
  tipocodFornitore :   Optional[TipocodFornitore] = None  #08
  codice_clienteforn : Optional[CodiceClienteforn] = None #09
  codice_cooperativa : Optional[CodiceCooperativa] = None #10
  codice_socio :       Optional[Codicesocio] = None       #11
  tipo_codicesocio :   Optional[TipoCodicesocio] = None   #12
  tipo_documento :     Optional[TipoDocumento] = None     #13
  
  def __init__(self, df: pd.DataFrame, index: int, puntiVendita: dict[str, PuntoVendita]):
    self.articoli = []
    self.index = index
    
    numFattura = None
    dataFattura = None
    dataBolla = None
    codiceSocio = puntiVendita[df.iloc[index]["nome"]]
    # print(codiceSocio)

    self.tipo_record = TipoRecord(value=2)
    self.progressivo = Progressivo(value=self.index)
    # self.rifFattura = NumeroFattura(value=rifFattura) # TODO da inserire ogni volta a mano
    # self.data_fattura = Datafattura(value=dataFattura) #TODO da inserire ogni volta a mano
    self.rif_bolla =  RifBolla(value=self.index)
    # self.data_bolla = Databolla(value=dataBolla) # TODO da prendere da venduto
    self.codice_fornitore = Codicefornitore(value=CODICE_FORNITORE)
    self.codice_socio = Codicesocio(value=codiceSocio.codice)
    self.tipo_codicesocio = TipoCodicesocio(value="1")
    self.tipo_documento = TipoDocumento(value="F")
    
  
  def getArticoli(self, df: pd.DataFrame) -> List[Articolo]:
    rowCleaned = epurateNaNOfRowByIndex(df, self.index)

    formatiFromRow = extractFormatiConQuantitaFromRow(rowCleaned)

    articoli = []
    indexArticolo = 1
    
    for codiceFormato in formatiFromRow:
      formatoColumn: FormatoColumn = formatiFromRow[codiceFormato]

      importoNetto = round(formatoColumn.quantita*float(formatoColumn.formato.prezzo), 2)
      
      # print(formatoColumn.formato.articolo)
      articolo = Articolo(
        tipo_record           = TipoRecord          (value=2),
        progressivo           = Progressivo         (value=indexArticolo), # TODO
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
      indexArticolo = indexArticolo + 1
      
      self.articoli = articoli
       

  def __self_interpolate__(self):
    stringCsv = ""
    for key, value in asdict(self).items():
      if key not in KEYS_TO_INTERPOLATE: continue
      if value is not None:
        stringCsv = stringCsv+getattr(self,key).__value__()
        # print(key, getattr(self,key).__value__())
        
    return stringCsv

  def __interpolate__(self):
    stringCsv = self.__self_interpolate__() + '\r\n'

    for articolo in self.articoli:
      stringCsv = stringCsv+articolo.__interpolate__() + '\r\n'

    return stringCsv





def NuovoBuono(df: pd.DataFrame, index: int, puntiVendita: dict[str, PuntoVendita])-> Buono:
  
  buono : Buono = Buono(df=df, index =index, puntiVendita=puntiVendita)
  buono.getArticoli(df)
  
  # print(buono.__interpolate__())
  return buono  

""" 
if __name__ == "__main__":

  exit() """