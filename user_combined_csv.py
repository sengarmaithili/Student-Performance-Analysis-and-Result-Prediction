import csv


import pandas as pd
import glob
pathname = '/home/user3/Documents/Cdac-Project/cancelled_class_csv/*.csv'
list_of_paths_to_files = glob.glob(pathname)
with open("/home/user3/Documents/Cdac-Project/combine_csv/combined_csv.csv", "a", newline="") as file:
    ss = csv.writer(file)
    s = csv.DictWriter(file,delimiter=',',fieldnames=['id','words'])

    for i in list_of_paths_to_files:
            df = pd.read_csv(i)
            try:
                # print(f"{df['working'].mean().round()}+{df['relaxing'].mean().round()}+{df['other_working'].mean().round()}+{df['other_relaxing'].mean().round()}")
                print()
                # s.writerow([i[-8:-5],df['working'].mean().round(),df['relaxing'].mean().round(),df['other_working'].mean().round(),df['other_relaxing'].mean().round()])
                ss.writerow([i[-7:-4],df['words']])
            except KeyError:
                print(f'The price ofis not known')