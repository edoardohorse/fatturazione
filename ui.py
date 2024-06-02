import tkinter as tk
from tkcalendar import DateEntry
from tkinter import filedialog
from tkinter import ttk 
from utils import fetchMesiDalVenduto
import datetime
from dataclasses import dataclass
import pandas as pd


ui = { 
'inputFattura' : None,
'filepicker' : None,
'monthSelector' : None,
'datepicker' : None,
'btn': None,
'progress': None,
'root':None
}

@dataclass
class Result:
  numeroFattura: str = None
  dataFattura: str = None
  filename: str = None
  mese: str = None

class TextInput:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Text Input")

        self.label = tk.Label(root, text="Inserisci il numero della fattura:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5,padx=5)

    def getNumeroFattura(self):
        input_text = self.entry.get()
        # print("Entered text:", input_text)
        
        return input_text    
    
    def alert(self):
      return tk.messagebox.showinfo("Alert", "Inserire il numero di fattura!")
      
    def check(self):
      if self.entry.get() != "": return True
      self.alert()
      return False

class FilePicker:
  filename : str = None
  def __init__(self, root):
    self.root = root

    self.button = tk.Button(self.root, text="Scegli il file del venduto", command=self.open_file_dialog)
    self.button.pack(pady=2)
    
    self.label = tk.Label(self.root)
    self.label.pack(pady=2)
    
  def open_file_dialog(self)->str:
    global ui
    file_path = filedialog.askopenfilename()

    if file_path:
      self.filename = file_path
      mesiDisponibili = fetchMesiDalVenduto(filename=file_path)
      if len(mesiDisponibili) > 0:
        self.label.config(text="File scelto: "+file_path.split("/")[-1])
        
        print("Seleziona il file del venduto", file_path)
        ui['monthSelector'].render(mesiDisponibili)
        
      else: self.alert()
      
    else: self.alert()
    
    return file_path
  
  def alert(self):
    return tk.messagebox.showinfo("Alert", "Scegliere un file del venduto")
    
  def check(self):
    if self.filename is not None: return True
    self.alert()
    return False

class DatePickerApp:
  date: datetime = None
  
  def __init__(self, root):
      self.root = root
      self.root.title("Tkinter Date Picker")
      
      # Label for instructions
      self.label = tk.Label(root, text="Data fattura:")
      self.label.pack(pady=5)
      
      # DateEntry widget
      self.date_entry = DateEntry(root, width=12, background='darkblue',
                                  foreground='white', borderwidth=2, year=2024)
      self.date_entry.pack(pady=2)
      
      
      # Label to display the selected date
      self.date_label = tk.Label(root, text="")
      self.date_label.pack(pady=2)
      
      self.date_entry.bind("<<DateEntrySelected>>", self.on_date_change)
      
  def on_date_change(self, event):
      # Get the selected date
      selected_date = self.date_entry.get_date()
      self.date = selected_date
      # Update the label with the selected date
      self.date_label.config(text=f"Data fattura: {selected_date.strftime('%d/%m/%Y')}")
  
  def alert(self):
    return tk.messagebox.showinfo("Alert", "Seleziona una data emissione fattura")
       
  def check(self):
    if self.date is not None: return True
    self.alert()
    return False
 
class MonthSelectorApp:
  mese: str = None
  def __init__(self, root, onReady):
    self.root = root
    self.onReady = onReady
    self.selected_month = tk.StringVar()
    self.month_label = tk.Label(self.root, text="Scegli mese:")
    self.month_label.pack()
    self.month_menu = tk.OptionMenu(self.root, "",[])
    self.month_menu.pack(pady=5)
      
  def render(self, mesiDisponibili):
    if len(mesiDisponibili) == 0:
      return filepicker.alert()
    
    self.selected_month = tk.StringVar()
    
    self.month_menu.pack_forget() 
    self.month_menu = tk.OptionMenu(self.root, self.selected_month, *mesiDisponibili, command=self.getMese)
    self.month_menu.pack(pady=5) 
         
    # self.selected_month.set(mesiDisponibili[0])  # Set the default selected month
    # months = mesiDisponibili
    # self.month_menu.config(variable=self.selected_month, *mesiDisponibili, command=self.getMese)
    
  def getMese(self,value):
      selected_month = value
      self.mese = selected_month
      print("Selezionato mese:", selected_month)
      checkInputs(self.onReady)
      
      return selected_month
      
  def alert(self):
    return tk.messagebox.showinfo("Alert", "Seleziona il mese da fatturare")
       
  def check(self):
    if self.mese is not None: return True
    self.alert()
    return False
    
class ButtonLaunch:
  def __init__(self, root, onReady, onLaunch) -> None:
    global ui
    self.root = root
    self.onReady = onReady
    self.onLaunch = onLaunch
    
    def onClick():
      res = checkInputs(self.onReady)
      if res is not False:
        self.onLaunch(ui)
      
    
    self.select_button = tk.Button(self.root, text="Lancia", command=onClick)
    self.select_button.pack(side=tk.BOTTOM,pady=10)
  
class VendutoInfo:
 
  def __init__(self, root) -> None:
    self.root = root
    self.status_bar = tk.Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

  def printInfo(self, log: str):
    self.status_bar.config(text=log)
        
def checkInputs(onReady):
  global ui
  
  if not ui['inputFattura'].check():
    return False
  
  if not ui['datepicker'].check():
    return False
  
  if not ui['filepicker'].check():
    return False
  
  if not ui['monthSelector'].check():
    return False
  
  res = {
    "numeroFattura" : ui['inputFattura'].getNumeroFattura(),
    "dataFattura" : ui['datepicker'].date,
    "filename" : ui['filepicker'].filename,
    "mese" : ui['monthSelector'].mese
  }
  
  # print(res)
  
  [data, puntivendita] = onReady(res)

  nRows = data.shape[0] 
  ui['info'].printInfo(f"Trovati {nRows} buoni di megagest")

  return res 
 
 
class Progress:
  def __init__(self, root):
    self.root = root
    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=10)
    self.progressbar = ttk.Progressbar(frame, orient='horizontal', mode='determinate')
    
  def start(self, length: int):
    self.progressbar.pack_forget()
    self.progressbar.config(length=length)
    self.progressbar.pack(pady=5,side=tk.BOTTOM)
    self.progressbar.start()
    
  def stop(self):
    self.progressbar.stop()

  def update(self, value: int):
    self.progressbar['value'] = value 
    self.root.update_idletasks()
     

def launchUI(onReady, onLaunch):
  global ui
  root = tk.Tk()
  
  ui['root'] = root
  ui['inputFattura'] = TextInput(root)
  ui['datepicker'] = DatePickerApp(root)
  ui['filepicker'] = FilePicker(root)
  ui['monthSelector'] = MonthSelectorApp(root, onReady)
  ui['info'] = VendutoInfo(root)
  ui['btn'] = ButtonLaunch(root, onReady, onLaunch)
  ui['progress'] = Progress(root)
  
  root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    inputFattura = TextInput(root)
    datepicker = DatePickerApp(root)
    filepicker = FilePicker(root)
    monthSelector = MonthSelectorApp(root)
    btn = ButtonLaunch(root)
    root.mainloop()
