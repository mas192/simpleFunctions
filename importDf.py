# Function to import csv and json as dataframes

def importDf(filename, filepath):
    if not filename.lower().endswith('.csv') or filename.lower().endswith('.json'):
        print('Please input a csv or json file')
    if filename.lower().endswith('.csv'):
        df = pd.read_csv(filepath+'/'+filename)
        return df
    elif filename.lower().endswith('.json'):
        df = pd.read_json(filepath+'/'+filename)
        return df
            
