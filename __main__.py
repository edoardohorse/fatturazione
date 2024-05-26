
from utils import *
from buono import *
from puntovendita import fetchPuntiVenditaMegagest


data = fetchDataFromVenduto()
puntivendita = fetchPuntiVenditaMegagest(filename="venduto 2024.xlsx")
buono = NuovoBuono(df=data, index=0, puntiVendita=puntivendita)

print(buono.__interpolate__())