import pandas as pd

from const import FILENAME

# get a row from df by its index and return only column that are populated
def epurateNaNOfRowByIndex(df: pd.DataFrame,index: int):
  return df.iloc[index][~df.iloc[index].isna()]

# return a df without rows that haven't an 'n. buono' and datetime type as 'data'
def dropRowsWithoutIDAndDate(df: pd.DataFrame) -> pd.DataFrame:
  mask = pd.to_datetime(df['data'], errors='coerce').notna()
  return df.dropna(subset=['n. buono'])[mask]

# return a df without rows that are not Megagest
def dropRowsNotMegagest(df: pd.DataFrame) -> pd.DataFrame:
  regex = r'MEGAGEST*'
  mask = df.apply(lambda row: not any (row.astype(str).str.contains(regex, regex=True)), axis=1)
  return df[~mask]

def initDataFrame(df: pd.DateOffset)->pd.DataFrame:
  new_df = dropRowsWithoutIDAndDate(df)
  new_df = dropRowsNotMegagest(new_df)
  return new_df


SHEET_MESE = "GENNAIO 2024"

def fetchDataFromVenduto():
  df = pd.read_excel(io=FILENAME, sheet_name=SHEET_MESE)
  df = initDataFrame(df)
  return df
