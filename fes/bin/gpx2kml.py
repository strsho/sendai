import xml.etree.ElementTree as et
import os
import glob
from geopy.distance import geodesic
import datetime

ns = {'kml': 'http://www.opengis.net/kml/2.2'}
nsg = {'gpx': 'http://www.topografix.com/GPX/1/1'}
et.register_namespace('', 'http://www.opengis.net/kml/2.2')
et.register_namespace('atom', 'http://www.w3.org/2005/Atom')

def velocity(lon, lat, lon2, lat2, tm, tm2):
    if tm == None or tm2 == None:
        return 0
    d = geodesic((lat, lon), (lat2, lon2)).m
    dt = datetime.datetime.strptime(tm, '%Y-%m-%dT%H:%M:%SZ')
    dt2 = datetime.datetime.strptime(tm2, '%Y-%m-%dT%H:%M:%SZ')
    dts = (dt2 - dt).total_seconds()
    v = int((d / dts)*60)
    vlevel = 0
    if v < 10:
        vlevel = 0
    elif v < 30:
        vlevel = 1
    elif v < 50:
        vlevel = 2
    elif v < 70:
        vlevel = 3
    elif v < 100:
        vlevel = 4
    elif v < 200:
        vlecel = 5
    elif v < 400:
        vlevel = 6
    elif v >= 400:
        vlevel = 7

    print((d, v, vlevel))
    return vlevel 


def mk(f, f_out):
    dom = et.parse('templates/template.kml')
    root = dom.getroot()
    doc = root.find('./*')
    dom_in = et.parse(f)
    root_in = dom_in.getroot()
    pm = None 
    cn = None
    lon_bak = -1
    lat_bak = -1
    v_bak = -1
    tm_bak = None
    for pt in root_in.findall('./*/*/gpx:trkpt', nsg):
        lat = float(pt.get('lat'))
        lon = float(pt.get('lon'))
        tm = pt.find('./gpx:time', nsg).text
        v = 0 
        if lon_bak > -1:
            v = velocity(lon_bak, lat_bak, lon, lat, tm_bak, tm)
        if pm == None or (v_bak > -1 and v != v_bak):
            if pm == None or v != v_bak:
                pm = et.SubElement(doc, 'Placemark')
                su = et.SubElement(pm, 'styleUrl')
                su.text = '#h' + str(v)
                ls = et.SubElement(doc, 'LineString')
                cn = et.SubElement(ls, 'coordinates')
                cn.text = ''
        cn.text = cn.text + str(lon) + ',' + str(lat) + '\n'
        lon_bak = lon
        lat_bak = lat
        v_bak = v
        tm_bak = tm
        print((lon, lat, v, tm))

        
    tree = et.ElementTree(root)
    tree.write(f_out, encoding="utf-8", xml_declaration=True)

if os.path.isdir('out'):
    pass
else:
    os.makedirs('out')

fs = glob.glob('in/*.gpx')
for f in fs:
    fout = f.replace('in/', 'out/').replace('.gpx', '.kml')
    mk(f, fout)












