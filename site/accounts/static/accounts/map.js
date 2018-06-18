function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: {
            lat: 50.436,
            lng: 30.521
        }
    });
    // Create an array of alphabetical characters used to label the markers.
    var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    // Add some markers to the map.
    // Note: The code uses the JavaScript Array.prototype.map() method to
    // create an array of markers based on a given "locations" array.
    // The map() method here has nothing to do with the Google Maps API.
    var markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });
    // Add a marker clusterer to manage the markers.
    var markerCluster = new MarkerClusterer(map, markers, {
        imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'
    });
}

var locations = [{
    lat: 50.436,
    lng: 30.521
}, {
    lat: 50.718234,
    lng: 30.363181
}, {
    lat: 50.527111,
    lng: 30.571124
}, {
    lat: 50.848588,
    lng: 31.209834
}, {
    lat: 50.851702,
    lng: 31.216968
}, {
    lat: 50.671264,
    lng: 30.863657
}, {
    lat: 50.304724,
    lng: 30.662905
}, {
    lat: 50.817685,
    lng: 30.699196
}, {
    lat: 50.828611,
    lng: 30.790222
}, {
    lat: 50.750000,
    lng: 30.116667
}, {
    lat: 50.759859,
    lng: 30.128708
}, {
    lat: 50.765015,
    lng: 30.133858
}, {
    lat: 50.770104,
    lng: 30.143299
}, {
    lat: 50.773700,
    lng: 30.145187
}, {
    lat: 50.774785,
    lng: 30.137978
}, {
    lat: -37.819616,
    lng: 144.968119
}, {
    lat: -38.330766,
    lng: 144.695692
}, {
    lat: -39.927193,
    lng: 175.053218
}, {
    lat: -41.330162,
    lng: 174.865694
}, {
    lat: -42.734358,
    lng: 147.439506
}, {
    lat: -42.734358,
    lng: 147.501315
}, {
    lat: -42.735258,
    lng: 147.438000
}, {
    lat: -43.999792,
    lng: 170.463352
}]