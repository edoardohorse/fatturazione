
from utils import *
from buono import *


data = fetchDataFromVenduto()
buono = NuovoBuono(data, 0)

print(buono.__interpolate__())