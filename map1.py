import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
name = list(data["NAME"])
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
<b>Name:</b> %s
<br>
<b>Height:</b> %s m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
for lt, ln, nm, ev in zip (lat, lon, name, elev):
    iframe = folium.IFrame(html=html % (nm, ev), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color="red")))


map.add_child(fg)

map.save("Map1.html")
