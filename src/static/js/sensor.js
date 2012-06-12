$(window).load(function(){ 
  // Place for us to stash debug info for JS console access.
  window.sensors = {};
  
  // ---------------------------------------------------------------------------
  // Utility functions
  // ---------------------------------------------------------------------------
  function log(msg) {
    try{
      console.log(msg);
    } catch (e) {
      // Browser doesn't support console.
    }
  }
  
  // ---------------------------------------------------------------------------
  // Startup.
  // ---------------------------------------------------------------------------
  
  function getData(success) {
    jQuery.getJSON("/readings", null, function(data) {
      log("Downloaded " + data["readings"].length + " readings");
      window.sensors["data"] = data;
      var chartData = new google.visualization.DataTable();
      chartData.addColumn('datetime', 'Date');
      chartData.addColumn('number', 'Living room/C');
      chartData.addColumn('number', 'Balcony/C');
      chartData.addColumn('number', 'Bedroom/C');
      
      var readings = data["readings"];
      for (var i = 0; i < readings.length; i++) {
        readings[i][0] = new Date(readings[i][0]*1000);
      }
      
      chartData.addRows(readings);
      
      success(chartData);
    })
    .error(function() {
      log("Failed to load readings");
    });
  }

  // Set chart options
  var options = {
      'title':'Temperature',
      'backgroundColor': 'whiteSmoke',
      'height': 760,
      'thickness': 2,
      'hAxis': {'format': 'd MMM ha',
                'slanted_text': true}
  };
  
  var chartBuffers = [
    {"chart": new google.visualization.AnnotatedTimeLine(document.getElementById('chart_div0')),
     "element": "#chart_div0"},
    {"chart": new google.visualization.AnnotatedTimeLine(document.getElementById('chart_div1')),
     "element": "#chart_div1"},
  ];
  var currentChart = 0;
  
  function redrawChart() {
    getData(function(chartData) {
      log("Redrawing chart");
      var oldBuffer = chartBuffers[currentChart];
      currentChart = (currentChart + 1) % chartBuffers.length;
      var newBuffer = chartBuffers[currentChart];
      
      newBuffer.chart.draw(chartData, options);
      setTimeout(function(){
        log("Flipping banks");
        $(oldBuffer.element).css("z-index", "50");
        $(newBuffer.element).css("z-index", "100");
      }, 2000);
    });
  }
  
  redrawChart();
  setInterval(redrawChart, 4 * 60 * 1000);
});
