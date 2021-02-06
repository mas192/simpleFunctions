import glob
import os
# a function to find all csv in a director and make a list

def csv_lst():
    csv_lst = []
    os.chdir('./')
    for file in glob.glob('*.csv'):
        df = pd.read_csv(file)
        csv_lst.append(df)
    return csv_lst
