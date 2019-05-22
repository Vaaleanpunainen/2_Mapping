import folium
map = folium.Map(location=[64.14, -21.94], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[64.14, -21.93], popup="I am a Marker", icon=folium.Icon(color="pink")))
map.add_child(fg)

map.save("Map1.html")
