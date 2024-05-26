
from utils import *
from buono import *
from calendario import launchUI
from puntovendita import fetchPuntiVenditaMegagest

dataFattura = launchUI()
print(dataFattura)
# data = fetchDataFromVenduto()
# buono = NuovoBuono(data, 0)

data = fetchDataFromVenduto()
puntivendita = fetchPuntiVenditaMegagest(filename="venduto 2024.xlsx")
buono = NuovoBuono(df=data, index=0, puntiVendita=puntivendita)

print(buono.__interpolate__())
