#pip3 install folium 

import pandas as pd
df= pd.read_csv('train.csv')       #df=data frame

import folium
from folium import plugins

stationArr= df[['Y','X']].values
# print(type(stationArr))       #numpy array

m= folium.Map(location=[stationArr[0][0],stationArr[0][1]], zoom_start=12)
m.add_child(plugins.HeatMap(stationArr[:50000],radius=15))
m.save('index.html')
