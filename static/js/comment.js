console.log('i am comment js')

$( document ).ready(function() {
    let display = false
   
    $(".cmt_btn").click(function () {
        if (display===false) {
            $(".comment-box").show("slow");
            display=true
        } else {
            $(".comment-box").hide("slow");
            display=false
        }  
    });
  
// $( document ).ready(function() {
    
//     $(".cmt_btn").click(function () {
      
//         var x = document.querySelector('.comment-box');
//   if (x.style.display === "none") {
//     x.style.display = "block";
//   } else {
//     x.style.display = "none";
//   }
    
//     });
 });
  