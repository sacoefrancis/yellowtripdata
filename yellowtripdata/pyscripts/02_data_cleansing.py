import pandas as pd
import os

dirName = os.path.dirname(__file__)
in_file = os.path.join(dirName,'../inputs/yellow_tripdata_2018-01.csv') 
out_file = os.path.join(dirName,'../inputs/yellow_tripdata_2018-01_cleared.csv') 

datas = pd.read_csv(in_file)

#print(datas[1:10])

datas = datas[datas['VendorID'] != '']

datas.to_csv(out_file, index=False)




