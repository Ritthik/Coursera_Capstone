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


df_latlon=pd.read_csv("http://cocl.us/Geospatial_data")
df_latlon.head()


df_merge=pd.merge(df_group,df_latlon,on="Postal Code",how="inner") #Merging this data frame to the grouped DF above


df_merge


df_merge=df_merge[df_merge.Borough.str.contains("Toronto",regex=False)] #Boroughs that include the word "Toronto"


df_merge.reset_index()


# Visualizing Toronto and the neighbourhood's locations
import folium
map_toronto = folium.Map(location=[43.651070,-79.347015],zoom_start=10)

for lat,lng,borough,neighborhood in zip(df_merge['Latitude'],df_merge['Longitude'],df_merge['Borough'],df_merge['Neighbourhood']):
    label = f'{neighborhood}, {borough}'
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
    [lat,lng],
    radius=5,
    popup=label,
    color='blue',
    fill=True,
    fill_color='#3186cc',
    fill_opacity=0.7,
    parse_html=False).add_to(map_toronto)
map_toronto


from sklearn.cluster import KMeans,AgglomerativeClustering

k=4

kmeans=KMeans(n_clusters=k,random_state=0).fit(df_merge[["Latitude","Longitude"]])
hmeans=AgglomerativeClustering(n_clusters=k).fit(df_merge[["Latitude","Longitude"]])
df_merge["Cluster (Kmeans)"]=kmeans.labels_
df_merge["Cluster (Hierarchical)"]=hmeans.labels_


import numpy as np
from matplotlib import cm, colors
# create map
map_clusters = folium.Map(location=[43.651070,-79.347015],zoom_start=10)

# set color scheme for the clusters
x = np.arange(k)
ys = [i + x + (i*x)**2 for i in range(k)]
colors_array = cm.rainbow(np.linspace(0, 1, len(ys)))
rainbow = [colors.rgb2hex(i) for i in colors_array]

# add markers to the map
markers_colors = []
for lat, lon, neighbourhood, cluster in zip(df_merge['Latitude'], df_merge['Longitude'], df_merge['Neighbourhood'], df_merge['Cluster (Kmeans)']):
    label = folium.Popup(' Cluster ' + str(cluster), parse_html=True)
    folium.CircleMarker(
        [lat, lon],
        radius=5,
        popup=label,
        color=rainbow[cluster-1],
        fill=True,
        fill_color=rainbow[cluster-1],
        fill_opacity=0.7).add_to(map_clusters)
       
map_clusters


import numpy as np
from matplotlib import cm, colors
# create map
map_clusters = folium.Map(location=[43.651070,-79.347015],zoom_start=10)

# set color scheme for the clusters
x = np.arange(k)
ys = [i + x + (i*x)**2 for i in range(k)]
colors_array = cm.rainbow(np.linspace(0, 1, len(ys)))
rainbow = [colors.rgb2hex(i) for i in colors_array]

# add markers to the map
markers_colors = []
for lat, lon, neighbourhood, cluster in zip(df_merge['Latitude'], df_merge['Longitude'], df_merge['Neighbourhood'], df_merge['Cluster (Hierarchical)']):
    label = folium.Popup(' Cluster ' + str(cluster), parse_html=True)
    folium.CircleMarker(
        [lat, lon],
        radius=5,
        popup=label,
        color=rainbow[cluster-1],
        fill=True,
        fill_color=rainbow[cluster-1],
        fill_opacity=0.7).add_to(map_clusters)
       
map_clusters


from scipy.cluster.hierarchy import dendrogram 

def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([model.children_, model.distances_,
                                      counts]).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)



# setting distance_threshold=0 ensures we compute the full tree.
model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)

model = model.fit(df_merge[["Latitude","Longitude"]])
plt.title('Hierarchical Clustering Dendrogram')
# plot the top three levels of the dendrogram
plot_dendrogram(model, truncate_mode='level', p=4) #4 clusters: cluster sizes 7, 6,3,23
plt.xlabel("Number of points in node (or index of point if no parenthesis, index is row number).")
plt.show()



