import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
name = list(data["NAME"])

html = """<h4>Volcano name:</h4>
%s
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
for lt, ln, nm in zip (lat, lon, name):
    iframe = folium.IFrame(html=html % nm, width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color="red")))


map.add_child(fg)

map.save("Map1.html")
