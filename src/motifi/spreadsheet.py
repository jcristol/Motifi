import pandas as pd

def read_excel(filename: str, columns: list=['Name', 'Weight', 'Symbol'], sheetname='Motif'):
  """
  given a excel filename parse the file into a list of dicts
  """
  with pd.ExcelFile(filename) as xl:
    df = xl.parse(sheetname)
    df.columns = df.iloc[0]
    df.reindex(df.index.drop(0))
    df_useful = df[columns]
    return df_useful.to_dict('records')[1:]