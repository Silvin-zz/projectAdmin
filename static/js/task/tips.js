$(document).ready(function(){
    
    listTips();
   
   
   $("#btnAddTipTask").on("click",function(){
       addTip();
   });
   
   function addTip(){
       
       $.ajax({  
			
			  url		:  "/tips/add",
			  type		:  "POST",
			  data		:  $("#frmTips").serialize(),
			  success	: function(result){
			      $("#taskTipsBody").prepend(result);
		      },
		      error: function(XMLHttpRequest, textStatus, errorThrown) { 
                   
                }   
	    }); 
   }
   
   
   
   
   function listTips(){
       
       $.ajax({  
			
			  url		:  "/tips/list",
			  type		:  "POST",
			  data		:  $("#frmTips").serialize(),
			  success	: function(result){
			      $("#taskTipsBody").html(result);
		      },
		      error: function(XMLHttpRequest, textStatus, errorThrown) { 
                    
                }   
	    }); 
   }
});