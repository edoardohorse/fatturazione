from typing import Dict, Optional
from dataclasses import asdict, dataclass, field

from utils import splitDecimalWithPadding, Field,formatDateToYYYYMMAA

KEYS_TO_INTERPOLATE = [
"tipo_record",
"progressivo",
"codice_articolo",
"descrizione_articolo",
"unita_di_misura",
"quantita",
"prezzo_unitario",
"importo_netto",
"vuoto",
"tipo_IVA",
"aliquota_IVA",
"tipo_movimento",
"tipo_cessione",
"vuoto2",
"tipo_accredito",
"vuoto3"
]



@dataclass
class TipoRecord(Field):
  name : str = "tipo_record"
  length : int = 2
  mandatory : bool = True
  value: int = 0

@dataclass
class Progressivo(Field):
  name : str = "progressivo"
  length : int = 5
  mandatory : bool = True
  value: int = 0

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
  name : str = "unita_di_misura"
  length : int = 2
  mandatory : bool = True

@dataclass
class Quantita(Field):
  name : str = "quantita"
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
class TipoAccredito(Field):
  name : str = "tipo_accredito"
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
    return formatDateToYYYYMMAA(self.value)

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
class Vuoto(Field):
  name : str = "vuoto"
  length : int
  mandatory : bool = True

@dataclass
class Articolo:
  tipo_record:          TipoRecord            = field(default_factory =  lambda : TipoRecord(name="tipo_record",length=2,mandatory=True, value=0)) #01
  progressivo:          Progressivo           = field(default_factory =  lambda : Progressivo(name="progressivo",length=5,mandatory=True)) #02
  codice_articolo:      CodiceArticolo        = field(default_factory =  lambda : CodiceArticolo(name="codice_articolo",length=15,mandatory=True, value="")) #03
  descrizione_articolo: DescrizioneArticolo   = field(default_factory =  lambda : DescrizioneArticolo(name="descrizione_articolo",length=30,mandatory=True, value="")) #04
  unita_di_misura:      UnitaDiMisura         = field(default_factory =  lambda : UnitaDiMisura(name="unita_di_misura",length=2,mandatory=True, value="")) #05
  quantita:             Quantita              = field(default_factory =  lambda : Quantita(name="quantita",length=7,mandatory=True, value="")) #06
  prezzo_unitario:      PrezzoUnitario        = field(default_factory =  lambda : PrezzoUnitario(name="prezzo_unitario",length=9,mandatory=True, value="")) #07
  importo_netto:        ImportoNetto          = field(default_factory =  lambda : ImportoNetto(name="importo_netto",length=9,mandatory=True, value="")) #08
  vuoto:                Vuoto                 = field(default_factory =  lambda : Vuoto(name="vuoto",length=4,mandatory=True, value="")) #09
  tipo_IVA:             TipoIVA               = field(default_factory =  lambda : TipoIVA(name="tipo_IVA",length=1,mandatory=True, value="")) #10
  aliquota_IVA:         AliquotaIVA           = field(default_factory =  lambda : AliquotaIVA(name="aliquota_IVA",length=2,mandatory=True, value="")) #11
  tipo_movimento:       TipoMovimento         = field(default_factory =  lambda : TipoMovimento(name="tipo_movimento",length=1,mandatory=True, value="")) #12
  tipo_cessione:        TipoCessione          = field(default_factory =  lambda : TipoCessione(name="tipo_cessione",length=1,mandatory=True, value="")) #13
  vuoto2:               Vuoto                 = field(default_factory =  lambda : Vuoto(name="vuoto2",length=17,mandatory=True, value="")) #13
  vuoto3:               Vuoto                 = field(default_factory =  lambda : Vuoto(name="vuoto3",length=22,mandatory=True, value="")) #13
  numero_ordine:        NumeroOrdine          = field(default_factory =  lambda : NumeroOrdine(name="numero_ordine",length=6,mandatory=False, value="")) #14
  codice_listino:       CodiceListino         = field(default_factory =  lambda : CodiceListino(name="codice_listino",length=2,mandatory=False, value="")) #15
  tipo_articolo:        TipoArticolo          = field(default_factory =  lambda : TipoArticolo(name="tipo_articolo",length=1,mandatory=False, value="")) #16
  tipo_contratto:       TipoContratto         = field(default_factory =  lambda : TipoContratto(name="tipo_contratto",length=1,mandatory=False, value="")) #17
  tipo_trattamento:     TipoTrattamento       = field(default_factory =  lambda : TipoTrattamento(name="tipo_trattamento",length=1,mandatory=False, value="")) #18
  costo_trasporto:      CostoTrasporto        = field(default_factory =  lambda : CostoTrasporto(name="costo_trasporto",length=5,mandatory=False, value="")) #19
  codice_contabile:     CodiceContabile       = field(default_factory =  lambda : CodiceContabile(name="codice_contabile",length=1,mandatory=False, value="")) #20
  tipo_accredito:       TipoAccredito         = field(default_factory =  lambda : TipoAccredito(name="tipo_accredito",length=1,mandatory=True, value="")) #21
  prezzo_catalogo:      PrezzoCatalogo        = field(default_factory =  lambda : PrezzoCatalogo(name="prezzo_catalogo",length=7,mandatory=False, value="")) #22
  non_usato:            NonUsato              = field(default_factory =  lambda : NonUsato(name="non_usato",length=3,mandatory=False, value="")) #23
  data_ordine:          DataOrdine            = field(default_factory =  lambda : DataOrdine(name="data_ordine",length=6,mandatory=False, value="")) #24
  riservato:            Riservato             = field(default_factory =  lambda : Riservato(name="riservato",length=6,mandatory=False, value="")) #25
  prezzo_pubblico:      PrezzoPubblico        = field(default_factory =  lambda : PrezzoPubblico(name="prezzo_pubblico",length=9,mandatory=False, value="")) #26
  ean:                  EAN                   = field(default_factory =  lambda : EAN(name="ean",length=23,mandatory=False, value="")) #27
  

  def __interpolate__(self):
    stringCsv = ""

    for key, value in asdict(self).items():
      if key not in KEYS_TO_INTERPOLATE: continue
      # print(value)
      
      # if getattr(self, key).__mandatory__() is True:
      stringCsv = stringCsv+getattr(self,key).__value__()
        # print(key, getattr(self,key).__value__())

    return stringCsv
  