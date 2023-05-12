// make button work

window.addEventListener("DOMContentLoaded", (event) => {
  var hButton = document.getElementById("higherButton"); 
  var lButton = document.getElementById("lowerButton"); 
  var nextButton = document.getElementById("nextButton");
  var sample = Math.floor(Math.random()*10000);
  var sample2 = Math.floor(Math.random()*10000);

  var str = sample + " is HIGHER or LOWER than " + sample2;

  var clicked = false;

  
      
  document.getElementById('text').innerHTML = str;
  console.log("WORKED");
  document.getElementById("nextButton").style.visibility="hidden";

  if (hButton == null) {
      console.log("hButton is null");
  }
  else {
  hButton.addEventListener("click", function() {
      if (sample > sample2) {
          document.getElementById("para").innerHTML = "DING DING DING";
          document.getElementById("para").style.color = "green";
      }
      else {
          document.getElementById("para").innerHTML = "WRONG";
          document.getElementById("para").style.color = "red";
      }
      clicked = true;
      console.log("higher clicked");
      document.getElementById("nextButton").style.visibility="visible";
    });
  }
  
  if (lButton == null) {
      console.log("lButton is null");
  }
  else {
  lButton.addEventListener("click", function() {
      if (sample > sample2) {
          document.getElementById("para").innerHTML = "WRONG";
          document.getElementById("para").style.color = "red";
      }
      else {
          document.getElementById("para").innerHTML = "DING DING DING";
          document.getElementById("para").style.color = "green";
      }
      console.log("lower clicked");
      clicked = true;
      document.getElementById("nextButton").style.visibility="visible";
    });
  }

  if (nextButton == null) {
    console.log("nextButton is null");
}
else {
nextButton.addEventListener("click", function() {
    
    console.log("next clicked");
    clicked = false;
    document.getElementById("nextButton").style.visibility="hidden";
  });
}
  });
  