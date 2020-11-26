console.log('i am custom javascript')

$(document).ready(function(){ 

  
    $(".cust_alert").fadeOut(6000);
 
});



// Get the modal
var modal = document.getElementById('id{{userpost.id}}');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


