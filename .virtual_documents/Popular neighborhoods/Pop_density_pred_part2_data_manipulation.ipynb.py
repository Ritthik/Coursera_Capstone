import pandas as pd


df=pd.read_pickle("./df_merge_withPop_with_FScategories")


df.head()


import numpy as np


# Mean latitude of downtown Boroughs
lat_m=np.mean(df[df.Borough=="Downtown Toronto"].Latitude)
# Mean longitude of downtown Boroughs
lon_m=np.mean(df[df.Borough=="Downtown Toronto"].Longitude)

#distance between two latitudes is ~111 km and between two longitudes at this range of latitude is ~ 80 km
df["Distance_to_Downtown [Km]"]=np.sqrt((((df["Latitude"]-lat_m)*111)**2)+(((df["Longitude"]-lon_m)*80)**2))


df=df.drop(["Borough","Neighbourhood","Latitude","Longitude","Place categories"],axis=1)


df=df.drop(["College","Events","Nightlife"],axis=1)


df["Ratio_commuting"]=df["Commuting"]/(100*df["Population"])
df["Ratio_renting"]=df["Renting"]/(100*df["Population"])
df=df.drop(["Commuting","Renting"],axis=1)


df


df["Average_income"]=df["Total income"]/df["Population"]
df["Population_density"]=df["Population"]/df["Area"]
df["Population_change_ratio"]=df["Population Change"]/(df["Population"]-df["Population Change"])


df=df.drop(["Total income"],axis=1)


df=df.set_index("Postal Code")


for col in ['Travel', 'Outdoors', 'Food','Arts', 'Shops', 'Residence', 'Professional']:
    df[col]= df[col]/df["Area"]


df.to_pickle("./df_analysis_part1") #Not yet standardized


df=pd.read_pickle("./df_analysis_part1")


df






