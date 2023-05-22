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
  var map = L.map('map').setView([40.71, -74.00], 10);

  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
      }).addTo(map);  
  L.circleMarker([40.7781, -73.9712], {radius: boroData[2]}).addTo(map); //MANHATTAN
  L.circleMarker([40.6782, -73.9442], {radius: boroData[0]}).addTo(map); //BROOKLYN
  L.circleMarker([40.7282, -73.7949], {radius: boroData[3]}).addTo(map); //QUEENS
  L.circleMarker([40.5795, -74.1502], {radius: boroData[4]}).addTo(map); //STATEN ISLAND
  L.circleMarker([40.8448, -73.8648], {radius: boroData[1]}).addTo(map); // BRONX

}

window.addEventListener("DOMContentLoaded", (event) => {
  streak = localStorage.getItem("streak");
  if (streak == null){
    document.getElementById("streak").innerHTML = `Streak: 0`;
  }
  else{
    document.getElementById("streak").innerHTML = `Streak: ${streak}`;
  }
  num_streak = Number(streak);
  console.log(`the streak before guessing is ${streak}`)

  //streak = Number(document.getElementById("streak").innerHTML);
  var hButton = document.getElementById("higherButton"); 
  var lButton = document.getElementById("lowerButton"); 
  var nextButton = document.getElementById("nextButton");
  var mappy = document.getElementById("map");
  var sample = boro_data1;
  var sample2 = boro_data2;
  console.log()
  var str = `${db_name} in ${boro_name1} or ${boro_name2}`

  hButton.innerHTML = boro_name1
  lButton.innerHTML = boro_name2
  var clicked = false;
  var counter = 0;

  
      
  document.getElementById('text').innerHTML = str;
  console.log("WORKED");
  document.getElementById("nextButton").style.visibility="hidden";
  document.getElementById("map").style.visibility="hidden";


  if (hButton == null) {
      console.log("hButton is null");
  }
  else {
  hButton.addEventListener("click", function() {
      hButton.innerHTML =  `The real number for ${boro_name1}: ${sample}`
      lButton.innerHTML = `The real number for ${boro_name2}: ${sample2}`
      if (Number(sample) >= Number(sample2)) {
          document.getElementById("para").innerHTML = "DING DING DING";
          document.getElementById("para").style.color = "green";
          console.log(`${boro_name1}'s ${sample} is greater than ${boro_name2}'s ${sample2}`);
          num_streak += 1;
          console.log(`num_streak is ${num_streak}`);
      }
      else {
          document.getElementById("para").innerHTML = "WRONG";
          document.getElementById("para").style.color = "red";
          console.log(`${boro_name1}'s ${sample} is less than ${boro_name2}'s ${sample2}`);
          num_streak = 0;
          console.log(`num_streak is ${num_streak}`);
      }
      clicked = true;
      //map.style.display = "inline-block";
      makeMap(data);
      console.log("higher clicked");
      document.getElementById("nextButton").style.visibility="visible";
      document.getElementById("map").style.visibility="visible";
      document.getElementById("maptitle").innerHTML = "cool map";
      console.log(`num_streak is ${num_streak}`);
      streak = num_streak.toString();
      console.log(`streak is ${streak}`)
      localStorage.setItem("streak", streak);
      console.log(`streak after guessing is ${localStorage.getItem("streak")}`);
      document.getElementById("streak").innerHTML = `Streak: ${streak}`;
    });

  }
  
  if (lButton == null) {
      console.log("lButton is null");
  }
  else {
  lButton.addEventListener("click", function() {
      hButton.innerHTML =  `The real number for ${boro_name1}: ${sample}`
      lButton.innerHTML = `The real number for ${boro_name2}: ${sample2}`
      if (Number(sample) > Number(sample2)) {
          document.getElementById("para").innerHTML = "WRONG";
          document.getElementById("para").style.color = "red";
          console.log(`${boro_name1}'s ${sample} is greater than ${boro_name2}'s ${sample2}`)
          num_streak = 0;
          console.log(`num_streak is ${num_streak}`);
      }
      else {
          document.getElementById("para").innerHTML = "DING DING DING";
          document.getElementById("para").style.color = "green";
          console.log(`${boro_name1}'s ${sample} is less than ${boro_name2}'s ${sample2}`)
          num_streak += 1;
          console.log(`num_streak is ${num_streak}`);

      }
      console.log("lower clicked");
      clicked = true;
      makeMap(data);
      document.getElementById("nextButton").style.visibility="visible";
      document.getElementById("map").style.visibility="visible";
      document.getElementById("maptitle").innerHTML = "cool map";
      console.log(`num_streak is ${num_streak}`);
      streak = num_streak.toString();
      console.log(`streak is ${streak}`)
      localStorage.setItem("streak", streak);
      console.log(`streak after guessing is ${localStorage.getItem("streak")}`);
      document.getElementById("streak").innerHTML = `Streak: ${streak}`;
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
