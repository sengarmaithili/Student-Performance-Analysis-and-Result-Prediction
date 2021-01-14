import os
import glob
import pandas as pd



pathname = '/home/user3/Documents/Cdac-Project/activity_csv/*.csv'
list_of_paths_to_files = glob.glob(pathname)
print(list_of_paths_to_files)
for i in list_of_paths_to_files:

