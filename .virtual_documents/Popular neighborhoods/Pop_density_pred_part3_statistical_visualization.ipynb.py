import pandas as pd


df=pd.read_pickle("./df_analysis_part1")


df.columns


df


from sklearn import preprocessing


X=df.values


X_scaled = preprocessing.StandardScaler().fit_transform(X)


df_scaled = pd.DataFrame(X_scaled,columns=['Population', 'Area', 'Population Change','Travel', 'Outdoors', 'Food', 'Arts', 'Shops', 'Residence',
       'Professional', 'Distance_to_Downtown [Km]', 'Ratio_commuting',
       'Ratio_renting', 'Average_income', 'Population_density',
       'Population_change_ratio'])


import seaborn as sns
sns.pairplot(df[['Travel', 'Outdoors', 'Food', 'Arts', 'Shops', 'Residence',
       'Professional', 'Distance_to_Downtown [Km]', 'Ratio_commuting',
       'Ratio_renting', 'Average_income', 'Population_density',
       'Population_change_ratio']])


df.corr()["Population_density"][3:]


df_scaled.corr()["Population_density"][3:]


df_scaled.to_pickle("./df_analysis_scaled")


df_scaled.describe()
