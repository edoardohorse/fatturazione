import tkinter as tk
from tkcalendar import DateEntry
from tkinter import filedialog
from utils import fetchMesiDalVenduto
import datetime

inputFattura = None
filepicker = None
monthSelector = None
datepicker = None
class TextInput:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Text Input")

        self.label = tk.Label(root, text="Inserisci il numero della fattura:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

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
    self.button.pack(pady=20)
    
  def open_file_dialog(self)->str:
    file_path = filedialog.askopenfilename()

    if file_path:
      self.filename = file_path
      mesiDisponibili = fetchMesiDalVenduto(filename=file_path)
      if len(mesiDisponibili) > 0:
        self.label = tk.Label(root, text="File scelto: "+file_path.split("/")[-1])
        self.label.pack(pady=10)
        
        print("Seleziona il file del venduto", file_path)
        monthSelector.render(mesiDisponibili)
        
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
      self.label.pack(pady=10)
      
      # DateEntry widget
      self.date_entry = DateEntry(root, width=12, background='darkblue',
                                  foreground='white', borderwidth=2, year=2024)
      self.date_entry.pack(pady=10)
      
      
      # Label to display the selected date
      self.date_label = tk.Label(root, text="")
      self.date_label.pack(pady=10)
      
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
  def __init__(self, root):
      self.root = root
      
  def render(self, mesiDisponibili):
    if len(mesiDisponibili) == 0:
      return filepicker.alert()

    self.selected_month = tk.StringVar()
    self.selected_month.set(mesiDisponibili[0])  # Set the default selected month

    self.month_label = tk.Label(self.root, text="Scegli mese:")
    self.month_label.pack(pady=10)

    self.month_menu = tk.OptionMenu(self.root, self.selected_month, *mesiDisponibili, command=self.getMese)
    self.month_menu.pack(pady=5)

  def getMese(self,value):
      selected_month = value
      self.mese = selected_month
      print("Selezionato mese:", selected_month)
      
      return selected_month
    
   
  def alert(self):
    return tk.messagebox.showinfo("Alert", "Seleziona il mese da fatturare")
       
  def check(self):
    if self.mese is not None: return True
    self.alert()
    return False

    
    
class ButtonLaunch:
  def __init__(self, root) -> None:
    self.root = root
    
    self.select_button = tk.Button(self.root, text="Lancia", command=self.check)
    self.select_button.pack(side=tk.BOTTOM,pady=10)
  
  def check(self):
    # if not inputFattura.check():
    #   return
    
    # if not datepicker.check():
    #   return
    
    # if not filepicker.check():
    #   return
    
    if not monthSelector.check():
      return
    
    res = {
      "numeroFattura" : inputFattura.getNumeroFattura(),
      "dataFattura" : datepicker.date,
      "filename" : filepicker.filename,
      "mese" : monthSelector.mese
    }
    
    print(res)
    
    return res 
      


def launchUI():
  root = tk.Tk()
  app = DatePickerApp(root)
  root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    inputFattura = TextInput(root)
    datepicker = DatePickerApp(root)
    filepicker = FilePicker(root)
    monthSelector = MonthSelectorApp(root)
    btn = ButtonLaunch(root)
    root.mainloop()
