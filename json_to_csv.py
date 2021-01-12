import glob
import pandas as pd

j = 0
k = 0
pathname = '/home/user3/Documents/Cdac-Project/Activity/*.json'
list_of_paths_to_files = glob.glob(pathname)
print(list_of_paths_to_files)
[print(i) for i in list_of_paths_to_files]
for i in list_of_paths_to_files:
    df = pd.read_json(i)
    df.to_csv(f'/home/user3/Documents/Cdac-Project/Activity_to_csv/acivity{i[-7:-5]}.csv', index = None,header=True)
    j = j+1
    k = k+1