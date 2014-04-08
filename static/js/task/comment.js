$(document).ready(function(){
   
   //txtTaskComment
   //btnAddTask
   
   loadInitialComments();
   
   
   
   function loadInitialComments(){
       
      var taskid    =$("#taskid").attr("value");
      var token     =$("#token").attr("value");
     alert(taskid + "------------------" + token);
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
				  $("#taskCommentBody").prepend(result); 
				  $("#txtTaskComment").val("");
		      }
	    });
      
   });
   
    /*
    
    */
   
});