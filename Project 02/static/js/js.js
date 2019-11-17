var url = "http://127.0.0.1:5000/roles";


let countObj = {};
let countFunc = keys => {
    countObj[keys] = ++countObj[keys] || 1;
  };

var xx = [];
var yy = [];
var cate = [];
var splity = [];

d3.json(url).then(function(data) {
    data.result.forEach(datax => {
        cate.push(datax.Category);
        var sp = datax.Posting_Date.split('');
        splity.push(sp[1]);
    });
   cate.forEach(countFunc);
   for (var i in countObj) {
        xx.push(i);
        yy.push(countObj[i]);

    var trace1 = {
        x: yy,
        y: xx,
        // text: data.map(row => row.greekName),
        // name: "Greek",
        type: "bar",
        orientation: "h"
        };    
    var data = [trace1];

    var layout = {
        title: "# Open Roles/Category",
        xaxis: { title: "Categories" },
        yaxis: { title: "# Open Roles" }
      };
      
      // Plot the chart to a div tag with id "bar-plot"
    Plotly.newPlot("bar-plot", data, layout);
   
        };
   
});


  


// result = {};
// for(var i = 0; i < cate.length; ++i) {
//     if(!result[cate[i]])
//         result[cate[i]] = 0;
//     ++result[cate[i]];
// };


// const uniqueValues = new Set([1,2,2,2,3,4,5,8,7,8]);









// // Create a map object
// var myMap = L.map("map", {
//     center: [37.09, -95.71],
//     zoom: 5
//   });

//   console.log("holaaaa" +myMap);
  
//   L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
//     attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
//     maxZoom: 18,
//     id: "mapbox.streets-basic",
//     accessToken: "pk.eyJ1IjoiYWxlam9lcyIsImEiOiJjazJ5M3lvdngwNDV4M21xcDRtdzBmbTNpIn0.FKFq8rnzYo40t98QALeL3w"
//   }).addTo(myMap);
  
  
//   // Loop through the cities array and create one marker for each city object
//   for (var i = 0; i < full_D.length; i++) {
//     L.circle(full_D[i].city_Coordinates, {
//       fillOpacity: 0.75,
//       color: "white",
//       fillColor: "purple",
//       // Setting our circle's radius equal to the output of our markerSize function
//       // This will make our marker's size proportionate to its population
//       radius: markerSize(cities[i].population)
//     }).bindPopup("<h1>" + full_D[i].Location + "</h1> <hr> <h3>Population: " + "</h3>").addTo(myMap);
//   };