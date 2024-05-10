import os
import pandas as pd

def split_csv(input_file, output_folder, chunk_size):
    chunk_size *= 10**6 
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    reader = pd.read_csv(input_file, sep=';', quotechar='"', chunksize=chunk_size)
    for i, chunk in enumerate(reader):
        chunk.to_csv(os.path.join(output_folder, f"part_{i}.csv"), index=False)

input_file = 'C:\\Tomasz.Slupik\\file\\testowy.csv'
output_folder = os.path.join(os.path.expanduser('~'), 'C:\\Tomasz.Slupik\\file\\insert', 'covert')
chunk_size_gb = 1

split_csv(input_file, output_folder, chunk_size_gb)