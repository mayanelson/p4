// make button work

window.addEventListener("DOMContentLoaded", (event) => {
var button = document.getElementById("buttonClick"); 
if (button == null) {
    console.log("button is null");
}
else {
button.addEventListener("click", function() {
    document.getElementById("para").innerHTML = "insert game here";
    console.log("button clicked");
  });
}
});
