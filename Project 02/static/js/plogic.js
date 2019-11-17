var ds = [];
var bi = [];
var mls = [];

var url = "http://127.0.0.1:5000/ds";

d3.json(url, function(data) {
    
    for (var i=0; i < data.result.length; i++) {
        var location = [data.result[i].city_Coordinates[0], data.result[i].city_Coordinates[1]];
        var category = data.result[i].Category;
        var cityState = data.result[i].Location;

            if (category === "Data Science") {
                ds.push(
                    L.marker(location, {draggable:'true'}).bindPopup("<h5>" + cityState + "</h5>")
                );       
            }     
            else if (category === "Business Intelligence") {
                bi.push(
                    L.marker(location, {draggable:'true'}).bindPopup("<h5>" + cityState + "</h5>")
                );
            }
            else {mls.push(
                L.marker(location, {draggable:'true'}).bindPopup("<h5>" + cityState + "</h5>")
                 );
            }

            // if (category === "Data Science") {
            //     ds.push(location);     
            // }     
            // else if (category === "Business Intelligence") {
            //     bi.push(location);
            // }
            // else {mls.push(location);
            // }
        }
        

var dsLayer = L.layerGroup(ds);
var biLayer = L.layerGroup(bi);
var mlsLayer = L.layerGroup(mls);

// var dsLayer = L.heatLayer(ds, {
//     radius: 50,
//     max: 1.5,
//     maxOpacity: 0.1,
//     minOpacity: 0,
//     fillColor: "red",
//     blur: 1,
//     density: 80
// });

// var biLayer = L.heatLayer(bi, {
//     radius: 20,
//     blur: 0
// });

// var mlsLayer = L.heatLayer(mls, {
//     radius: 20,
//     blur: 0
// });


var light = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.streets",
      accessToken: "pk.eyJ1IjoiZWxsaW90cGFyazE5OTUiLCJhIjoiY2syYjE1b2x4MzVzajNkcWM4emNpNmU4bSJ9.zKpnpfGCfjfINMRlP0UBPg"
    });

var dark = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.dark",
    accessToken: "pk.eyJ1IjoiZWxsaW90cGFyazE5OTUiLCJhIjoiY2syYjE1b2x4MzVzajNkcWM4emNpNmU4bSJ9.zKpnpfGCfjfINMRlP0UBPg"
    });    

var overlayMaps = {
    Data_Science: dsLayer,
    Business_Intelligence: biLayer,
    Machine_Learning_Science: mlsLayer
};

var baseMaps = {
    Light: light,
    Dark: dark
};

var myMap = L.map("map", {
    center: [37.0902, -95.7129],
    zoom: 3.5,
    layers: [light, dsLayer]
  });

L.control.layers(baseMaps, overlayMaps).addTo(myMap);

console.log(ds);
console.log(bi);
console.log(mls);

});
