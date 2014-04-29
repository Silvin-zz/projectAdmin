$(document).ready(function(){
   
   //txtTaskComment
   //btnAddTask
   
   loadInitialComments();
   expandTextarea('txtTaskComment');
   
   
   
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
   
   $("#btnAddTask").click(function(){
       
      var txtComment=$("#txtTaskComment").val();
      var taskid    =$("#taskid").attr("value");
      var token     =$("#token").attr("value");
     
      $.ajax({  
			
			  url		: "/comment/add",
			  type		: "POST",
			  data		: { comment: txtComment, taskid: taskid, csrfmiddlewaretoken:token },
			  success	: function(result){
			      $(".comment-row:first").removeClass("bg-success");
				  $("#taskCommentBody").prepend(result); 
				  $("#txtTaskComment").val("");
				  changeColorLastRow();
		      }
	    });
      
   });
   
   
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