import folium
import folium.map
json_file = "filename.geojson"
m = folium.Map()
folium.GeoJson(json_file).add_to(m)
m.save('filename.html')
