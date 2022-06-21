import json
import csv
import os
import sys
import pandas as pd

args = sys.argv
csv_file_path = args[1]

if not os.path.isfile(csv_file_path):
    print("引数のファイルが存在しません")
    exit

df = pd.read_csv(csv_file_path, header=0, index_col=0)
json_fields = df.to_json(orient='table', force_ascii=False)
file_name = os.path.splitext(os.path.basename(csv_file_path))
print(json.dumps(json.loads(json_fields), indent=2, ensure_ascii=False))