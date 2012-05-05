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
  function drawChart() {

    jQuery.getJSON("/readings", null, function(data) {
      log("Downloaded " + data["readings"].length + " readings");
      window.sensors["data"] = data;
      var chartData = new google.visualization.DataTable();
      chartData.addColumn('datetime', 'Date');
      chartData.addColumn('number', 'Temperature/C');
      
      var readings = data["readings"];
      for (var i = 0; i < readings.length; i++) {
        readings[i][0] = new Date(readings[i][0]);
      }
      
      chartData.addRows(readings);
      
      // Set chart options
      var options = {'title':'Temperature',
                     'width': 900,
                     'height':600};

      // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
      chart.draw(chartData, options);
    })
    .error(function() {
      log("Failed to load readings");
    });
  }
  
  drawChart();
});
