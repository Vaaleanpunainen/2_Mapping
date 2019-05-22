import folium
map = folium.Map(location=[64.14, -21.94], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[64.14, -21.93], popup="I am a Marker-kun", icon=folium.Icon(color="pink")))
fg.add_child(folium.Marker(location=[64.34, -21.73], popup="I am a Marker-chan", icon=folium.Icon(color="pink")))
fg.add_child(folium.Marker(location=[64.54, -21.53], popup="I am a Marker-san", icon=folium.Icon(color="pink")))
fg.add_child(folium.Marker(location=[64.74, -21.33], popup="I am a Marker-sama", icon=folium.Icon(color="pink")))
map.add_child(fg)

map.save("Map1.html")
