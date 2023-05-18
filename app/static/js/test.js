// make button work
function makeMap(data){
  data.shift();
  var boroData = data.map(function(x){
    return parseInt(x, 10);
  });
  //console.log(boroData)
  console.log(boroData)
  const max = Math.max.apply(Math, boroData)
  const scaler = 50;
  //console.log(max);

  boroData =  data.map(function(x){
    return (x / max) * scaler;
  });
  console.log(boroData);
  //console.log(boroData[0])
  var map = L.map('map').setView([40.71, -74.00], 11);

  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
      }).addTo(map);
  bkNormal = data;
  L.circleMarker([40.7781, -73.9712], {radius: boroData[2]}).addTo(map); //MANHATTAN
  L.circleMarker([40.6782, -73.9442], {radius: boroData[0]}).addTo(map); //BROOKLYN
  L.circleMarker([40.7282, -73.7949], {radius: boroData[3]}).addTo(map); //QUEENS
  L.circleMarker([40.5795, -74.1502], {radius: boroData[4]}).addTo(map); //STATEN ISLAND
  L.circleMarker([40.8448, -73.8648], {radius: boroData[1]}).addTo(map); // BRONX

}
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
      makeMap(data);
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