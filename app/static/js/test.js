// make button work

window.addEventListener("DOMContentLoaded", (event) => {
  var hButton = document.getElementById("higherButton"); 
  var lButton = document.getElementById("lowerButton"); 
  var sample = 10000;
  var sample2 = 15000;

  if (hButton == null) {
      console.log("hButton is null");
  }
  else {
  hButton.addEventListener("click", function() {
      if (sample < sample2) {
          document.getElementById("para").innerHTML = "DING DING DING";
      }
      else {
          document.getElementById("para").innerHTML = "WRONG";
      }
      console.log("higher clicked");
    });
  }
  
  if (lButton == null) {
      console.log("lButton is null");
  }
  else {
  lButton.addEventListener("click", function() {
      if (sample < sample2) {
          document.getElementById("para").innerHTML = "WRONG";
      }
      else {
          document.getElementById("para").innerHTML = "DING DING DING";
      }
      console.log("higher clicked");
    });
  }
  });
  