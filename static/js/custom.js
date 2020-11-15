console.log('i am custom javascript')





$(document).ready(function(){ 

  
    $(".cust_alert").fadeOut(4000);
 
});

// Get the modal
var modal = document.getElementById("myModal");
console.log(modal)
// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.querySelector(".img-profile");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}


// gallary photo
$(document).on("click", '[data-toggle="lightbox"]', function(event) {
  event.preventDefault();
  $(this).ekkoLightbox();
});



