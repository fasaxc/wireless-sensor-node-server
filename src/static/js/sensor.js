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
  
});
