// *.js file for Javascript exercises
function myFunction() {
  const text = document.getElementById("doge_text");
  
  if (text.innerHTML == "You got a Doge!") {
    text.innerHTML = "You don't have a Doge.";
  }
  else {
    text.innerHTML = "You got a Doge!";
  }
}