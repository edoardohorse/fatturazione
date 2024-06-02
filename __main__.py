
from utils import *
from buono import *
from ui import launchUI
from puntovendita import fetchPuntiVenditaMegagest
from ui import Result
from tkinter import filedialog
import tkinter as tk
from datetime import datetime



data = None
puntivendita = None

def onReady(res: Result):
  global data, puntivendita
  
  print(res)
  data = fetchDataFromVenduto(filename=res['filename'], sheet=res['mese'])
  
  puntivendita = fetchPuntiVenditaMegagest(filename=res['filename'])
  return [data, puntivendita]
  
def launchConversion(res:Result, ui = None):
  global data, puntivendita
  filenameToExport = None
  if ui:
    filenameToExport = createFileToExport()
  else:
    filenameToExport = res['output']
    
  nRows = data.shape[0]
  
  if ui:
    ui['progress'].start(nRows)
  contentFile = ''
  
  numeroFattura = res['numeroFattura']
  dataFattura = res['dataFattura']  
  
  for index in range(nRows):
    buono = NuovoBuono(df=data, index=index, numFattura=numeroFattura, dataFattura=dataFattura, puntiVendita=puntivendita)

    # print(buono.__interpolate__())
    contentFile = contentFile + buono.__interpolate__()
    
    log = f"Buono {index+1} fatto"
    print(log)
    if ui:
      ui['info'].printInfo(log)
      ui['progress'].update(index)

  

  appendToText(filename=filenameToExport, content=contentFile)
  
  if ui:
    ui['progress'].stop()
    tk.messagebox.showinfo("Succes", "Finito!")
  
    ui['root'].destroy()

def appendToText(filename:str, content:str):
  with open(filename, "w") as file:
    file.write(content)
    
def createFileToExport():
  return filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])


import sys

def cli():
  args = {}
  required_params = ["-i", "-o", "-data", "-mese", "-numFattura"]
  
  
  for i in range(1, len(sys.argv), 2):
      if sys.argv[i][0] == '-' and i + 1 < len(sys.argv):
          args[sys.argv[i]] = sys.argv[i+1]
          
  for param in required_params:
      if param not in args:
          print(f"Error: Parameter '{param}' is missing.")
          return

  res: Result = {
    'filename':args.get("-i"),
    'output':args.get("-o"),
    'numeroFattura': args.get("-numFattura"),
    'dataFattura':datetime.strptime(args.get("-data"), "%d/%m/%Y"),
    'mese':args.get("-mese"),
  } 
  
  
  print(res)
  
  global data, puntivendita
  [data, puntivendita] = onReady(res)  
  launchConversion(res) 

if __name__ == "__main__":
  # print(sys.argv)
  if len(sys.argv) == 1:
    launchUI(onReady, launchConversion)
  else:
    cli()
