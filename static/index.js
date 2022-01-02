let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: {lat: -25.363, lng: 131.044 },
    zoom: 8,
  });

  new google.maps.Marker({
    position:  {lat: -25.373, lng: 131.044 },
    map,
    title: "Hello World!",
  });

  const script = document.createElement("script");
	script.src =
          "https://developers.google.com/maps/documentation/javascript/examples/json/earthquake_GeoJSONP.js";
        document.getElementsByTagName("head")[0].appendChild(script);	
}
// Loop through the results array and place a marker for each
// set of coordinates.
const eqfeed_callback = function (results) {
  for (let i = 0; i < results.features.length; i++) {
    const coords = results.features[i].geometry.coordinates;
    const latLng = new google.maps.LatLng(coords[1], coords[0]);
    new google.maps.Marker({
      position: latLng,
      map: map,
    });
  }
};