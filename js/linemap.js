// Load json data
d3.json("Resources/national.json").then(function(rates) {
  console.log(rates);
  // convert dict to list
  Year = [];
  Mrate = [];
  Drate = [];
  for (var i = 0; i < rates.length; i++ ) {
            Year.push(rates[i].Year);
            Mrate.push(rates[i].Marriage_Rate)
            Drate.push(rates[i].Divorce_Rate)
        }
  console.log(Year);
// define X & Y axsis
  var trace1 = {
    x: Year,
    y: Mrate,
    mode: 'lines+markers',
    name: 'Marriage Rate'
  }; 
  var trace2 = {
    x: Year,
    y: Drate,
    mode: 'lines+markers',
    name: 'Divorce Rate'
  };
  var data = [trace1, trace2];
  var layout = {
    title: 'Marriage Vs Divorce Rate',
    xaxis: {
      title: 'Year'
    },
    yaxis: {
      title: 'Rates'
    }
  };
 //Map 
  Plotly.newPlot('line', data, layout);
}).catch(function(error) {
  console.log(error);
});