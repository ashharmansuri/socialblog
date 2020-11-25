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
  

    $('.like-form').submit(function(e){
         e.preventDefault
         const post_id = $(this)
         console.log(post_id)
    });
   
 });
  