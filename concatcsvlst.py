# a function concat all csv into a dataframe
def concat_csv_lst(csv_lst):
    df = pd.concat(csv_lst, axis=0)
    return df
