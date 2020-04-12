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
    type: 'bar',
    name: 'Marriage Rate'
  }; 
  var trace2 = {
    x: Year,
    y: Drate,
    type: 'bar',
    name: 'Divorce Rate'
  };
  var data = [trace1, trace2];
  var layout = {
    title: 'Year',
    xaxis: {tickfont: {
        size: 14,
        color: 'rgb(107, 107, 107)'
      }},
    yaxis: {
      title: 'Rates',
      titlefont: {
        size: 16,
        color: 'rgb(107, 107, 107)'
      },
      tickfont: {
        size: 14,
        color: 'rgb(107, 107, 107)'
      }
    },
    legend: {
      x: 0,
      y: 1.0,
      bgcolor: 'rgba(255, 255, 255, 0)',
      bordercolor: 'rgba(255, 255, 255, 0)'
    },
    barmode: 'group',
    bargap: 0.15,
    bargroupgap: 0.1,
    title: 'Marriage Vs Divorce'
    // ,margin=dict(l=50,r=50,b=100,t=100,pad=4)
  };
 //Map 
  Plotly.newPlot('bar', data, layout);
}).catch(function(error) {
  console.log(error);
});