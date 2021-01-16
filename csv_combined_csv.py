import pandas as pd
import glob

path = r'/home/user3/Documents/Cdac-Project/cancelled_class_csv'
all_files = glob.glob(path + "/*.csv")
print(all_files)

li = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0, delim_whitespace=True, error_bad_lines=False)

    print(li)
    frame = pd.concat(li, axis=0, ignore_index=True)



# print(li)
#
# for i in li:
#     try:
#         print(i['words'])
#
#     except KeyError:
#      print(f'The price ofis not known')
