
const vector = new ol.layer.Vector({
  source: new ol.source.Vector({
    url: 'data/rk1.gpx',
    format: new ol.format.GPX(),
  }),
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
    zoom: 32,
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


