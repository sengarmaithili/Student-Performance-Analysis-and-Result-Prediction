import pandas as pd
import glob

def activity_csv():
    pathname = '/home/user3/Documents/Cdac-Project/Activity/*.json'
    list_of_paths_to_files = glob.glob(pathname)
    # print(list_of_paths_to_files)
    # [print(i) for i in list_of_paths_to_files]
    for i in list_of_paths_to_files:
        print(i)
        df = pd.read_json(i)
        df.to_csv(f'/home/user3/Documents/Cdac-Project/activity_csv/activity_{i[-8:-5]}.csv', index=None,header=True)

activity_csv()

def behaviour_csv():
    pathname = '/home/user3/Documents/Cdac-Project/Behavior/*.json'
    list_of_paths_to_files = glob.glob(pathname)
    # print(list_of_paths_to_files)
    # [print(i) for i in list_of_paths_to_files]
    for i in list_of_paths_to_files:
        df = pd.read_json(i)
        df.to_csv(f'/home/user3/Documents/Cdac-Project/behavior_csv/behavior_{i[-8:-5]}.csv', index=None,
                  header=True)

behaviour_csv()

def social_csv():
    pathname = '/home/user3/Documents/Cdac-Project/Social/*.json'
    list_of_paths_to_files = glob.glob(pathname)
    # print(list_of_paths_to_files)
    # [print(i) for i in list_of_paths_to_files]
    for i in list_of_paths_to_files:
        df = pd.read_json(i)
        df.to_csv(f'/home/user3/Documents/Cdac-Project/social_csv/social_{i[-8:-5]}.csv', index=None,
                  header=True)
social_csv()

def class_csv():
    pathname = '/home/user3/Documents/Cdac-Project/Class/*.json'
    list_of_paths_to_files = glob.glob(pathname)
    # print(list_of_paths_to_files)
    # [print(i) for i in list_of_paths_to_files]
    for i in list_of_paths_to_files:
        df = pd.read_json(i)
        df.to_csv(f'/home/user3/Documents/Cdac-Project/class_csv/class_{i[-8:-5]}.csv', index=None,
                  header=True)
class_csv()

def stress_csv():
    pathname = '/home/user3/Documents/Cdac-Project/Stress/*.json'
    list_of_paths_to_files = glob.glob(pathname)
    # print(list_of_paths_to_files)
    # [print(i) for i in list_of_paths_to_files]
    for i in list_of_paths_to_files:
        df = pd.read_json(i)
        df.to_csv(f'/home/user3/Documents/Cdac-Project/stress_csv/stress_{i[-8:-5]}.csv', index=None,
                  header=True)
stress_csv()

def sleep_csv():
    pathname = '/home/sunbeam/Downloads/Project/dataset/dataset/EMA/response/Sleep/*.json'
    list_of_paths_to_files = glob.glob(pathname)
    # print(list_of_paths_to_files)
    # [print(i) for i in list_of_paths_to_files]
    for i in list_of_paths_to_files:
        df = pd.read_json(i)
        df.to_csv(f'/home/sunbeam/Downloads/Project/dataset/sleep_csv/sleep_{i[-8:-5]}.csv', index=None,
                  header=True)
sleep_csv()

def exercise_csv():
    pathname = '/home/user3/Documents/Cdac-Project/Exercise/*.json'
    list_of_paths_to_files = glob.glob(pathname)
    # print(list_of_paths_to_files)
    # [print(i) for i in list_of_paths_to_files]
    for i in list_of_paths_to_files:
        df = pd.read_json(i)
        df.to_csv(f'/home/user3/Documents/Cdac-Project/exercise_csv/exercise_{i[-8:-5]}.csv', index=None,
                  header=True)
exercise_csv()

def study_space_csv():
    pathname = '/home/user3/Documents/Cdac-Project/Study Spaces/*.json'
    list_of_paths_to_files = glob.glob(pathname)
    # print(list_of_paths_to_files)
    # [print(i) for i in list_of_paths_to_files]
    for i in list_of_paths_to_files:
        df = pd.read_json(i)
        df.to_csv(f'/home/user3/Documents/Cdac-Project/study_space_csv/study_space_{i[-8:-5]}.csv', index=None,
                  header=True)
study_space_csv()

def lab_csv():
    pathname = '/home/user3/Documents/Cdac-Project/Lab/*.json'
    list_of_paths_to_files = glob.glob(pathname)
    # print(list_of_paths_to_files)
    # [print(i) for i in list_of_paths_to_files]
    for i in list_of_paths_to_files:
        df = pd.read_json(i)
        df.to_csv(f'/home/user3/Documents/Cdac-Project/lab_csv/lab_{i[-8:-5]}.csv', index=None,
                  header=True)
lab_csv()

def cancelled_classes_csv():
    pathname = '/home/user3/Documents/Cdac-Project/Cancelled Classes/*.json'
    list_of_paths_to_files = glob.glob(pathname)
    # print(list_of_paths_to_files)
    # [print(i) for i in list_of_paths_to_files]
    for i in list_of_paths_to_files:
        df = pd.read_json(i)
        df.to_csv(f'/home/user3/Documents/Cdac-Project/cancelled_class_csv/cancelled_classes_{i[-8:-5]}.csv', index=None,
                  header=True)

cancelled_classes_csv()

def class2_csv():
    pathname = '/home/user3/Documents/Cdac-Project/Class 2/*.json'
    list_of_paths_to_files = glob.glob(pathname)
    # print(list_of_paths_to_files)
    # [print(i) for i in list_of_paths_to_files]
    for i in list_of_paths_to_files:
        df = pd.read_json(i)
        df.to_csv(f'/home/user3/Documents/Cdac-Project/class2_csv/class2_{i[-8:-5]}.csv', index=None,
                  header=True)
class2_csv()

def qr_code_csv():
    pathname = '/home/user3/Documents/Cdac-Project/QR_Code/*.json'
    list_of_paths_to_files = glob.glob(pathname)
    # print(list_of_paths_to_files)
    # [print(i) for i in list_of_paths_to_files]
    for i in list_of_paths_to_files:
        df = pd.read_json(i)
        df.to_csv(f'/home/user3/Documents/Cdac-Project/qr_code_csv/qr_code_{i[-8:-5]}.csv', index=None,
                  header=True)

qr_code_csv()