# Usage
| param      | desc      |
|------------|------------|
| -i         | file venduto.xlsx|
| -o         | output del risultato|
| -data      |data della fattura|
| -mese      | nome del foglio excel (GENNAIO 2024, FEBBRAIO 2024...)|
| -numFattura | numero della fattura|

---

## Example
Basta lanciare il *main.pyw* per avviare la UI

oppure da CLI

```powershell
python .\main.pyw -i '.\venduto 2024.xlsx' -o 'res.txt' -data '02/06/2024' -mese 'GENNAIO 2024' -numFattura '1'
```