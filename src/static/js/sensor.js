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
      chartData.addColumn('number', 'Date');
      chartData.addColumn('number', 'Temperature/C');
      chartData.addRows(data["readings"]);
      
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
