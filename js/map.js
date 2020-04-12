function myFunction(browser) {

var button = d3.select("#filter-btn");

button.on("click", function() {
    
var inputElement_date = d3.select("#Year");
// Get the value property of the input element
// console.log(inputElement_date.property("value"));
// var str_append="Year_"
var inputValue_date = inputElement_date.property("value");
var file_name=browser;
main(inputValue_date,file_name)
})};
function main(inputValue_date,file_name){
// console.log(inputValue_date);
var width = 800;
    height = 700;

var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-5, 0])
  .html(function(d) {
    var dataRow = countryById.get(d.properties.name);
       if (dataRow) {
        //    console.log(dataRow);
           return dataRow.state + ": " + dataRow.dataYear;
       } else {
           console.log("no dataRow", d);
           return d.properties.name + ": No data.";
       }
  })

d3.select("#vis").select("svg").remove();
var svg = d3.select('#vis').append('svg')
    .attr('width', width)
    .attr('height', height);

svg.call(tip);

var projection = d3.geo.albersUsa()
    .scale(900) // mess with this if you want
    .translate([width / 2, height / 2]);

var path = d3.geo.path()
    .projection(projection);

var colorScale = d3.scale.linear().range(["#D4EEFF", "#1009FF"]).interpolate(d3.interpolateLab);

var countryById = d3.map();

// we use queue because we have 2 data files to load.
queue()
    .defer(d3.json, "Resources/USA.json")
    .defer(d3.json, file_name) // process
    .await(loaded);

function getColor(d) {
    var dataRow = countryById.get(d.properties.name);
    // console.log(dataRow);
    if (dataRow) {
        console.log(colorScale(dataRow.dataYear));
        return colorScale(dataRow.dataYear);
    } else {
        // alert("No Data");
        // console.log("no dataRow", d);
        return "#ccc";

    }
}


function loaded(error, usa, un) {

if (error) throw error;


  un.forEach(function(d) { 
    if (inputValue_date=='2018'){
        d.dataYear = +d.Year_2018;}
        else if(inputValue_date=='2017'){
        d.dataYear = +d.Year_2017;
        }
        else if(inputValue_date=='2016'){
            d.dataYear = +d.Year_2016;
            }
        else if(inputValue_date=='2015'){
                d.dataYear = +d.Year_2015;
            }
            else if(inputValue_date=='2014'){
                d.dataYear = +d.Year_2014;
            }
            else if(inputValue_date=='2013'){
                d.dataYear = +d.Year_2013;
            }
            else if(inputValue_date=='2014'){
                d.dataYear = +d.Year_2014;
            }
            else if(inputValue_date=='2013'){
                d.dataYear = +d.Year_2013;
            }
            else if(inputValue_date=='2012'){
                d.dataYear = +d.Year_2012;
            }
            else if(inputValue_date=='2011'){
                d.dataYear = +d.Year_2011;
            }
            else if(inputValue_date=='2010'){
                d.dataYear = +d.Year_2010;
            }
            else if(inputValue_date=='2009'){
                d.dataYear = +d.Year_2009;
            }
            else if(inputValue_date=='2008'){
                d.dataYear = +d.Year_2008;
            }
            else if(inputValue_date=='2007'){
                d.dataYear = +d.Year_2007;
            }
            else if(inputValue_date=='2006'){
                d.dataYear = +d.Year_2006;
            }
            else if(inputValue_date=='2005'){
                d.dataYear = +d.Year_2005;
            }
            else if(inputValue_date=='2004'){
                d.dataYear = +d.Year_2004;
            }
            else if(inputValue_date=='2003'){
                d.dataYear = +d.Year_2003;
            }
            else if(inputValue_date=='2002'){
                d.dataYear = +d.Year_2002;
            }
            else if(inputValue_date=='2001'){
                d.dataYear = +d.Year_2001;
            }
            else if(inputValue_date=='2000'){
                d.dataYear = +d.Year_2000;
            }
            else if(inputValue_date=='1999'){
                d.dataYear = +d.Year_1999;
            }
            else if(inputValue_date=='1995'){
                d.dataYear = +d.Year_1995;
            }
            else if(inputValue_date=='1990'){
                d.dataYear = +d.Year_1990;
            }
            else if(inputValue_date=='avg'){
                d.dataYear = +d.avg;
            }
    countryById.set(d.state, d);
  });
//   console.log(dataYear);
var dataYear=[];
for (var i=0; i<51; i++){
//   console.log(un[0].dataYear);
//   dataYear=un[0].dataYear;
  dataYear.push(un[i].dataYear);
          }
console.log(dataYear);

    colorScale.domain(d3.extent(un, function(d) {
        console.log(d.dataYear);
        return d.dataYear;}));


    var states = topojson.feature(usa, usa.objects.units).features;

    svg.selectAll('path.states')
        .data(states)
        .enter()
        .append('path')
        .attr('class', 'states')
        .attr('d', path)
        .on('mouseover', tip.show)
        .on('mouseout', tip.hide)
        .attr('fill', function(d) {
            // console.log(d.properties.name);
            return getColor(d);
        })
        .append("title");

    var linear = colorScale;
    
    svg.append("g")
      .attr("class", "legendLinear")
      .attr("transform", "translate(20,20)");

    var legendLinear = d3.legend.color()
      .shapeWidth(30)
      .orient('horizontal')
      .scale(linear);

    svg.select(".legendLinear")
      .call(legendLinear);

}

};
// var strMarriage=`http://127.0.0.1:5000/api/v1.0/MarriageByState`;

main('avg',"Resources/state_marriage.JSON");
headGranim();

function headGranim(){
    var granimInstance = new Granim({
        element: '#logo-canvas',
        direction: 'left-right',
        states : {
            "default-state": {
                gradients: [
                    ['#4CB8C4', '#3CD3AD'],
                    ['#24C6DC', '#514A9D'],
    
                ],
                transitionSpeed: 2000
            }
        }
    });
    
    granimInstance.play();
}

