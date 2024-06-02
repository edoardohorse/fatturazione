
from utils import *
from buono import *
from ui import launchUI
from puntovendita import fetchPuntiVenditaMegagest
from ui import Result
from tkinter import filedialog
import tkinter as tk
import time


data = None
puntivendita = None

def onReady(res: Result):
  global data, puntivendita
  
  print(res)
  data = fetchDataFromVenduto(filename=res['filename'], sheet=res['mese'])
  
  puntivendita = fetchPuntiVenditaMegagest(filename=res['filename'])
  return [data, puntivendita]
  
def launchConversion(ui):
  global data, puntivendita
  
  filenameToExport = createFileToExport()
  nRows = data.shape[0]
  
  ui['progress'].start(nRows)
  contentFile = ''
  
  for index in range(nRows):
    buono = NuovoBuono(df=data, index=index, puntiVendita=puntivendita)

    # print(buono.__interpolate__())
    contentFile = contentFile + buono.__interpolate__()
    
    log = f"Buono {index+1} fatto"
    print(log)
    ui['info'].printInfo(log)
    ui['progress'].update(index)

  

  appendToText(filename=filenameToExport, content=contentFile)
  
  ui['progress'].stop()
  tk.messagebox.showinfo("Succes", "Finito!")
  
  ui['root'].destroy()

def appendToText(filename:str, content:str):
  with open(filename, "w") as file:
    file.write(content)
    
def createFileToExport():
  return filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])


launchUI(onReady, launchConversion)