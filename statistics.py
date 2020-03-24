import pandas as pd
from collections import defaultdict
raw_data=pd.read_csv("data_op.csv")
locations=raw_data['location']
city_dict=defaultdict(int)
state_dict=defaultdict(int)
country_dict=defaultdict(int)
#print(locations)
for i in raw_data.index:
    #print(raw_data['location'][i])
    csc=raw_data['location'][i].split(',')
    city=csc[0]
    state=csc[1]
    country=csc[2]

    city_dict[city]+=1
    state_dict[state]+=1
    country_dict[country]+=1
#print(city_dict,state_dict,country_dict)
print(city_dict,state_dict,country_dict)
