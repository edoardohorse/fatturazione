from typing import Dict, Optional
from dataclasses import asdict, dataclass

from utils import splitDecimalWithPadding

@dataclass
class Field:
  value: any
  length: int
  
  def __value__(self):
    return str(self.value).strip().rjust(self.length, "0")
  


@dataclass
class TipoRecord(Field):
  name : str = "tipo_record"
  length : int = 2
  mandatory : bool = True

@dataclass
class Progressivo(Field):
  name : str = "progressivo"
  length : int = 5
  mandatory : bool = True

@dataclass
class CodiceArticolo(Field):
  name : str = "codice_articolo"
  length : int = 15
  mandatory : bool = True

@dataclass
class DescrizioneArticolo(Field):
  name : str = "descrizione_articolo"
  length : int = 30
  mandatory : bool = True

@dataclass
class UnitaDiMisura(Field):
  name : str = "unità_di_misura"
  length : int = 2
  mandatory : bool = True

@dataclass
class Quantita(Field):
  name : str = "quantità"
  length : int = 7
  mandatory : bool = True

  def __value__(self):
    return splitDecimalWithPadding(value=self.value, nPaddingInt=5, nPaddingDecimal=2)

@dataclass
class PrezzoUnitario(Field):
  name : str = "prezzo_unitario"
  length : int = 9
  mandatory : bool = True

  def __value__(self):
    return splitDecimalWithPadding(value=self.value, nPaddingInt=5, nPaddingDecimal=4)
  
@dataclass
class ImportoNetto(Field):
  name : str = "importo_netto"
  length : int = 9
  mandatory : bool = True

  def __value__(self):
    return splitDecimalWithPadding(value=self.value, nPaddingInt=7, nPaddingDecimal=2)

@dataclass
class NumeroPezzi(Field):
  name : str = "numero_pezzi"
  length : int = 4
  mandatory : bool = False

@dataclass
class TipoIVA(Field):
  name : str = "tipo_IVA"
  length : int = 1
  mandatory : bool = True

@dataclass
class AliquotaIVA(Field):
  name : str = "aliquota_IVA"
  length : int = 2
  mandatory : bool = True

@dataclass
class TipoMovimento(Field):
  name : str = "tipo_movimento"
  length : int = 1
  mandatory : bool = True

@dataclass
class TipoCessione(Field):
  name : str = "tipo_cessione"
  length : int = 1
  mandatory : bool = True

@dataclass
class NumeroOrdine(Field):
  name : str = "numero_ordine"
  length : int = 6
  mandatory : bool = False

@dataclass
class CodiceListino(Field):
  name : str = "codice_listino"
  length : int = 2
  mandatory : bool = False

@dataclass
class TipoArticolo(Field):
  name : str = "tipo_articolo"
  length : int = 1
  mandatory : bool = False

@dataclass
class TipoContratto(Field):
  name : str = "tipo_contratto"
  length : int = 1
  mandatory : bool = False

@dataclass
class TipoTrattamento(Field):
  name : str = "tipo_trattamento"
  length : int = 1
  mandatory : bool = False

@dataclass
class CostoTrasporto(Field):
  name : str = "costo_trasporto"
  length : int = 5
  mandatory : bool = False

@dataclass
class CodiceContabile(Field):
  name : str = "codice_contabile"
  length : int = 1
  mandatory : bool = False

@dataclass
class TipoReso(Field):
  name : str = "tipo_reso"
  length : int = 1
  mandatory : bool = True

@dataclass
class PrezzoCatalogo(Field):
  name : str = "prezzo_catalogo"
  length : int = 7
  mandatory : bool = False

@dataclass
class NonUsato(Field):
  name : str = "non_usato"
  length : int = 3
  mandatory : bool = False

@dataclass
class DataOrdine(Field):
  name : str = "data_ordine"
  length : int = 6
  mandatory : bool = True

  def __value__(self):
    return self.value.strftime("%Y%m%d")

@dataclass
class Riservato(Field):
  name : str = "riservato"
  length : int = 6
  mandatory : bool = False

@dataclass
class PrezzoPubblico(Field):
  name : str = "prezzo_pubblico"
  length : int = 9
  mandatory : bool = False

@dataclass
class EAN(Field):
  name : str = "ean"
  length : int = 23
  mandatory : bool = True


@dataclass
class Articolo:
  tipo_record:          Optional[TipoRecord]            = None #01
  progressivo:          Optional[Progressivo]           = None #02
  codice_articolo:      Optional[CodiceArticolo]        = None #03
  descrizione_articolo: Optional[DescrizioneArticolo]   = None #04
  unita_di_misura:      Optional[UnitaDiMisura]         = None #05
  quantita:             Optional[Quantita]              = None #06
  prezzo_unitario:      Optional[PrezzoUnitario]        = None #07
  importo_netto:        Optional[ImportoNetto]          = None #08
  numero_pezzi:         Optional[NumeroPezzi]           = None #09
  tipo_IVA:             Optional[TipoIVA]               = None #10
  aliquota_IVA:         Optional[AliquotaIVA]           = None #11
  tipo_movimento:       Optional[TipoMovimento]         = None #12
  tipo_cessione:        Optional[TipoCessione]          = None #13
  numero_ordine:        Optional[NumeroOrdine]          = None #14
  codice_listino:       Optional[CodiceListino]         = None #15
  tipo_articolo:        Optional[TipoArticolo]          = None #16
  tipo_contratto:       Optional[TipoContratto]         = None #17
  tipo_trattamento:     Optional[TipoTrattamento]       = None #18
  costo_trasporto:      Optional[CostoTrasporto]        = None #19
  codice_contabile:     Optional[CodiceContabile]       = None #20
  tipo_reso:            Optional[TipoReso]              = None #21
  prezzo_catalogo:      Optional[PrezzoCatalogo]        = None #22
  non_usato:            Optional[NonUsato]              = None #23
  data_ordine:          Optional[DataOrdine]            = None #24
  riservato:            Optional[Riservato]             = None #25
  prezzo_pubblico:      Optional[PrezzoPubblico]        = None #26
  ean:                  Optional[EAN]                   = None #27
  

  def __interpolate__(self):
    stringCsv = ""

    for key, value in asdict(self).items():
      if value is not None:
        stringCsv = stringCsv+getattr(self,key).__value__()
        # print(key, getattr(self,key).__value__())

    return stringCsv
  