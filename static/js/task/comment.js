$(document).ready(function(){
   
   //txtTaskComment
   //btnAddTask

   /** Apartado para los comentarios **/

   $("#btnAddCommentTask").click(function(){
       
      var txtComment=$("#txtTaskComment").val();
      var taskid    =$("#taskid").attr("value");
      var token     =$("#token").attr("value");
     
      $.ajax({  
      
        url   : "/comment/addfortask",
        type    : "POST",
        data    : $("#frmComment").serialize(),
        success : function(result){
          $("#taskCommentBody").prepend(result); 
          $("#comment").val("");
          changeColorLastRow();

          }
      });
      
   });

   
   loadInitialComments();
   expandTextarea('comment');
   
   
   
   function loadInitialComments(){
       
      var taskid    =$("#taskid").attr("value");
      var token     =$("#token").attr("value");
    
      $.ajax({  
			
			  url		: "/comment/list",
			  type		: "POST",
			  data		: { taskid: taskid, csrfmiddlewaretoken:token },
			  success	: function(result){
				  $("#taskCommentBody").prepend(result); 
				  $("#txtTaskComment").val("");
		      }
	    }); 
      //listByTaskId 
   }
   


   
   
   function changeColorLastRow(){
       $(".comment-row:first").addClass("bg-success");
       setTimeout(function(){
           $(".comment-row:first").removeClass("bg-success");
            },
        3000);
       
   }
   
   
   function expandTextarea(id) {
        var $element = $('#' + id).get(0);  
        
        $element.addEventListener('keyup', function() {
            this.style.overflow = 'hidden';
            this.style.height = 0;
            this.style.height = this.scrollHeight + 'px';
        }, false);
    }
   
});