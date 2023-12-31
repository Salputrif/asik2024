from flask import Flask
import folium
from flask import render_template
import os
from folium import plugins
import pickle



app = Flask(__name__)
model= pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():

    return render_template('home.html')

@app.route('/map', methods=['GET'])
def tracking():

    basemaps={
        'Google Satellite Hybrid':folium.TileLayer(
            tiles='https:mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
            attr='Google',
            name='Google Satellite',
            overlay=True,
            control=True
        ),
    }
    d = os.path.dirname(os.path.abspath(__file__))
    start_coords = (-8.103, 110.431)
    wpp = "WPP 573"
    folium_map = folium.Map(location=start_coords, zoom_start=8)
    for basemap, tilelyr in basemaps.items():
        basemaps[basemap].add_to(folium_map)
    
    folium.LayerControl().add_to(folium_map)
    #fungsi mouse
    fmtr="function(num) {return L.Util.formation(num, 3) + '&deg;';};"
    plugins.MousePosition(position='topright', separator='|', lat_formatter=fmtr, lng_formatter=fmtr).add_to(folium_map)
    folium_map.add_child(folium.LatLngPopup())
    
    folium.Marker(location=[-9.0198,121.3718],
                  popup="Koordinat: (-13.87074806,1119.9915814)        SPL:28.4142    |   CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.0185,124.7076],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[-9.1920,124.5538],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.2137,123.4555],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -9.1703,117.4845],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -9.1775,118.2319],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.1558,117.7927],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -8.6568,115.8162],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.5912,124.6001],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.8410,122.0907],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.1827,121.8107],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -8.9273,120.3783],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    
    folium.Marker(location=[  -8.4823,119.8512],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    
    folium.Marker(location=[ -8.5691, 119.7963],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    
    folium.Marker(location=[ -8.5366, 119.6426],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -8.5798, 119.4756],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.6232, 119.4097],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.6558, 119.5305],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.0139, 119.1901],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.6558, 119.5305],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.0139, 119.1901],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.6558, 119.5305],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.0139, 119.1901],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.6558, 119.5305],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.0139, 119.1901],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.6558, 119.5305],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.0139, 119.1901],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.6558, 119.5305],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.0139, 119.1901],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.6558, 119.5305],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.0139, 119.1901],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.6558, 119.5305],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.0139, 119.1901],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.6558, 119.5305],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.0139, 119.1901],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.6558, 119.5305],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.0139, 119.1901],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.6558, 119.5305],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.0139, 119.1901],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.6558, 119.5305],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.0139, 119.1901],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.6558, 119.5305],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.0139, 119.1901],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.6558, 119.5305],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.0139, 119.1901],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='green',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)

    folium.Marker(location=[ -8.7437,113.0491],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='red',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.4159, 112.8515],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='red',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.5700,113.2907],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='red',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[   -8.4598,112.5850],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='red',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.3403,112.0469],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='red',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[  -8.5793,110.3230],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='red',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.4252,111.6406],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='red',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)
    folium.Marker(location=[ -9.5660,113.0571],
                  popup="Koordinat: (-13.87074806,1119.9915814),SPL:28.4142, CHL:0.149617",
                  tooltip="See the details",
                  icon=folium.Icon(color='red',icon_color='yellow',icon='ship'),
                  draggable=True).add_to(folium_map)

    
    folium_map.save(d+'/templates/map.html')
    return render_template('index.html', koordinat = start_coords, wpp = wpp)
@app.route('/information')
def information():

    return render_template('information.html')

if __name__ == '__main__':
    app.run()