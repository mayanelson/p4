// make button work
window.addEventListener("DOMContentLoaded", (event) => {
  var hButton = document.getElementById("higherButton"); 
  var lButton = document.getElementById("lowerButton"); 
  var nextButton = document.getElementById("nextButton");
  var mappy = document.getElementById("map");
  var sample = boro_data1
  var sample2 = boro_data2
  console.log()
  var str = `${db_name} in ${boro_name1} or ${boro_name2}`

  hButton.innerHTML = boro_name1
  lButton.innerHTML = boro_name2
  var clicked = false;

  
      
  document.getElementById('text').innerHTML = str;
  console.log("WORKED");
  document.getElementById("nextButton").style.visibility="hidden";
  document.getElementById("map").style.visibility="hidden";


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
      //map.style.display = "inline-block";
      console.log("higher clicked");
      document.getElementById("nextButton").style.visibility="visible";
      document.getElementById("map").style.visibility="visible";
      document.getElementById("maptitle").innerHTML = "cool map";
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
      document.getElementById("map").style.visibility="visible";
      document.getElementById("maptitle").innerHTML = "cool map";
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
    document.getElementById("map").style.visibility="hidden";
  });
}
  });