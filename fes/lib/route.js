
const style = {
  'Point': new ol.style.Style({
    image: new ol.style.Circle({
      fill: new ol.style.Fill({
        color: 'rgba(255,255,0,0.4)',
      }),
      radius: 5,
      stroke: new ol.style.Stroke({
        color: '#ff0',
        width: 1,
      }),
    }),
  }),
  'LineString': new ol.style.Style({
    stroke: new ol.style.Stroke({
      color: '#f00',
      width: 3,
    }),
  }),
  'MultiLineString': new ol.style.Style({
    stroke: new ol.style.Stroke({
      color: '#0f0',
      width: 3,
    }),
  }),
};

const vector = new ol.layer.Vector({
  source: new ol.source.Vector({
    url: 'data/rk1.gpx',
    format: new ol.format.GPX(),
  }),
  style: function (feature) {
    return style[feature.getGeometry().getType()];
  },
});


const map = new ol.Map({
  layers: [
    new ol.layer.Tile({
      source: new ol.source.OSM(),
    }),
    vector
  ],
  target: 'map',
  view: new ol.View({
    center: ol.proj.fromLonLat([139.618, 35.412]),
    zoom: 13,
  }),
});

document.getElementById('zoom-out').onclick = function () {
  const view = map.getView();
  const zoom = view.getZoom();
  view.setZoom(zoom - 1);
};

document.getElementById('zoom-in').onclick = function () {
  const view = map.getView();
  const zoom = view.getZoom();
  view.setZoom(zoom + 1);
};


