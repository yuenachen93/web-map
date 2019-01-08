# use library folium
# a web map 
import folium 
import pandas


data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])


#marker color changes depends on elevation
def color_producer(el):
	if el < 1000:
		return 'green'
	elif 1000 <= el < 3000:
		return 'orange'
	else:
		return 'red'

#popup style 
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# The base map
map = folium.Map(location = [38.58, -99.09], zoom_start=6, tiles = "Mapbox Bright")
fgv = folium.FeatureGroup(name = "Volcanoes")

#add markers and popup
for lt, ln, el, name in zip(lat, lon, elev, name):
	iframe = folium.IFrame(html=html % (name, name, el), width=200, height=80)
	fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = color_producer(el))))


fgp = folium.FeatureGroup(name = "Population")
# add geojson polygon layer
fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(), 
	style_function=lambda x: {'fillColor' : 'green' if x['properties']['POP2005'] < 10000000 
	else 'orange' if  10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# use color to represent population(2005)

# lay_control
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
















