import folium
map = folium.Map(location=[64.14, -21.94], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
for coordinates in [[64.14, -21.93], [64.34, -21.73], [64.54, -21.53], [64.74, -21.33]]:
    fg.add_child(folium.Marker(location=coordinates, popup="I am a Marker", icon=folium.Icon(color="pink")))

map.add_child(fg)

map.save("Map1.html")
