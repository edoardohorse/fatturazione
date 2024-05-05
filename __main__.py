
from utils import *
from buono import *


data = fetchDataFromVenduto()
buono = NuovoBuono(data, 0)

print(buono.__interpolate__())



""" for key in row.keys():
  if row[key] is not None:
    print(f"{key} {row[key]}") """