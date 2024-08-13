
// Create a map object
let myMap = L.map("map", { center: [0, 0], zoom: 2 });

// Add a tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

// Fetch the JSON data
const URL = "storms_final.json";

d3.json(URL).then(function (data) {
  // Function to plot markers based on filtered data
  function plotMarkers(filteredData) {
    filteredData.forEach(function (storms_final) {
      let location = [storms_final.lat, storms_final.long];
      let popupText = `<h1>${storms_final.name}</h1> <hr> <h3>Category: ${storms_final.category}</h3>`;
      L.marker(location).bindPopup(popupText).addTo(myMap);
    });
  }

  let years = Array.from({ length: 75 }, (_, i) => (1950 + i).toString())

  const selectedYear = this.value;

  // Filter data based on the selected year and category 1 and above
  var filteredData = data.filter(function (storms_final) {
    return storms_final.category >= "1";
  });

  // Create custom control
  L.Control.YearSelector = L.Control.extend({
    onAdd: function (map) {
      var div = L.DomUtil.create('div', 'leaflet-control leaflet-bar');
      var select = L.DomUtil.create('select', 'year-selector', div);

      years.forEach(year => {
        var option = L.DomUtil.create('option', '', select);
        option.value = year;
        option.innerHTML = year;
      });

      L.DomEvent.on(select, 'change', function () {
        var year = this.value;
        filterByYear(year);
      });

      return div;
    }
  });

  // Add the control to the map
  myMap.addControl(new L.Control.YearSelector({ position: 'topright' }));

  // Filter function (you'll need to adapt this to your specific use case)
  function filterByYear(year) {
    console.log(year)
    // Clear existing markers on the map
    myMap.eachLayer(function(layer) {
    if (layer instanceof L.Marker) {
    myMap.removeLayer(layer);
    }
    });
    let filteredDataByYear = filteredData.filter((stormData) => stormData.year == year)
    console.log(filteredDataByYear)
    plotMarkers(filteredDataByYear);
  }
});