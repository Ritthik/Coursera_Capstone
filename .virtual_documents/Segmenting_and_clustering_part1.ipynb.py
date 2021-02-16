from bs4 import BeautifulSoup # assumed bs4, requests and pandas have been installed using conda for example


import requests
source_file=requests.get("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M").text
soup = BeautifulSoup(source_file, 'html.parser')


#print(soup.title,'\n') #print statements to check the webpage, commented to avoid pasting on github
#print(soup.prettify())


from IPython.display import display_html
table = str(soup.table)
display_html(table,raw=True) #since it is a small table, displaying it


import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)
df=pd.read_html(table)


df=df[0] #first element of the list df is the dataframe


df=df[df.Boroughget_ipython().getoutput("="Not assigned"] # Removing not assigned boroughs")


df_group=df.groupby("Postal Code",sort=False).agg(",".join) # Grouped by Postal Code
df_group.reset_index(inplace=True)
df_group


df_group[df_group["Neighbourhood"]=="Not assigned"].Neighbourhood=df_group[df_group["Neighbourhood"]=="Not assigned"].Borough #Not applicable for this dataset


df_group.shape



