import xml.etree.ElementTree as et
import os
import glob
import copy

ns = {'kml': 'http://www.opengis.net/kml/2.2'}
nsg = {'gpx': 'http://www.topografix.com/GPX/1/1'}

def mk(f, f_out):
    dom = et.parse('templates/template.kml')
    root = dom.getroot()
    doc = root.find('./*')
    dom_in = et.parse(f)
    root_in = dom_in.getroot()
    pm = None 
    cn = None
    for pt in root_in.findall('./*/*/gpx:trkpt', nsg):
        if pm == None:
            pm = et.SubElement(doc, 'Placemark')
            su = et.SubElement(pm, 'styleURL')
            su.text = '#h0'
            ls = et.SubElement(pm, 'LineString')
            cn = et.SubElement(ls, 'coordinates')
            cn.text = ''
        lat = pt.get('lat')
        lon = pt.get('lon')
        cn.text = cn.text + lon + ',' + lat + '\n'
        
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












