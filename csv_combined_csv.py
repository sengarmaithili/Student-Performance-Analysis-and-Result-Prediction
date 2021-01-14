import pandas as pd
import glob

path = r'/home/user3/Documents/Cdac-Project/activity_csv/test'
all_files = glob.glob(path + "/*.csv")
li = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0, delim_whitespace=True, error_bad_lines=False)
    li.append(df)
    frame = pd.concat(li, axis=0, ignore_index=True)


print(li)

for i in li:
    try:
        print(i['working'])

    except KeyError:
     print(f'The price ofis not known')
