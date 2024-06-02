
from utils import *
from buono import *
from ui import launchUI
from puntovendita import fetchPuntiVenditaMegagest
from ui import Result

ui = None
data = None
puntivendita = None

def onReady(res: Result):
  global ui, data, puntivendita
  # data = fetchDataFr  omVenduto()
  # buono = NuovoBuono(data, 0)
  print(res)
  print(ui)
  data = fetchDataFromVenduto(filename=res['filename'], sheet=res['mese'])
  
  puntivendita = fetchPuntiVenditaMegagest(filename=res['filename'])
  return [data, puntivendita]
  
def launchConversion(res:Result):
  global data, puntivendita
  buono = NuovoBuono(df=data, index=0, puntiVendita=puntivendita)

  print(buono.__interpolate__())


ui = launchUI(onReady, launchConversion)