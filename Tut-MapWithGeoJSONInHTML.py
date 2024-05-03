import folium
import folium.map
json_file = "Linhas_200_milhas.geojson"
m = folium.Map()
folium.GeoJson(json_file).add_to(m)
m.save('br_map.html')
