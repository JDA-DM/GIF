import pandas as pd
import sys
import os


args = sys.argv
excel_file_path = args[1]

if not os.path.isfile(excel_file_path):
    print("引数のファイルが存在しません")
    exit

df = pd.read_excel(excel_file_path, header=0, index_col=0, sheet_name=None)
for sheet_name in df.keys():
    print(sheet_name)
    file_path = './' + sheet_name + '.csv'
    df[sheet_name].to_csv(file_path, encoding='utf_8_sig')
