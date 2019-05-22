import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
name = list(data["NAME"])
elev = list(data["ELEV"])



def marker_color(elevation):
    if elevation < 1000:
        return "blue"
    elif elevation > 4000:
        return "red"
    elif elevation > 2000:
        return "orange"
    elif elevation > 1000:
        return "green"


html = """<h4>Volcano information:</h4>
<b>Name:</b> %s
<br>
<b>Height:</b> %s m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fg_volcanoes = folium.FeatureGroup(name="American volcanoes map")
fg_population = folium.FeatureGroup(name="World population map")

for lt, ln, nm, ev in zip (lat, lon, name, elev):
    iframe = folium.IFrame(html=html % (nm, ev), width=200, height=100)

    fg_volcanoes.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=folium.Popup(iframe),
    fill_color=marker_color(ev), color="black", fill_opacity=0.7))

fg_population.add_child(folium.GeoJson(data=(open("world.json", "r", encoding="utf-8-sig").read()),
style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))

map.add_child(fg_volcanoes)
map.add_child(fg_population)

map.add_child(folium.LayerControl())

map.save("Map1.html")
