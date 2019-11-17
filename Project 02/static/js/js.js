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
