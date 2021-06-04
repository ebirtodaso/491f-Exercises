// *.js file for Javascript exercises

//Function waits for doge to be clicked and gives a response
$(document).ready(function(){
  $("#doge_button").click(function(){
    $(this).remove();
    $("#doge_alert").attr("class","alert alert-success")
    $("#doge_text").text("You got a doge!");
  });
});

/*function myFunction() {
  const text = document.getElementById("doge_text");
  
  if (text.innerHTML == "You got a Doge!") {
    text.innerHTML = "You don't have a Doge.";
  }
  else {
    text.innerHTML = "You got a Doge!";
  }
}*/
