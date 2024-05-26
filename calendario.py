import tkinter as tk
from tkcalendar import DateEntry

class DatePickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Date Picker")
        
        # Label for instructions
        self.label = tk.Label(root, text="Select a date:")
        self.label.pack(pady=10)
        
        # DateEntry widget
        self.date_entry = DateEntry(root, width=12, background='darkblue',
                                    foreground='white', borderwidth=2, year=2024)
        self.date_entry.pack(pady=10)
        
        # Button to show the selected date
        self.show_date_button = tk.Button(root, text="Show Date", command=self.show_date)
        self.show_date_button.pack(pady=10)
        
        # Label to display the selected date
        self.date_label = tk.Label(root, text="")
        self.date_label.pack(pady=10)
        
    def show_date(self):
        # Get the selected date
        selected_date = self.date_entry.get_date()
        # Update the label with the selected date
        self.date_label.config(text=f"Selected Date: {selected_date}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DatePickerApp(root)
    root.mainloop()
