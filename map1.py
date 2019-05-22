import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
name = list(data["NAME"])

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
for lt, ln, nm in zip (lat, lon, name):
    fg.add_child(folium.Marker(location=[lt, ln], popup=nm, icon=folium.Icon(color="pink")))


map.add_child(fg)

map.save("Map1.html")
