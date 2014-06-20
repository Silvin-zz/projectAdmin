$(document).ready(function(){
/* jQueryKnob */
    $(".knob").knob();
    gettasks();
    function gettasks(){


      $.ajax({  
      
        url   : "/tasks/dashboard",
        type    : "POST",
        data    : $("#frmGetTargets").serialize(),
        success : function(result){
          $("#pad").html(result); 
          }
      });


    }
});