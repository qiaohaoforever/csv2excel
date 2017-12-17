import sys
import pandas as pd

filename = sys.argv[1].split("/")[-1].split('.')[0]
print(filename)
file_excel = filename+'.xlsx'

def csv_to_xlsx_pd(file_csv):
    csv = pd.read_csv(file_csv, encoding='utf-8',sep='\t')
    csv.to_excel(file_excel, sheet_name='data')

csv_to_xlsx_pd(sys.argv[1])
