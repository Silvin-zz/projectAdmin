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
			      clearTipForm();
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
   
   
   
   function clearTipForm(){
       debugger;
       $("#taskTitle").val("");
       $("#tipKeywords").val("");
       $("#descriptionTip").val("");
       
   }
});